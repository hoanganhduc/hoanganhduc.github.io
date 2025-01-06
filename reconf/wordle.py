import re
"""
This script generates a word cloud from the titles of entries in a BibTeX file.
Functions:
    extract_titles_from_bibtex(bibtex_file):
        Extracts titles from a given BibTeX file using regular expressions.
        Args:
            bibtex_file (str): Path to the BibTeX file.
        Returns:
            list: A list of titles extracted from the BibTeX file.
    generate_wordcloud(titles):
        Generates and displays a word cloud from a list of titles.
        Args:
            titles (list): A list of titles.
        Returns:
            WordCloud: The generated word cloud object.
    save_wordcloud(wordcloud, output_file):
        Saves the generated word cloud to a file.
        Args:
            wordcloud (WordCloud): The word cloud object to save.
            output_file (str): Path to the output image file.
        Returns:
            None
    print_usage():
        Prints usage instructions for the script.
        Args:
            None
        Returns:
            None
    main():
        Main function to handle command-line arguments and execute the script.
        Args:
            None
        Returns:
            None
Usage:
    Run the script from the command line with the path to a BibTeX file as the first argument.
    Optionally, provide a second argument to specify the output image file for the word cloud.
    Example: python wordle.py <path_to_bibtex_file> [<output_image_file>]
"""
from wordcloud import WordCloud
import sys
import matplotlib.pyplot as plt

# Function to extract titles from a BibTeX file
def extract_titles_from_bibtex(bibtex_file):
    with open(bibtex_file, 'r') as file:
        content = file.read()
    
    # Use regex to find all titles in the BibTeX file
    titles = re.findall(r'\stitle\s*=\s*{([^}]+)}', content, re.IGNORECASE)
    return titles

# Function to generate a word cloud from a list of titles
def generate_wordcloud(titles):
    text = ' '.join(titles)
    wordcloud = WordCloud(width=1400, height=700, background_color='white').generate(text)
    
    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return wordcloud

# Function to save the generated word cloud to a file
def save_wordcloud(wordcloud, output_file):
    wordcloud.to_file(output_file)
    print(f"Word cloud saved as {output_file}")

# Function to print usage instructions
def print_usage():
    print("Usage: python wordle.py <path_to_bibtex_file> [<output_image_file>]")

# Main function to handle command-line arguments and execute the script
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print_usage()
        sys.exit(1)
    
    bibtex_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else 'wordcloud.png'
    titles = extract_titles_from_bibtex(bibtex_file)
    wordcloud = generate_wordcloud(titles)
    save_wordcloud(wordcloud, output_file)

# Entry point of the script
if __name__ == "__main__":
    main()