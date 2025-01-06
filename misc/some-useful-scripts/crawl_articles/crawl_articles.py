# Last Modified: 2025-01-06
# Description: A Python script to crawl articles from various databases based on user-selected keywords.

# -*- coding: utf-8 -*-
import sys
import os
import requests
from bs4 import BeautifulSoup
import bibtexparser
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from scholarly import scholarly
import threading
import argparse
import aiohttp
import asyncio
import time
import psutil
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import fonts
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import signal

# Default keywords to search for articles
default_keywords = [
    "reconfiguration problem",
    "reconfiguration graph",
    "combinatorial reconfiguration",
    "solution graph",
    "reconfiguration puzzle",
    "reconfiguring",
    "token swap",
    "token sliding",
    "sliding cube",
    "sliding block",
    "token graph",
    "supertoken graph",
    "Johnson graph",
    "double vertex graph",
    "flip graph",
    "Fibonacci cube",
    "simplex graph",
    "token jumping",
    "token addition removal",
    "recolor",
    "recolour"
]

# Default data sources to fetch existing titles from
data_sources = ["https://reconf.wdfiles.com/local--files/papers/core-pubs.bib"]
# data_sources = [] # No default data sources, for testing purposes

# Fetch existing titles from a given URL containing a BibTeX file
def fetch_existing_titles(sources):
    """
    Fetch existing article titles from a list of data sources.

    Args:
        sources (list): A list of URLs or file paths that contain BibTeX data.

    Returns:
        set: A set of lowercased article titles without surrounding braces.
    """
    print("Fetching existing titles from data sources...")
    existing_titles = set()
    for source in sources:
        try:
            local_filename = os.path.basename(source)
            if source.startswith('http'):
                # Check if a local copy of the BibTeX data exists
                if os.path.exists(local_filename):
                    # Load the BibTeX data from the local file
                    with open(local_filename, 'r', encoding='utf-8') as local_file:
                        bib_database = bibtexparser.load(local_file)
                else:
                    # Fetch the BibTeX data from the URL
                    response = requests.get(source, timeout=10)
                    response.raise_for_status()
                    bib_database = bibtexparser.loads(response.text)
                    # Save a local copy of the BibTeX data
                    with open(local_filename, 'w', encoding='utf-8') as local_file:
                        local_file.write(response.text)
            else:
                # Load the BibTeX data from a local file
                with open(source, 'r', encoding='utf-8') as bibfile:
                    bib_database = bibtexparser.load(bibfile)
            # Extract and clean titles, then add them to the set
            existing_titles.update({entry['title'].lower().strip('{}') for entry in bib_database.entries})
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching titles from URL '{source}': {e}")
        except Exception as e:
            print(f"An error occurred while fetching titles from source '{source}': {e}")
    return existing_titles

# Fetch articles from arXiv based on keywords and filter by existing titles and years
async def fetch_arxiv_articles(keywords, existing_titles, years, limit=20, verbose=False):
    """
    Fetch articles from arXiv based on keywords, filtering by existing titles and years.

    Args:
        keywords (list): List of keywords to search for.
        existing_titles (set): Set of existing article titles to filter out.
        years (int): Number of years back to search for articles.
        limit (int, optional): Maximum number of articles to fetch per keyword. Defaults to 20.
        verbose (bool, optional): If True, print additional logs. Defaults to False.

    Returns:
        list: A list of articles with details such as id, title, author, journal, year, url, and doi.
    """
    print("Fetching articles from arXiv...")
    base_url = "http://export.arxiv.org/api/query?search_query=all:{}&start=0&max_results={}"
    articles = []
    titles_seen = set()
    current_year = datetime.now().year

    async def fetch_keyword(session, keyword):
        """
        Fetch and process articles for a specific keyword from arXiv.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            keyword (str): The keyword to search for in arXiv.
        """
        try:
            if verbose:
                print(f"Processing keyword '{keyword}' in arXiv")
            # Send request to arXiv API
            async with session.get(base_url.format(keyword.lower().replace(" ", "+"), limit)) as response:
                response_text = await response.text()
                soup = BeautifulSoup(response_text, 'xml')
                entries = soup.find_all('entry')
                for entry in entries:
                    year = int(entry.published.text[:4])
                    title = entry.title.text
                    title_lower = title.lower().strip('{}')
                    # Skip if title already seen or too old
                    if title_lower in existing_titles or title_lower in titles_seen:
                        continue
                    if current_year - year <= years:
                        # Compile article information
                        article = {
                            'id': entry.id.text.split('/')[-1],
                            'title': title,
                            'author': ' and '.join([author.find('name').text for author in entry.find_all('author')]),
                            'journal': 'arXiv preprint',
                            'year': str(year),
                            'url': entry.id.text
                        }
                        # Check for DOI
                        doi_tag = entry.find('arxiv:doi', {'xmlns:arxiv': 'http://arxiv.org/schemas/atom'})
                        if doi_tag:
                            article['doi'] = doi_tag.text
                        articles.append(article)
                        titles_seen.add(title_lower)
        except Exception as e:
            if verbose:
                print(f"An error occurred while fetching articles for keyword '{keyword}' from arXiv: {e}")

    # Create an aiohttp session and gather tasks for fetching articles by keyword
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_keyword(session, keyword) for keyword in keywords]
        await asyncio.gather(*tasks)

    return articles

# Fetch articles from DBLP based on keywords and filter by existing titles and years
async def fetch_dblp_articles(keywords, existing_titles, years, limit=20, verbose=False):
    """
    Fetch articles from DBLP based on keywords, filtering by existing titles and years.

    Args:
        keywords (list): List of keywords to search for.
        existing_titles (set): Set of existing article titles to filter out.
        years (int): Number of years back to search for articles.
        limit (int, optional): Maximum number of articles to fetch per keyword. Defaults to 20.
        verbose (bool, optional): If True, print additional logs. Defaults to False.

    Returns:
        list: A list of articles with details such as id, title, author, journal, year, url, and doi.
    """
    print("Fetching articles from DBLP...")
    base_url = "https://dblp.org/search/publ/api?q={}&h={}&format=json"
    articles = []
    titles_seen = set()
    current_year = datetime.now().year

    async def fetch_keyword(session, keyword):
        """
        Fetch and process articles for a specific keyword from DBLP.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            keyword (str): The keyword to search for in DBLP.
        """
        try:
            if verbose:
                print(f"Processing keyword '{keyword}' in DBLP")
            # Send request to DBLP API
            async with session.get(base_url.format(keyword.lower().replace(" ", "+"), limit)) as response:
                data = await response.json()
                for entry in data.get('result', {}).get('hits', {}).get('hit', []):
                    info = entry.get('info', {})
                    year = int(info.get('year', 0))
                    title = info.get('title', '')
                    title_lower = title.lower().strip('{}').removesuffix('.')
                    # Skip if title already seen or too old
                    if title_lower in existing_titles or title_lower in titles_seen:
                        continue
                    if current_year - year <= years:
                        authors = info.get('authors', {}).get('author', [])
                        # Extract author names and filter out digits
                        if isinstance(authors, list):
                            author_names = ' and '.join([''.join(filter(lambda x: not x.isdigit(), a.get('text', ''))) for a in authors])
                        else:
                            author_names = ''.join(filter(lambda x: not x.isdigit(), authors.get('text', 'N/A')))
                        # Consider only computer science or math articles
                        if 'cs' in info.get('type', '').lower() or 'math' in info.get('type', '').lower():
                            article = {
                                'id': info.get('key', 'N/A'),
                                'title': title,
                                'author': author_names,
                                'journal': 'DBLP',
                                'year': str(year),
                                'url': info.get('url', 'N/A')
                            }
                            if 'doi' in info:
                                article['doi'] = info['doi']
                            articles.append(article)
                            titles_seen.add(title_lower)
        except Exception as e:
            if verbose:
                print(f"An error occurred while fetching articles for keyword '{keyword}' from DBLP: {e}")

    # Create an aiohttp session and gather tasks for fetching articles by keyword
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_keyword(session, keyword) for keyword in keywords]
        await asyncio.gather(*tasks)

    return articles

# Fetch articles from Semantic Scholar based on keywords and filter by existing titles and years
async def fetch_semantic_scholar_articles(keywords, existing_titles, years, limit=20, verbose=False):
    """
    Fetch articles from Semantic Scholar based on keywords, filtering by existing titles and years.

    Args:
        keywords (list): List of keywords to search for.
        existing_titles (set): Set of existing article titles to filter out.
        years (int): Number of years back to search for articles.
        limit (int, optional): Maximum number of articles to fetch per keyword. Defaults to 20.
        verbose (bool, optional): If True, print additional logs. Defaults to False.

    Returns:
        list: A list of articles with details such as id, title, author, journal, year, url, and doi.
    """
    print("Fetching articles from Semantic Scholar...")
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query={}&limit={}"
    articles = []  # List to store articles
    titles_seen = set()  # Set to track seen titles
    current_year = datetime.now().year  # Current year for filtering

    async def fetch_keyword(session, keyword):
        """
        Fetch and process articles for a specific keyword from Semantic Scholar.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            keyword (str): The keyword to search for in Semantic Scholar.
        """
        try:
            if verbose:
                print(f"Processing keyword '{keyword}' in Semantic Scholar")
            # Send request to Semantic Scholar API
            async with session.get(base_url.format(keyword.lower().replace(" ", "+"), limit)) as response:
                data = await response.json()
                for entry in data.get('data', []):
                    year = int(entry.get('year', 0))
                    title = entry.get('title', '')
                    title_lower = title.lower().strip('{}')
                    # Skip if title already seen or too old
                    if title_lower in existing_titles or title_lower in titles_seen:
                        continue
                    if current_year - year <= years:
                        authors = entry.get('authors', [])
                        author_names = ' and '.join([a.get('name', 'N/A') for a in authors])
                        fields_of_study = entry.get('fieldsOfStudy', [])
                        # Consider articles in computer science or mathematics
                        if 'Computer Science' in fields_of_study or 'Mathematics' in fields_of_study:
                            article = {
                                'id': entry.get('paperId', 'N/A'),
                                'title': title,
                                'author': author_names,
                                'journal': 'Semantic Scholar',
                                'year': str(year),
                                'url': entry.get('url', 'N/A')
                            }
                            if 'doi' in entry:
                                article['doi'] = entry['doi']
                            articles.append(article)
                            titles_seen.add(title_lower)
        except Exception as e:
            if verbose:
                print(f"An error occurred while fetching articles for keyword '{keyword}' from Semantic Scholar: {e}")

    # Create an aiohttp session and gather tasks for fetching articles by keyword
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_keyword(session, keyword) for keyword in keywords]
        await asyncio.gather(*tasks)

    return articles

# Fetch articles from Google Scholar based on keywords and filter by existing titles and years
async def fetch_google_scholar_articles(keywords, existing_titles, years, limit=20, verbose=False):
    """
    Fetch articles from Google Scholar based on keywords and filter by existing titles and years.

    Args:
        keywords (list): List of keywords to search for.
        existing_titles (set): Set of existing article titles to filter out.
        years (int): Number of years back to search for articles.
        limit (int, optional): Maximum number of articles to fetch per keyword. Defaults to 20.
        verbose (bool, optional): If True, print additional logs. Defaults to False.

    Returns:
        list: A list of articles with details such as id, title, author, journal, year, url, and doi.
    """
    print("Fetching articles from Google Scholar...")
    articles = []
    titles_seen = set()
    current_year = datetime.now().year

    async def fetch_keyword(keyword):
        """
        Fetch and process articles for a specific keyword from Google Scholar.

        Args:
            keyword (str): The keyword to search for in Google Scholar.
        """
        if verbose:
            print(f"Processing keyword '{keyword}' in Google Scholar")
        try:
            search_query = scholarly.search_pubs(keyword)
            for j, entry in enumerate(search_query):
                if j >= limit:
                    break
                bib = entry.get('bib', {})
                year = int(entry.get('pub_year', 0))
                title = bib.get('title', '').lower().strip('{}')
                if not title or title in existing_titles or title in titles_seen or current_year - year > years:
                    continue
                article = {
                    'id': entry.get('pub_url', 'N/A').split('/')[-1],
                    'title': bib['title'],
                    'author': ' and '.join(bib.get('author', [])),
                    'journal': entry.get('venue', 'Google Scholar'),
                    'year': str(year),
                    'url': entry.get('pub_url', 'N/A')
                }
                if 'doi' in entry:
                    article['doi'] = entry['doi']
                articles.append(article)
                titles_seen.add(title)
        except Exception as e:
            if verbose:
                print(f"An error occurred while fetching articles for keyword '{keyword}' from Google Scholar: {e}")

    await asyncio.gather(*(fetch_keyword(keyword) for keyword in keywords))

    return articles

# Fetch articles from zbMATH based on keywords and filter by existing titles and years
async def fetch_zbmath_articles(keywords, existing_titles, years, limit=20, verbose=False):
    """
    Fetch articles from zbMATH based on keywords and filter by existing titles and years.

    Args:
        keywords (list): List of keywords to search for.
        existing_titles (set): Set of existing article titles to filter out.
        years (int): Number of years back to search for articles.
        limit (int, optional): Maximum number of articles to fetch per keyword. Defaults to 20.
        verbose (bool, optional): If True, print additional logs. Defaults to False.

    Returns:
        list: A list of articles with details such as id, title, author, journal, year, url, and doi.
    """
    print("Fetching articles from zbMATH...")
    base_url = "https://api.zbmath.org/v1/document/_search?search_string={}&page=0&results_per_page={}&sort=year:desc"
    articles = []
    titles_seen = set()
    current_year = datetime.now().year

    async def fetch_keyword(session, keyword):
        """
        Fetch and process articles for a specific keyword from zbMATH.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            keyword (str): The keyword to search for in zbMATH.
        """
        try:
            if verbose:
                print(f"Processing keyword '{keyword}' in zbMATH")
            async with session.get(base_url.format(keyword.lower().replace(" ", "+"), limit)) as response:
                data = await response.json()
                results = data.get('result', [])
                if not results:
                    if verbose:
                        print(f"No results found for keyword '{keyword}' in zbMATH")
                    return
                for entry in results[:limit]:
                    year = int(entry.get('year', 0))
                    title = entry.get('title', {}).get('title', 'N/A')
                    title_lower = title.lower().strip('{}')
                    if title_lower in existing_titles or title_lower in titles_seen:
                        continue
                    if current_year - year <= years:
                        authors = [a.get('name', 'N/A') for a in entry.get('contributors', {}).get('authors', [])]
                        author_names = ' and '.join(authors)
                        doi = next((link.get('identifier') for link in entry.get('links', []) if link.get('type') == "doi"), None)
                        article = {
                            'id': str(entry.get('id', 'N/A')),
                            'title': title,
                            'author': author_names,
                            'journal': 'zbMATH',
                            'year': str(year),
                            'url': f"https://zbmath.org/?q=an:{entry.get('id', 'N/A')}"
                        }
                        if doi:
                            article['doi'] = doi
                        articles.append(article)
                        titles_seen.add(title_lower)
        except Exception as e:
            if verbose:
                print(f"An error occurred while fetching articles for keyword '{keyword}' from zbMATH: {e}")

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_keyword(session, keyword) for keyword in keywords]
        await asyncio.gather(*tasks)

    return articles

# Convert articles to BibTeX format
def articles_to_bibtex(articles):
    """
    Convert a list of articles into a BibTeX database.

    :param articles: A list of dictionaries containing article details.
    :return: A BibTeX-formatted string representing the database.
    """
    try:
        # Create a new BibTeX database
        bib_database = bibtexparser.bibdatabase.BibDatabase()
        bib_database.entries = []
        for article in articles:
            # Create a new BibTeX entry from the article details
            entry = {
                'ENTRYTYPE': 'article',  # All entries are articles
                'ID': article['id'],  # Use the ID as the BibTeX key
                'title': f"{{{article['title']}}}",  # Title of the article with braces
                'author': article['author'],  # Authors of the article
                'journal': article['journal'],  # Journal or venue of the article
                'year': article['year']  # Year of publication
            }
            # Add the URL of the article
            entry['url'] = article['url']
            # If the article has a DOI, add it
            if 'doi' in article:
                entry['doi'] = article['doi']
            # If the article is an arXiv preprint, add the eprint field
            if article['journal'] == 'arXiv preprint':
                entry['eprint'] = article['id']
                entry['archivePrefix'] = 'arXiv'
            # Add the entry to the database
            bib_database.entries.append(entry)
        # Convert the database to a BibTeX-formatted string
        return bibtexparser.dumps(bib_database)
    except Exception as e:
        print(f"An error occurred while converting articles to BibTeX: {e}")
        return None

# Convert articles to HTML format
def articles_to_html(articles):
    """
    Convert a list of articles into an HTML document.

    :param articles: A list of dictionaries containing article details.
    :return: An HTML-formatted string representing the articles.
    """
    try:
        # Create a Jinja2 environment with a file system loader
        env = Environment(loader=FileSystemLoader('.'))

        # Define the default template for the HTML document
        default_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Reconfiguration Articles</title>
        </head>
        <body>
            <h1>Reconfiguration Articles</h1>
            <ol>
            {% for article in articles %}
                <li>
                    <strong>{{ article.title }}</strong><br>
                    Author(s): {{ article.author }}<br>
                    Journal: {{ article.journal }}<br>
                    Year: {{ article.year }}<br>
                    <a href="{{ article.url }}">Link</a>
                </li>
            {% endfor %}
            </ol>
        </body>
        </html>
        """

        # Write the default template to a temporary file called 'template.html'
        with open('template.html', 'w', encoding='utf-8') as template_file:
            template_file.write(default_template)

        # Get the Jinja2 template from the temporary file
        template = env.get_template('template.html')

        # Render the HTML document from the template and the list of articles
        html_content = template.render(articles=articles)

        # Write the rendered HTML document to a file called 'articles.html'
        with open('articles.html', 'w', encoding='utf-8') as htmlfile:
            htmlfile.write(html_content)

        # Attempt to remove the temporary 'template.html' file
        try:
            os.remove('template.html')
        except OSError as e:
            print(f"Error removing temporary template file: {e}")

        # Return the rendered HTML document
        return html_content

    except Exception as e:
        print(f"An error occurred while converting articles to HTML: {e}")
        return None

# Parse command-line arguments
def parse_arguments():
    """
    Parse command-line arguments for the script.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    # Create an ArgumentParser object to parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Crawl articles from various databases based on user-selected keywords."
    )

    # Add an argument to generate a requirements.txt file with all required Python packages
    parser.add_argument(
        '--requirements',
        action='store_true',
        help="Generate a requirements.txt file with all required Python packages"
    )

    # Add an argument to specify a comma-separated list of keywords to search for
    parser.add_argument(
        '-k',
        '--keywords',
        type=str,
        help="Comma-separated list of keywords to search for (e.g., 'reconfiguration problem, token swap')"
    )

    # Add an argument to specify the number of years back to search for articles
    parser.add_argument(
        '-y',
        '--years',
        type=int,
        help="Number of years back to search for articles (e.g., 5)"
    )

    # Add an argument to specify a comma-separated list of database names or numbers to search
    parser.add_argument(
        '-db',
        '--databases',
        type=str,
        help="Comma-separated list of database names or numbers to search (1: arXiv, 2: DBLP, 3: Semantic Scholar, 4: Google Scholar, 5: zbMATH). Example: '1,3,5'"
    )

    # Add an argument to print the list of default keywords as a comma-separated list
    parser.add_argument(
        '--print-default-keywords',
        action='store_true',
        help="Print the list of default keywords as a comma-separated list"
    )

    # Add an argument to use default settings for keywords, years, and databases
    parser.add_argument(
        '-d',
        '--default',
        action='store_true',
        help="Use default settings for keywords, years, and databases"
    )

    # Add an argument to specify a comma-separated list of additional data sources (URLs or file paths) to fetch existing titles from
    parser.add_argument(
        '-ds',
        '--data-sources',
        type=str,
        help="Comma-separated list of additional data sources (URLs or file paths) to fetch existing titles from (e.g., 'https://example.com/data.bib, /path/to/local/file.bib')"
    )

    # Add an argument to specify a limit on the number of resulting articles to fetch from each database
    parser.add_argument(
        '-l',
        '--limit',
        type=int,
        help="Limit on the number of resulting articles to fetch from each database (default: 20, e.g., 50)"
    )

    # Add an argument to remove all files generated by this script
    parser.add_argument(
        '-c',
        '--clean',
        action='store_true',
        help="Remove all files generated by this script"
    )

    # Add an argument to increase verbosity of the script output
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help="Increase verbosity of the script output"
    )

    # Add an argument to specify the output formats for the articles
    parser.add_argument(
        '-f',
        '--output-formats',
        type=str,
        help="Specify the output formats for the articles as a comma-separated list (e.g., 'bib,html,pdf')"
    )

    # Add an argument to enable debug mode to print all outputs and error messages to a txt file
    parser.add_argument(
        '--debug',
        action='store_true',
        help="Enable debug mode to print all outputs and error messages to a txt file"
    )

    # Add an argument to upload generated files to multiple services (Dropbox using rclone, temp.sh, or bashupload.com)
    parser.add_argument(
        '--upload',
        type=str,
        help="Upload generated files to multiple services. Specify 'dropbox:<directory>' for Dropbox, 'tempsh' for temp.sh, or 'bashupload' for bashupload.com, separated by commas (e.g., 'dropbox:my_dropbox_folder,tempsh,bashupload'). Use 'all' to upload to all available services."
    )

    # Parse the command-line arguments and return the parsed arguments
    return parser.parse_args()

# Function to validate command-line arguments
def validate_arguments(args):
    """
    Validate command-line arguments to ensure they are valid.

    Args:
        args: The parsed command-line arguments from argparse.

    Raises:
        ValueError: If any of the arguments are invalid.
    """
    # Helper function to check if a value is a non-negative integer
    def is_non_negative_integer(value, name):
        if value is not None and value < 0:
            raise ValueError(f"The {name} must be a non-negative integer.")

    # Helper function to check if a value is a positive integer
    def is_positive_integer(value, name):
        if value is not None and value <= 0:
            raise ValueError(f"The {name} must be a positive integer.")

    # Helper function to check if specified values are within a set of valid options
    def are_valid_options(values, valid_options, name):
        if values:
            specified_values = {v.strip().lower() for v in values.split(',')}
            if not specified_values.issubset(valid_options):
                raise ValueError(f"Invalid {name} specified. Valid options are {', '.join(valid_options)}.")

    # Validate years and limit arguments
    is_non_negative_integer(args.years, "number of years")
    is_positive_integer(args.limit, "limit on the number of articles")

    # Validate databases and output formats
    valid_databases = {'1', '2', '3', '4', '5', 'arxiv', 'dblp', 'semantic scholar', 'google scholar', 'zbmath'}
    are_valid_options(args.databases, valid_databases, "database")

    valid_formats = {'bib', 'html', 'pdf', 'all'}
    are_valid_options(args.output_formats, valid_formats, "output format")

    # Validate upload argument
    if args.upload:
        if args.clean:
            raise ValueError("The --upload argument cannot be used with --clean.")
        valid_services = {'dropbox', 'tempsh', 'bashupload', 'all'}
        upload_services = args.upload.split(',')
        for service in upload_services:
            if ':' in service:
                service_name, _ = service.split(':', 1)
                if service_name not in valid_services:
                    raise ValueError(f"Invalid upload service '{service_name}'. Valid services are 'dropbox', 'tempsh', 'bashupload', and 'all'.")
            elif service not in valid_services:
                raise ValueError(f"Invalid upload service '{service}'. Valid services are 'dropbox', 'tempsh', 'bashupload', and 'all'.")

    # Check for conflicting arguments
    conflicting_args = [
        (args.default, [args.keywords, args.years, args.databases, args.data_sources, args.limit, args.output_formats], "--default"),
        (args.clean, [args.keywords, args.years, args.databases, args.data_sources, args.limit, args.output_formats, args.default], "--clean"),
        (args.requirements, [args.keywords, args.years, args.databases, args.data_sources, args.limit, args.output_formats, args.default, args.clean], "--requirements")
    ]

    for flag, dependencies, flag_name in conflicting_args:
        if flag and any(dependencies):
            raise ValueError(f"The {flag_name} argument cannot be used with other specified arguments.")

    return True

# Function to get additional data sources from command-line arguments
def get_additional_data_sources(args):
    """
    Retrieve additional data sources from command-line arguments.

    Args:
        args (argparse.Namespace): Command-line arguments.

    Returns:
        list: A list of additional data source URLs or file paths.
    """
    additional_sources = []  # Initialize an empty list for additional sources
    if args.data_sources:
        # Split the comma-separated data sources and strip any surrounding whitespace
        additional_sources = [source.strip() for source in args.data_sources.split(',')]
    return additional_sources  # Return the list of additional data sources

# Generate a requirements.txt file with all required Python packages
def generate_requirements_file():
    """
    Generate a requirements.txt file with all required Python packages.

    This function creates a requirements.txt file in the current directory containing all the required Python packages for the script to run.
    """
    # List of required Python packages
    requirements = [
        "requests",
        "beautifulsoup4",
        "bibtexparser",
        "jinja2",
        "scholarly",
        "aiohttp",
        "argparse",
        "psutil",
        "reportlab"
    ]
    # Open the file in write mode and write the list of requirements to it
    with open('requirements.txt', 'w', encoding='utf-8') as reqfile:
        reqfile.write('\n'.join(requirements))
    # Print a message indicating the file has been created
    print("requirements.txt file has been created.")

# Prompt the user for input with a specified timeout.
# If no input is received or an EOFError occurs, exit.
def get_user_input(prompt, default, timeout=10):
    """
    Prompt the user for input with a specified timeout.
    If no input is received within the timeout, the program exits with a message.

    Args:
        prompt (str): The message displayed to the user.
        default (str): The default value returned if no input is received.
        timeout (int): The time in seconds to wait for user input before exiting.

    Returns:
        str: The user input if provided, otherwise the default value.
    """
    def on_timeout():
        """
        Handle the timeout event by printing a message and exiting the program.
        """
        print(f"\nNo input received. Exiting the program.")
        os._exit(1)  # Exit the program immediately

    # Create a timer that triggers on_timeout after the specified timeout
    timer = threading.Timer(timeout, on_timeout)
    timer.start()  # Start the timer

    try:
        user_input = input(prompt).strip()  # Prompt for input and strip whitespace
    except EOFError:
        user_input = ''  # Set input to empty string if input stream is closed
    finally:
        timer.cancel()  # Cancel the timer to prevent on_timeout from being called

    return user_input if user_input else default  # Return user input or default value

# Print keywords in columns for better readability
def print_keywords_in_columns(keywords, columns):
    """
    Print the keywords in a specified number of columns for better readability.

    Args:
        keywords (list): List of keywords to be printed.
        columns (int): Number of columns to print the keywords in.
    """
    # Calculate the number of rows needed given the number of columns
    rows = (len(keywords) + columns - 1) // columns

    # Iterate over each row
    for row in range(rows):
        # Iterate over each column in the current row
        for col in range(columns):
            # Calculate the index of the keyword in the flattened list
            index = row + col * rows
            # Check if the index is within the list size
            if index < len(keywords):
                # Print the keyword with formatting
                print(f"{index + 1}. {keywords[index]:<30}", end=' ')
        # Print a newline after each row
        print()
        
# Function to use default settings for keywords, years, databases, and limit
def use_default_settings():
    """
    Use default settings for fetching articles.

    Returns:
        tuple: A tuple containing default values for keywords, selected keywords,
               years, databases, additional sources, limit, and output format.
    """
    # Default to all available keywords
    all_keywords = default_keywords
    
    # Select all default keywords
    selected_keywords = default_keywords
    
    # Default number of years back to search for articles
    years = 1
    
    # Default databases to search within
    databases = ['arXiv', 'DBLP', 'Semantic Scholar', 'Google Scholar', 'zbMATH']
    
    # No additional data sources by default
    additional_sources = []
    
    # Default limit on the number of articles to fetch per keyword
    limit = 20
    
    # Default output format for saving articles
    output_format = ['bib']
    
    # Print the default settings being used
    print("Using default settings:")
    print(f"Keywords:")
    print_keywords_in_columns(default_keywords, 2)
    print(f"Number of Years Back to Search for Articles: {years}")
    print(f"Databases: {', '.join(databases)}")
    print(f"Limit on Number of Articles to Fetch: {limit}")
    print(f"Additional Data Sources: {', '.join(additional_sources) if additional_sources else 'None'}")
    print(f"Output Format: {', '.join(output_format)}")
    
    # Return the default settings as a tuple
    return all_keywords, selected_keywords, years, databases, additional_sources, limit, output_format

# Function to get user settings for keywords, years, databases, and limit
def get_user_settings(args):
    """
    Get user settings for fetching articles.

    Args:
        args (argparse.Namespace): Command-line arguments.

    Returns:
        tuple: A tuple containing the user settings for keywords, selected keywords,
               years, databases, additional sources, limit, and output format.
    """
    all_keywords = default_keywords.copy()
    
    # Print default list of keywords
    print("\nDefault list of keywords:")
    print_keywords_in_columns(all_keywords, 2)

    # Check if keywords are provided via command-line arguments
    if args.keywords:
        specified_keywords = [kw.strip() for kw in args.keywords.split(',')]
        all_keywords.extend(specified_keywords)
        all_keywords = list(set(all_keywords))
    else:
        # Prompt user to specify new keywords
        user_keywords = get_user_input("\nDo you want to specify any new keywords? (comma-separated, enter '00' to quit, press Enter to skip): ", "", timeout=10)
        if user_keywords == '00':
            print("\nNo new keywords specified. Exiting the program.")
            sys.exit(0)
        if user_keywords:
            new_keywords = [kw.strip() for kw in user_keywords.split(',')]
            all_keywords.extend(new_keywords)
            all_keywords = list(set(all_keywords))
        else:
            print("\nNo new keywords specified. Using the default list of keywords.")

    # Print updated list of keywords if any new keywords are added
    if args.keywords or user_keywords:
        print("\nUpdated list of keywords:")
        print_keywords_in_columns(all_keywords, 2)

    # Select keywords based on user input or use specified keywords
    if args.keywords:
        selected_keywords = specified_keywords
    else:
        while True:
            selected_indices = get_user_input("\nEnter the numbers corresponding to the keywords you want to use (comma-separated, default is all, enter '0' to quit, press Enter to skip): ", ','.join(map(str, range(1, len(all_keywords) + 1))), timeout=10).split(',')
            if '0' in selected_indices:
                print("\nNo keywords selected. Exiting the program.")
                sys.exit(0)
            try:
                selected_indices = list(set(int(i.strip()) for i in selected_indices))
                if all(1 <= i <= len(all_keywords) for i in selected_indices):
                    selected_keywords = [all_keywords[i - 1] for i in selected_indices]
                    break
                else:
                    print("Invalid input. Please enter valid keyword numbers.")
            except ValueError:
                print("Invalid input. Please enter valid keyword numbers.")

    # Get databases from command-line arguments or prompt user to choose
    if args.databases:
        database_map = {
            'arxiv': 1,
            'dblp': 2,
            'semantic scholar': 3,
            'google scholar': 4,
            'zbmath': 5
        }
        database_indices = list(set(database_map[db.strip().lower()] if db.strip().lower() in database_map else int(db.strip()) for db in args.databases.split(',')))
    else:
        while True:
            database_input = get_user_input("\nEnter the numbers corresponding to the databases you want to use (comma-separated, 1: arXiv, 2: DBLP, 3: Semantic Scholar, 4: Google Scholar, 5: zbMATH, 0: Quit, default is all): ", "1,2,3,4,5", timeout=10)
            if '0' in database_input.split(','):
                print("\nNo databases selected. Exiting the program.")
                sys.exit(0)
            try:
                database_indices = list(set(int(db.strip()) for db in database_input.split(',')))
                if all(1 <= db <= 5 for db in database_indices):
                    break
                else:
                    print("Invalid input. Please enter valid database numbers (1-5).")
            except ValueError:
                print("Invalid input. Please enter valid database numbers (1-5).")

    database_map = {1: 'arXiv', 2: 'DBLP', 3: 'Semantic Scholar', 4: 'Google Scholar', 5: 'zbMATH'}
    databases = [database_map[i] for i in database_indices if i in database_map]

    # Get number of years to search for articles from command-line arguments or prompt user to specify
    if args.years is None:
        while True:
            years_input = get_user_input(
                "\nNo number of years specified. Do you want to specify the number of years back to search for articles? "
                "(default is 1, enter '00' to quit, press Enter to skip): ", 
                "1", 
                timeout=10
            )
            if years_input == '00':
                print("\nNo number of years specified. Exiting the program.")
                sys.exit(0)
            try:
                years = int(years_input)
                if years >= 0:
                    break
                else:
                    print("The number of years must be a non-negative integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid non-negative integer.")
    else:
        years = args.years
    
    additional_sources = get_additional_data_sources(args)
    if not args.data_sources:
        # Print current data sources
        print("\nCurrent data sources:")
        if data_sources:
            for source in data_sources:
                print(f"- {source}")
        else:
            print("- None")

        # Prompt user to specify new data sources
        user_data_sources = get_user_input("\nDo you want to specify any new data sources? (comma-separated URLs or file paths, enter '00' to quit, press Enter to skip): ", "", timeout=10)
        if user_data_sources == '00':
            print("\nNo new data sources specified. Exiting the program.")
            sys.exit(0)
        if user_data_sources:
            for source in user_data_sources.split(','):
                source = source.strip()
                if source.startswith('http') or os.path.exists(source):
                    additional_sources.append(source)
                else:
                    print(f"Specified source does not exist: {source}")

    # Get limit on the number of articles to fetch from command-line arguments or prompt user to specify
    if args.limit is None:
        while True:
            limit_input = get_user_input("\nNo limit specified. Do you want to specify the limit on the number of articles to fetch? (default is 20, enter '00' to quit, press Enter to skip): ", "20", timeout=10)
            if limit_input == '00':
                print("\nNo limit specified. Exiting the program.")
                sys.exit(0)
            try:
                limit = int(limit_input)
                if limit > 0:
                    break
                else:
                    print("The limit must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid positive integer.")
        limit = int(limit_input)
    else:
        limit = args.limit

    # Get output format from command-line arguments or prompt user to specify
    if args.output_formats is None:
        while True:
            output_format_input = get_user_input("\nNo output format specified. Do you want to specify the output format? (bib/html/pdf/all, default is bib, press Enter to skip): ", "bib", timeout=10)
            output_format = [fmt.strip() for fmt in output_format_input.split(',') if fmt.strip() in ['bib', 'html', 'pdf', 'all']]
            if output_format:
                break
            else:
                print("Invalid output format specified. Valid options are 'bib', 'html', 'pdf', 'all'. Please try again.")
    else:
        output_format = [fmt.strip() for fmt in args.output_formats.split(',') if fmt.strip() in ['bib', 'html', 'pdf', 'all']]

    # Print user settings
    print("\nUser Settings:")
    print(f"Selected Keywords: {', '.join(selected_keywords)}")
    print(f"Number of Years Back to Search for Articles: {years}")
    print(f"Databases: {', '.join(databases)}")
    print(f"Limit on Number of Articles to Fetch: {limit}")
    print(f"Additional Data Sources: {', '.join(additional_sources) if additional_sources else 'None'}")
    print(f"Output Format: {', '.join(output_format)}")

    return all_keywords, selected_keywords, years, databases, additional_sources, limit, output_format

# Function to prompt user to choose databases to search
def get_user_databases():
    """
    Prompt user to choose databases to search.

    Returns:
        list: List of databases chosen by the user.
    """
    # Print options for databases
    print("No databases specified. Please choose from the following options:")
    print("1. arXiv")
    print("2. DBLP")
    print("3. Semantic Scholar")
    print("4. Google Scholar")
    print("5. zbMATH")
    print("6. All of the above (default)")
    print("7. None (Quit)")

    # Get user input for databases
    choice = get_user_input("Enter your choices (comma-separated, e.g., 1,2,3): ", "6", timeout=10)

    # Handle quit option
    if choice == "7":
        print("No databases selected. Exiting the program.")
        sys.exit(0)

    # Handle default option
    elif choice == "6":
        return ['arXiv', 'DBLP', 'Semantic Scholar', 'Google Scholar', 'zbMATH']

    # Handle custom options
    else:
        choices = [int(c.strip()) for c in choice.split(',')]
        databases = []
        if 1 in choices:
            databases.append('arXiv')
        if 2 in choices:
            databases.append('DBLP')
        if 3 in choices:
            databases.append('Semantic Scholar')
        if 4 in choices:
            databases.append('Google Scholar')
        if 5 in choices:
            databases.append('zbMATH')
        return databases

# Function to fetch articles from all specified databases
async def fetch_all_articles(selected_keywords, existing_titles, years, databases, limit, verbose=False):
    """
    Fetch articles from all specified databases asynchronously.

    Args:
        selected_keywords (list): List of keywords to search for.
        existing_titles (set): Set of existing article titles to filter out.
        years (int): Number of years back to search for articles.
        databases (list): List of databases to search in.
        limit (int): Maximum number of articles to fetch per keyword.
        verbose (bool, optional): If True, print additional logs. Defaults to False.

    Returns:
        list: A combined list of articles fetched from all specified databases.
    """
    all_articles = []
    tasks = []

    # Append tasks for fetching articles from specified databases
    if 'arXiv' in databases:
        tasks.append(fetch_arxiv_articles(selected_keywords, existing_titles, years, limit, verbose))
    if 'DBLP' in databases:
        tasks.append(fetch_dblp_articles(selected_keywords, existing_titles, years, limit, verbose))
    if 'Semantic Scholar' in databases:
        tasks.append(fetch_semantic_scholar_articles(selected_keywords, existing_titles, years, limit, verbose))
    if 'Google Scholar' in databases:
        tasks.append(fetch_google_scholar_articles(selected_keywords, existing_titles, years, limit, verbose))
    if 'zbMATH' in databases:
        tasks.append(fetch_zbmath_articles(selected_keywords, existing_titles, years, limit, verbose))

    # Run all tasks concurrently and gather results
    results = await asyncio.gather(*tasks)

    # Combine all results into a single list
    for result in results:
        all_articles.extend(result)

    return all_articles

# Function to write articles to a BibTeX file
def write_bibtex(all_articles, timestamp, verbose=False):
    """Write the articles to a BibTeX file."""
    if verbose:
        print("Starting to write BibTeX file...")
    try:
        bibtex_data = articles_to_bibtex(all_articles)
        with open(f'articles_{timestamp}.bib', 'w', encoding='utf-8') as bibfile:
            bibfile.write(bibtex_data)
        if verbose:
            print("Finished writing BibTeX file.")
    except Exception as e:
        print(f"An error occurred while writing the BibTeX file: {e}")

# Function to write articles to an HTML file
def write_html(all_articles, timestamp, verbose=False):
    """Write the articles to an HTML file."""
    if verbose:
        print("Starting to write HTML file...")
    try:
        html_content = articles_to_html(all_articles)
        with open(f'articles_{timestamp}.html', 'w', encoding='utf-8') as htmlfile:
            htmlfile.write(html_content)
        if verbose:
            print("Finished writing HTML file.")
    except Exception as e:
        print(f"An error occurred while generating the HTML file: {e}")

# Function to write articles to a PDF file using ReportLab
def write_pdf(all_articles, timestamp, verbose=False):
    """Write the articles to a PDF file using ReportLab."""
    if verbose:
        print("Starting to write PDF file...")

    try:
        pdf_file = f'articles_{timestamp}.pdf'
        c = canvas.Canvas(pdf_file, pagesize=A4)
        width, height = A4

        # Set PDF metadata
        c.setTitle("Reconfiguration Articles")
        c.setAuthor("Article Crawler Script")
        c.setSubject("A collection of articles on reconfiguration problems")
        c.setKeywords("reconfiguration, articles, research, bibliography")

        # Set the font and title
        c.setFont('Times-Roman', 16)
        c.drawString(40, height - 40, "Reconfiguration Articles")
        c.setFont('Times-Roman', 12)

        y_position = height - 80
        line_height = 14

        def draw_wrapped_text(text, x, y, max_width):
            """Draw text with word wrapping."""
            lines = []
            words = text.split()
            while words:
                line = ''
                while words and c.stringWidth(line + words[0], 'Times-Roman', 12) < max_width:
                    line += words.pop(0) + ' '
                lines.append(line)
            for line in lines:
                c.drawString(x, y, line.strip())
                y -= line_height
            return y

        for article in all_articles:
            if y_position < 100:
                c.showPage()
                c.setFont('Times-Roman', 12)
                y_position = height - 40

            y_position = draw_wrapped_text(f"Title: {article['title']}", 40, y_position, width - 80)
            y_position -= line_height
            y_position = draw_wrapped_text(f"Author(s): {article['author']}", 40, y_position, width - 80)
            y_position -= line_height
            y_position = draw_wrapped_text(f"Journal: {article['journal']}", 40, y_position, width - 80)
            y_position -= line_height
            y_position = draw_wrapped_text(f"Year: {article['year']}", 40, y_position, width - 80)
            y_position -= line_height
            y_position = draw_wrapped_text(f"URL: {article['url']}", 40, y_position, width - 80)
            y_position -= line_height
            if 'doi' in article:
                y_position = draw_wrapped_text(f"DOI: {article['doi']}", 40, y_position, width - 80)
                y_position -= line_height
            y_position -= line_height

        c.save()

        if verbose:
            print("Finished writing PDF file.")
    except Exception as e:
        print(f"An error occurred while generating the PDF file: {e}")

# Function to save fetched articles to files based on specified output format
def save_articles_to_files(all_articles, output_format, verbose=False, timestamp=""):
    """
    Save fetched articles to files based on the specified output format.

    Args:
        all_articles (list): List of articles to be saved.
        output_format (list): The formats in which to save the articles (e.g., ['bib', 'html', 'pdf']).
        verbose (bool): If True, print additional logs.

    This function utilizes threading to write the articles in the specified formats concurrently.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Initialize threads for writing files
    threads = []
    if 'bib' in output_format or 'all' in output_format:
        bibtex_thread = threading.Thread(target=write_bibtex, args=(all_articles, timestamp, verbose))
        threads.append(bibtex_thread)
        bibtex_thread.start()

    if 'html' in output_format or 'all' in output_format:
        html_thread = threading.Thread(target=write_html, args=(all_articles, timestamp, verbose))
        threads.append(html_thread)
        html_thread.start()

    if 'pdf' in output_format or 'all' in output_format:
        pdf_thread = threading.Thread(target=write_pdf, args=(all_articles, timestamp, verbose))
        threads.append(pdf_thread)
        pdf_thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print completion message based on the output format
    if 'html' in output_format or 'all' in output_format:
        print(f"HTML file 'articles_{timestamp}.html' has been created.")
    if 'bib' in output_format or 'all' in output_format:
        print(f"BibTeX file 'articles_{timestamp}.bib' has been created.")
    if 'pdf' in output_format or 'all' in output_format:
        print(f"PDF file 'articles_{timestamp}.pdf' has been created.")
    if not any(fmt in output_format for fmt in ['bib', 'html', 'pdf', 'all']):
        print(f"Script finished. There was an error creating the files.")

# Function to upload generated files to Dropbox using rclone
def upload_to_dropbox(filenames, dropbox_directory, verbose=False):
    """
    Upload generated files to Dropbox using rclone.

    Args:
        filenames (list): List of filenames to be uploaded.
        dropbox_directory (str): The Dropbox directory to upload the files to.
        verbose (bool): If True, print additional logs.
    """
    try:
        # Check if rclone is installed
        rclone_installed = os.system('rclone --version >nul 2>&1') == 0
        if not rclone_installed:
            print("rclone is not installed. Please install rclone and set it up with Dropbox.")
            return

        # Upload each file to Dropbox using rclone
        for filename in filenames:
            if os.path.exists(filename):
                if verbose:
                    print(f"Uploading {filename} to Dropbox directory {dropbox_directory}...")
                # Check if the Dropbox directory exists, create it if it doesn't
                os.system(f'rclone mkdir dropbox:/{dropbox_directory} >nul 2>&1')
                upload_result = os.system(f'rclone copy {filename} dropbox:/{dropbox_directory}/ >nul 2>&1')
                if upload_result != 0:
                    print(f"Failed to upload {filename} to Dropbox. Please ensure Dropbox is set up correctly with rclone.")
                else:
                    print(f"Successfully uploaded {filename} to Dropbox directory {dropbox_directory}.")
            else:
                if verbose:
                    print(f"File {filename} does not exist and will not be uploaded.")

    except Exception as e:
        print(f"An error occurred while uploading files to Dropbox: {e}")

# Function to upload generated files to temp.sh
def upload_to_tempsh(filenames, verbose=False):
    """
    Upload generated files to temp.sh.

    Args:
        filenames (list): List of filenames to be uploaded.
        verbose (bool): If True, print additional logs.
    """
    try:
        # Upload each file to temp.sh
        for filename in filenames:
            if os.path.exists(filename):
                if verbose:
                    print(f"Uploading {filename} to temp.sh...")
                with open(filename, 'rb') as file:
                    response = requests.post('https://temp.sh/upload', files={'file': file})
                    if response.status_code == 200:
                        download_link = response.text.strip()
                        print(f"Successfully uploaded {filename} to temp.sh. Download link: {download_link}")
                    else:
                        print(f"Failed to upload {filename} to temp.sh. Status code: {response.status_code}")
            else:
                if verbose:
                    print(f"File {filename} does not exist and will not be uploaded.")
    except Exception as e:
        print(f"An error occurred while uploading files to temp.sh: {e}")

# Function to upload generated files to bashupload.com
def upload_to_bashupload(filenames, verbose=False):
    """
    Upload generated files to bashupload.com.

    Args:
        filenames (list): List of filenames to be uploaded.
        verbose (bool): If True, print additional logs.
    """
    try:
        # Upload each file to bashupload.com
        for filename in filenames:
            if os.path.exists(filename):
                if verbose:
                    print(f"Uploading {filename} to bashupload.com...")
                with open(filename, 'rb') as file:
                    response = requests.post('https://bashupload.com', files={'file': file})
                    if response.status_code == 200:
                        download_link = response.text.strip()
                        print(f"Successfully uploaded {filename} to bashupload.com. Download link: {download_link}")
                    else:
                        print(f"Failed to upload {filename} to bashupload.com. Status code: {response.status_code}")
            else:
                if verbose:
                    print(f"File {filename} does not exist and will not be uploaded.")
    except Exception as e:
        print(f"An error occurred while uploading files to bashupload.com: {e}")

# Save the fetched articles to files and upload them to the specified service
def upload_articles(filenames, upload_service, upload_destination, verbose=False):
    """
    Save fetched articles to files and upload them to the specified service.

    Args:
        filenames (list): List of filenames to be uploaded.
        upload_service (str): The service to upload the files to ('dropbox', 'tempsh', 'bashupload', or 'all').
        upload_destination (str): The destination directory or service-specific identifier for the upload.
        verbose (bool): If True, print additional logs.
    """
    # Upload files to the specified service
    if upload_service == 'dropbox':
        upload_to_dropbox(filenames, upload_destination, verbose)
    elif upload_service == 'tempsh':
        upload_to_tempsh(filenames, verbose)
    elif upload_service == 'bashupload':
        upload_to_bashupload(filenames, verbose)
    elif upload_service == 'all':
        upload_to_dropbox(filenames, upload_destination, verbose)
        upload_to_tempsh(filenames, verbose)
        upload_to_bashupload(filenames, verbose)
    else:
        print(f"Unknown upload service: {upload_service}. Supported services are 'dropbox', 'tempsh', 'bashupload', and 'all'.")

# Function to print environment and resource usage information
def print_environment_info(start_time, verbose=False):
    """
    Print environment and resource usage information.

    Args:
        start_time (float): The start time of the script.
        verbose (bool): If True, print detailed environment and resource usage information.

    This function prints the elapsed time of the script. If verbose is True, it also prints
    detailed resource usage information such as CPU time, memory usage, number of threads,
    disk usage, network I/O, operating system details, and Python version.
    """
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if verbose:
        # Gather process and system information
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        cpu_usage = psutil.cpu_percent(interval=1)
        python_version = sys.version
        num_threads = process.num_threads()
        disk_usage = psutil.disk_usage('/')
        net_io = psutil.net_io_counters()

        # Get CPU times
        user_time, system_time, children_user_time, children_system_time = os.times()[:4]

        # Print detailed environment and resource usage information
        print("\nEnvironment and Resource Usage Information:")
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")
        print(f"User CPU Time: {user_time:.2f} seconds")
        print(f"System CPU Time: {system_time:.2f} seconds")
        print(f"Children User CPU Time: {children_user_time:.2f} seconds")
        print(f"Children System CPU Time: {children_system_time:.2f} seconds")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB")
        print(f"Number of Threads: {num_threads}")
        print(f"Disk Usage: {disk_usage.percent}% used")
        print(f"Network I/O: Sent = {net_io.bytes_sent / (1024 * 1024):.2f} MB, Received = {net_io.bytes_recv / (1024 * 1024):.2f} MB")
        
        # Print OS-specific information
        if os.name == 'posix':
            os_info = os.uname()
            print(f"Operating System: {os_info.sysname} {os_info.release} {os_info.version}")
        elif os.name == 'nt':
            print(f"Operating System: Windows {os.sys.getwindowsversion().major}.{os.sys.getwindowsversion().minor}")
        
        print(f"Python Version: {python_version}")
    else:
        # Print only the total elapsed time of the script
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")

# Function to clean up generated files
def clean_generated_files():
    """
    Remove all files generated by this script.
    """
    files_to_remove = [file for file in os.listdir('.') if file.startswith('articles_') and (file.endswith('.bib') or file.endswith('.html') or file.endswith('.pdf')) or file in ['template.html', 'requirements.txt', 'debug_output.txt']]
    for file in files_to_remove:
        try:
            os.remove(file)
            print(f"Removed file: {file}")
        except OSError as e:
            print(f"Error removing file {file}: {e}")

# Function to print a welcome message and briefly explain what the script does
def print_welcome_message():
    """
    Print a welcome message and briefly explain what the script does.
    """
    print("Welcome to the Article Crawler Script!")
    print("This script fetches articles from various databases based on user-selected keywords.")
    print("You can specify keywords, the number of years back to search, and the databases to search within.")
    print("The script will filter out existing articles fetched from known data sources and save the new articles in the specified format (BibTeX, HTML, PDF, or all).")
    print("You can also generate a requirements.txt file, clean up generated files, enable debug mode for detailed logs, and upload generated files to multiple services.")
    print("Supported upload services: Dropbox (using rclone), temp.sh, and bashupload.com.")
    print("Let's get started!\n")

def enable_debug_mode():
    """
    Enable debug mode to print all outputs and error messages to a txt file.
    """
    class Tee:
        def __init__(self, *files):
            self.files = files
        def write(self, obj):
            for f in self.files:
                f.write(obj)
        def flush(self):
            for f in self.files:
                f.flush()
    log_file = open('debug_output.txt', 'w')
    sys.stdout = Tee(sys.stdout, log_file)
    sys.stderr = Tee(sys.stderr, log_file)

def handle_print_default_keywords():
    """
    Print default keywords if the corresponding argument is provided.
    """
    print_keywords_in_columns(default_keywords, 2)

def handle_generate_requirements():
    """
    Generate a requirements file if the corresponding argument is provided.
    """
    generate_requirements_file()

def handle_clean_generated_files():
    """
    Clean up generated files if the corresponding argument is provided.
    """
    clean_generated_files()

def handle_upload_files(upload_arg, filenames, verbose):
    """
    Upload files to the specified service if specified.

    Args:
        upload_arg (str): The upload argument specifying the services and destinations.
        filenames (list): List of filenames to be uploaded.
        verbose (bool): If True, print additional logs.
    """
    upload_services = upload_arg.split(',')
    for service in upload_services:
        if ':' in service:
            upload_service, upload_destination = service.split(':', 1)
        else:
            upload_service = service
            upload_destination = ''
        try:
            upload_articles(filenames, upload_service, upload_destination, verbose)
        except Exception as e:
            print(f"An error occurred while uploading to {upload_service}: {e}")
            continue
    
# Main function to execute the script
def main():
    """
    Main function to handle the process of fetching and saving articles based on user-defined or default settings.
    This function performs the following steps:
    1. Parses command-line arguments.
    2. Handles each argument separately.
    """
    start_time = time.time()
    
    # Print welcome message and briefly explain what the script does
    print_welcome_message()
    
    # Parse command-line arguments
    args = parse_arguments()
    
    # Validate the parsed arguments
    try:
        validate_arguments(args)
    except ValueError as e:
        print(f"Argument validation error: {e}")
        sys.exit(1)
        
    # Enable debug mode if specified
    if args.debug:
        enable_debug_mode()

    # Handle the argument to print default keywords
    if args.print_default_keywords:
        handle_print_default_keywords()
        return

    # Handle the argument to generate a requirements file
    if args.requirements:
        handle_generate_requirements()
        return

    # Handle the argument to clean up generated files
    if args.clean:
        handle_clean_generated_files()
        return

    # Use default settings if specified, otherwise get user settings
    if args.default:
        all_keywords, selected_keywords, years, databases, additional_sources, limit, output_format = use_default_settings()
    else:
        all_keywords, selected_keywords, years, databases, additional_sources, limit, output_format = get_user_settings(args)

    # Combine default and additional data sources
    all_data_sources = data_sources + additional_sources
    
    # Fetch existing titles from the data sources
    existing_titles = fetch_existing_titles(all_data_sources)
    
    # Fetch articles from all specified databases asynchronously
    all_articles = asyncio.run(fetch_all_articles(selected_keywords, existing_titles, years, databases, limit, args.verbose))

    # Print the total number of articles found
    print(f"Total number of articles found: {len(all_articles)}")

    # Generate a timestamp for file naming
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Save the fetched articles to files in the specified formats
    save_articles_to_files(all_articles, output_format, args.verbose, timestamp)

    # Handle the argument to upload generated files
    if args.upload:
        filenames = [f'articles_{timestamp}.bib', f'articles_{timestamp}.html', f'articles_{timestamp}.pdf']
        existing_files = [filename for filename in filenames if os.path.exists(filename)]
        if existing_files:
            handle_upload_files(args.upload, existing_files, args.verbose)
        else:
            print("No files were generated to upload.")

    # Print environment and resource usage information
    print_environment_info(start_time, args.verbose)

if __name__ == "__main__":

    def handler(signum, frame):
        print("Script execution time exceeded the limit. Exiting...")
        # Cancel all running tasks and close the event loop
        loop = asyncio.get_event_loop()
        for task in asyncio.all_tasks(loop):
            task.cancel()
        loop.stop()
        sys.exit(1)

    # Set the timeout limit (in seconds)
    timeout_limit = 3600  # 1 hour

    # Set the signal handler for SIGALRM
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_limit)

    try:
        main()
    finally:
        # Disable the alarm
        signal.alarm(0)
