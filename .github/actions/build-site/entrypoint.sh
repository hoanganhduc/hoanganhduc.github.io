#!/bin/bash

# Original: https://bpaulino.com/entries/10-automating-your-work-with-github-actions
# Exit immediately if a pipeline returns a non-zero status.
set -e

echo "🚀 Starting deployment action"

# Here we are using the variables
# - GITHUB_ACTOR: It is already made available for us by Github. It is the username of whom triggered the action
# - GITHUB_TOKEN: That one was intentionally injected by us in our workflow file.
# Creating the repository URL in this way will allow us to `git push` without providing a password
# All thanks to the GITHUB_TOKEN that will grant us access to the repository
REMOTE_REPO="https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

# Setting timezone
export TZ="Asia/Tokyo"

# Restoring timestamps
# Original: https://superuser.com/a/513854
cat .timestamps |  perl -ne 'INIT{ $/ = "\0";} chomp; m!^([0-9]+)/([0-9]+)/([0-9]+)/(.*)!s or next; my ($ct, $mt, $at, $f) = ($1, $2, $3, $4); utime $at, $mt, $f;'

# Removing .git folder so that jekyll-last-modified-at uses mtime
rm -rf .git

# We need to clone the master brach which contains source files.
# Remember, our Docker container is practically pristine at this point
# git clone $REMOTE_REPO master
# cd master

# Importing PGP secret key
openssl aes-256-cbc -K ${ENCRYPTED_2DB5BEF319F4_KEY} -iv ${ENCRYPTED_2DB5BEF319F4_IV} -in PGP-key.asc.enc -out PGP-key.asc -d
gpg2 --import PGP-key.asc
srm -rvf PGP-key.asc

# Install all of our dependencies inside the container
# based on the git repository Gemfile
# echo "⚡️ Installing project dependencies..."
bundle config set --local path 'vendor/bundle'
bundle install

# Build the website using Jekyll
echo "🏋️ Building website..."
#export PATH=/usr/local/texlive/2021/bin/x86_64-linux:$PATH && cd _CV && make && cd ..
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml
find ./_site -type f -name "*.html" -exec sed -i 's, />,>,g' {} \;
sed -i 's,Duc A. Hoang,<u>Duc A. Hoang</u>,g' ./_site/publications/index.html
# echo -e "Generating HTML sitemap"
# cd _site && tree -H '.' --noreport --charset utf-8 -h -D -T "HTML Sitemap" -I "*.html" --timefmt "%b %d, %Y %H:%M" -t > sitemap.html && cd ..
echo "Jekyll build done"

# Jekyll generates files are stored in the _site directory
# Now lets clone the gh-pages branch and copy all files from _site
git clone --single-branch --branch gh-pages $REMOTE_REPO gh-pages
rsync -arv --delete ./_site/* gh-pages
cd gh-pages 
# Making sure correct file permissions
find ./ -type f -exec chmod 644 {} \; 
find ./ -type d -exec chmod 755 {} \; 
# Backing up file timestamps
find ./ -mount ! -path "./.git/*" ! -name ".timestamps" -print0 | perl -ne 'INIT{ $/ = "\0"; use File::stat;} chomp; my $s = stat($_); next unless $s; print $s->ctime . "/" . $s->mtime . "/" . $s->atime ."/$_\0"; ' > .timestamps

echo "☁️ Publishing website"

# Now we can perform a commit
git config user.name 'Duc A. Hoang'
git config user.email 'anhduc.hoang1990@gmail.com'
git config gpg.program gpg2
git config user.signingkey D4E51506
git add --all .
# That will create a nice commit message with something like: 
# Github Actions @ 2019-09-06 12:32:22 JST
git commit -S -m "Github Actions Built @ $(date +'%Y-%m-%d  %H:%M:%S %Z')"
echo "Build branch ready to go. Pushing to Github..."
# Force push this update to our gh-pages
git push -u origin gh-pages
# Now everything is ready.
# Lets just be a good citizen and clean-up after ourselves
rm -fr .git
# cd ../..
# rm -rf master
yes | gpg2 --batch --yes --delete-secret-keys FBEAAAD6C193858F7D9BCFD73D544026D4E51506
yes | gpg2 --batch --yes --delete-keys FBEAAAD6C193858F7D9BCFD73D544026D4E51506
echo "🎉 New version deployed 🎊"
