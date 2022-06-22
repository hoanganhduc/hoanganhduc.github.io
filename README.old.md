# About

This is the source of my [personal webpage](https://hoanganhduc.github.io) powered by [Jekyll](http://jekyllrb.com).

Below, I record how to set up and use Jekyll ([version 3.3.0](https://jekyllrb.com/news/2016/10/06/jekyll-3-3-is-here/)) in [Windows](#how-i-set-up-jekyll-in-windows) and [Linux](#how-i-set-up-jekyll-in-linux).

# How I set up Jekyll in Windows

In this section, I describe how I set up and use Jekyll in Windows.

* [Chocolatey](#chocolatey)
* [Install Ruby and Jekyll](#install-ruby-and-jekyll)
  * [If you get an error about SSL, here is how to fix it](#if-you-get-an-error-about-ssl-here-is-how-to-fix-it)
  * [If you get an error when installing unicode](#if-you-get-an-error-when-installing-unicode)
* [Install Ruby with Cygwin](#install-ruby-with-cygwin)
* [SSH for Windows](#ssh-for-windows)
  * [Installation](#installation)
  * [Generate new SSH key and add to GitHub](#generate-new-ssh-key-and-add-to-github)
  * [Adding your SSH key to the ssh-agent](#adding-your-ssh-key-to-the-ssh-agent)
  * [Test your SSH connection to GitHub](#test-your-ssh-connection-to-github)
* [Using PGP](#using-pgp)
* [Git for Windows](#git-for-windows)
  * [Installation](#installation-1)
  * [Global Setup](#global-setup)
  * [Setup my repo](#setup-my-repo)
* [References](#references)

## Chocolatey

Run the following command in Windows command prompt under administrator.

```
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```
Close the command prompt.

## Install Ruby and Jekyll

Run the following commands in Windows command prompt under administrator.

```
choco install ruby -y
```

Since I've already got my own `Gemfile` and `Gemfile.lock` files, I install Jekyll and all other dependencies using `bundler`.

```
gem install bundler
# Move to the folder that contains `Gemfile` and `Gemfile.lock`
bundle install
```

The content of my file `Gemfile`

```
source 'https://rubygems.org'

gem 'jekyll'
gem 'rouge'
gem 'kramdown'
gem 'rake'
gem 'jekyll-scholar'
gem 'pygments.rb'
gem 'jekyll-sitemap'
gem 'jekyll-feed'
gem 'jekyll-email-protect'
```

The content of my file `Gemfile.lock`

```
GEM
  remote: https://rubygems.org/
  specs:
    addressable (2.5.1)
      public_suffix (~> 2.0, >= 2.0.2)
    bibtex-ruby (4.4.3)
      latex-decode (~> 0.0)
    citeproc (1.0.5)
      namae (~> 0.8)
    citeproc-ruby (1.1.6)
      citeproc (>= 1.0.4, < 2.0)
      csl (~> 1.4)
    colorator (1.1.0)
    csl (1.4.5)
      namae (~> 0.7)
    csl-styles (1.0.1.7)
      csl (~> 1.0)
    ffi (1.9.18)
    ffi (1.9.18-x64-mingw32)
    ffi (1.9.18-x86-mingw32)
    forwardable-extended (2.6.0)
    jekyll (3.4.3)
      addressable (~> 2.4)
      colorator (~> 1.0)
      jekyll-sass-converter (~> 1.0)
      jekyll-watch (~> 1.1)
      kramdown (~> 1.3)
      liquid (~> 3.0)
      mercenary (~> 0.3.3)
      pathutil (~> 0.9)
      rouge (~> 1.7)
      safe_yaml (~> 1.0)
    jekyll-email-protect (1.0.3)
    jekyll-feed (0.9.2)
      jekyll (~> 3.3)
    jekyll-sass-converter (1.5.0)
      sass (~> 3.4)
    jekyll-scholar (5.9.1)
      bibtex-ruby (~> 4.0, >= 4.0.13)
      citeproc-ruby (~> 1.0)
      csl-styles (~> 1.0)
      jekyll (~> 3.0)
    jekyll-sitemap (1.1.1)
      jekyll (~> 3.3)
    jekyll-watch (1.5.0)
      listen (~> 3.0, < 3.1)
    kramdown (1.13.2)
    latex-decode (0.2.2)
      unicode (~> 0.4)
    liquid (3.0.6)
    listen (3.0.8)
      rb-fsevent (~> 0.9, >= 0.9.4)
      rb-inotify (~> 0.9, >= 0.9.7)
    mercenary (0.3.6)
    multi_json (1.12.1)
    namae (0.11.3)
    pathutil (0.14.0)
      forwardable-extended (~> 2.6)
    public_suffix (2.0.5)
    pygments.rb (1.1.2)
      multi_json (>= 1.0.0)
    rake (12.0.0)
    rb-fsevent (0.9.8)
    rb-inotify (0.9.8)
      ffi (>= 0.5.0)
    rouge (1.11.1)
    safe_yaml (1.0.4)
    sass (3.4.23)
    unicode (0.4.4.4)
    unicode (0.4.4.4-x86-mingw32)

PLATFORMS
  ruby
  x64-mingw32
  x86-mingw32

DEPENDENCIES
  jekyll
  jekyll-email-protect
  jekyll-feed
  jekyll-scholar
  jekyll-sitemap
  kramdown
  pygments.rb
  rake
  rouge

BUNDLED WITH
   1.14.6

```

### If you get an error about SSL, here is how to fix it

Download [rubygems-update-2.6.7.gem](https://rubygems.org/downloads/rubygems-update-2.6.7.gem) to the folder `C:\Users\<your-user-name>\Downloads` (indeed you can save it to any folder you like). Then, open a command prompt as administrator and move to the folder using the `cd` command, and run the following

```
gem install --local rubygems-update-2.6.7.gem
update_rubygems --no-ri --no-rdoc
```

After this, run `gem --version` to see the new update version.
Then, uninstall `rubygems-update` gem using the command

```
gem uninstall rubygems-update -x
```

### If you get an error when installing `unicode` gem

I got the following error

```
ERROR:  Error installing jekyll:
        The 'unicode' native gem requires installed build tools.

Please update your PATH to include build tools or download the DevKit
from 'http://rubyinstaller.org/downloads' and follow the instructions
at 'http://github.com/oneclick/rubyinstaller/wiki/Development-Kit'
```

To fix this, first you need to check the installed Ruby (which version?) and your OS (32-bit or 64-bit?) to download the suitable [development kit](http://rubyinstaller.org/downloads/). Then, extract the file to some folder, in my case `C:\Users\<your-user-name>\DevKit`. Then, move to this folder in the command prompt under administrator, and run the followings.

```
ruby dk.rb init # For generating the config.yml file
ruby dk.rb install
```

In case you use **Windows 64-bit**, before running the commands, you need to edit the file `dk.rb` (say, using Notepad++) by changing the `REG_KEYS` array to

```
REG_KEYS = [
    'Software\RubyInstaller\MRI',
    'Software\RubyInstaller\Rubinius',
    'Software\Wow6432Node\RubyInstaller\MRI'
]
```

Then, just simply run `bundle install` again. 

## Install Ruby with Cygwin

* Download [Cygwin](https://www.cygwin.com/) and install [as usual](https://cygwin.com/install.html).
* Install [apt-cyg](https://github.com/transcode-open/apt-cyg).
* Install some necessary packages

```
apt-cyg install git gcc-core gcc-g++ make zlib-devel curl autoconf libiconv libiconv-devel rsync patch unzip openssh openssl-devel libxml2-devel libxslt-devel libffi-devel libgdbm-devel libreadline-devel
```

* Install [rbenv](https://github.com/rbenv/rbenv)

```
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile
~/.rbenv/bin/rbenv init
```

* Install [ruby-build](https://github.com/rbenv/ruby-build)

```
mkdir -p "$(rbenv root)"/plugins
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

* Install Ruby

```
rbenv install --list # lists all available versions of Ruby
rbenv install 2.3.0 # installs Ruby 2.3.0 to ~/.rbenv/versions
rbenv global 2.3.0
rbenv rehash
```

* Verify that everything is properly set up using [rbenv-doctor](https://github.com/rbenv/rbenv-installer/blob/master/bin/rbenv-doctor).

```
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash
```

## SSH for Windows

### Installation

Download and install [OpenSSH for Windows](http://www.mls-software.com/opensshd.html).

### Generate new SSH key and add to GitHub

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

When you're prompted to `Enter a file in which to save the key` press `Enter`. This accepts the default file location. In my case, it is `/home/.ssh/id_rsa` (which is indeed `C:\Users\<your-user-name>\.ssh\id_rsa`). 

Then, add the contents of the file `id_rsa.pub` (open with Notepad++) to GitHub.

### Adding your SSH key to the ssh-agent

Move to the folder `C:\Users\<your-user-name>\.ssh` in command prompt and run

```
ssh-agent /bin/sh
ssh-add id_rsa
```

### Test your SSH connection to GitHub

See [here](https://help.github.com/articles/testing-your-ssh-connection/).

```
ssh -T git@github.com
```

## Using PGP

Download [Gpg4win](https://www.gpg4win.org/get-gpg4win.html) and install. To generate and use your PGP key, see [this article](https://www.deepdotweb.com/2015/02/21/pgp-tutorial-for-windows-kleopatra-gpg4win/). 

## Git for Windows

### Installation

Download Git for Windows from [here](https://git-scm.com/download/win) and install it. 

### Global Setup

```
git config --global user.name "<your-name>"
git config --global user.email "your_email@example.com"
git config --global gpg.program "C:\Program Files (x86)\GnuPG\bin\gpg.
exe"
git config --global user.signingkey <your-gpg-key-id>
```

### Setup my repo

To set up the git repo for my personal page, I use the follwing commands:

```
mkdir C:\Users\<your-user-name>\hoanganhduc.github.io # create the directory for my repo
xcopy /E /Y /F _site\* C:\Users\<your-user-name>\hoanganhduc.github.io # Copy all Jekyll generated files to the folder
cd C:\Users\<your-user-name>\hoanganhduc.github.io # Move to the folder
git init
git remote add origin git@github.com:hoanganhduc/hoanganhduc.github.io.git
git add --all .
git commit -S -m "%date%-%time% - commit"
git push -f origin master
```

In case you've already have the GitHub repo and just want to update, use the command `git pull origin master` after `git remote add origin git@github.com:hoanganhduc/hoanganhduc.github.io.git`. If you get the error `gpg: signing failed: Inappropriate ioctl for device`, then use `export GPG_TTY=$(tty)` before `git commit -S -m "%date%-%time% - commit"`.

For conventional reason, I create a simple `BAT` file named `make.bat` to generate and upload the webpage.

```
jekyll build --config _config.yml && xcopy /E /Y /F _site\* C:\Users\<your-user-name>\hoanganhduc.github.io && cd C:\Users\<your-user-name>\hoanganhduc.github.io && git add --all . && git commit -S -m "%date%-%time% - commit" && git push -f origin master
```

## References

1. [Jekyll on Windows](https://jekyllrb.com/docs/windows/)
2. [Easily install Jekyll on Windows with 3 command prompt entries and Chocolatey](https://davidburela.wordpress.com/2015/11/28/easily-install-jekyll-on-windows-with-3-command-prompt-entries-and-chocolatey/)
3. [SSL Certificate Update - RubyGems Guides](http://guides.rubygems.org/ssl-certificate-update/)
4. [Development Kit - oneclick/rubyinstaller Wiki](https://github.com/oneclick/rubyinstaller/wiki/Development-Kit)
5. [Can't get Ruby DevKit configuration file autogenerated properly - Stack Overflow](http://stackoverflow.com/questions/16523607/cant-get-ruby-devkit-configuration-file-autogenerated-properly)
6. [How to SSH from Windows 10](http://www.simplehelp.net/2016/03/13/how-to-ssh-from-windows-10/)
7. [Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/)
8. [PGP Tutorial For Windows (Kleopatra – Gpg4Win)](https://www.deepdotweb.com/2015/02/21/pgp-tutorial-for-windows-kleopatra-gpg4win/)
9. [Customizing Git - Git Configuration](https://git-scm.com/book/tr/v2/Customizing-Git-Git-Configuration)
10. [Installing Ruby 2.3.0 on Cygwin x64](https://gist.github.com/aspyatkin/d2b28fc754e009bd4a48)

# How I set up Jekyll in Linux

In this section, I describe how I set up and use Jekyll in Linux.
All the commands are performed in **Ubuntu 14.04 LTS (32-bit)**.

* [Ruby Version Manager](#ruby-version-manager)
* [Install Ruby](#install-ruby)
* [Install nodejs](#install-nodejs)
* [Install Jekyll](#install-jekyll)
* [References](#references-1)

## Ruby Version Manager

First of all, install `curl`.

```
sudo apt-get install curl
```

Then install RVM

```
curl -sSL https://get.rvm.io | bash -s stable
```

You will get some output report like the followings. Here `anhduc` is my username and `ASUS-X44H` is my computer name.

```
anhduc@ASUS-X44H:~$ curl -sSL https://get.rvm.io | bash -s stable
Downloading https://github.com/wayneeseguin/rvm/archive/stable.tar.gz

Installing RVM to /home/anhduc/.rvm/
    Adding rvm PATH line to /home/anhduc/.profile /home/anhduc/.bashrc /home/anhduc/.zshrc.
    Adding rvm loading line to /home/anhduc/.bash_profile /home/anhduc/.zlogin.
Installation of RVM in /home/anhduc/.rvm/ is almost complete:

  * To start using RVM you need to run `source /home/anhduc/.rvm/scripts/rvm`
    in all your open shell windows, in rare cases you need to reopen all shell windows.

# anhduc,
#
#   Thank you for using RVM!
#   We sincerely hope that RVM helps to make your life easier and more enjoyable!!!
#
# ~Wayne, Michal & team.

In case of problems: http://rvm.io/help and https://twitter.com/rvm_io 
```

To run RVM, you neend to use the command `source /home/anhduc/.rvm/scripts/rvm`.

## Install Ruby

Install the latest Ruby version (see [this page](https://www.ruby-lang.org/en/downloads/)). At the time I wrote this guide, the latest version is `2.4.1`.

```
rvm requirements
rvm install 2.4.1
rvm use 2.4.1 --default
```

## Install nodejs

```
sudo apt-get install nodejs
```

## Install Jekyll

Since I've already got my own `Gemfile` and `Gemfile.lock` files, I install Jekyll and all other dependencies using `bundler`.

```
gem install bundler
# Move to the folder that contains `Gemfile` and `Gemfile.lock`
bundle install
```

The content of my file `Gemfile`

```
source 'https://rubygems.org'

gem 'jekyll'
gem 'rouge'
gem 'kramdown'
gem 'rake'
gem 'jekyll-scholar'
gem 'pygments.rb'
gem 'jekyll-sitemap'
gem 'jekyll-feed'
gem 'jekyll-email-protect'
```

The content of my file `Gemfile.lock`

```
GEM
  remote: https://rubygems.org/
  specs:
    addressable (2.5.1)
      public_suffix (~> 2.0, >= 2.0.2)
    bibtex-ruby (4.4.3)
      latex-decode (~> 0.0)
    citeproc (1.0.5)
      namae (~> 0.8)
    citeproc-ruby (1.1.6)
      citeproc (>= 1.0.4, < 2.0)
      csl (~> 1.4)
    colorator (1.1.0)
    csl (1.4.5)
      namae (~> 0.7)
    csl-styles (1.0.1.7)
      csl (~> 1.0)
    ffi (1.9.18)
    ffi (1.9.18-x64-mingw32)
    ffi (1.9.18-x86-mingw32)
    forwardable-extended (2.6.0)
    jekyll (3.4.3)
      addressable (~> 2.4)
      colorator (~> 1.0)
      jekyll-sass-converter (~> 1.0)
      jekyll-watch (~> 1.1)
      kramdown (~> 1.3)
      liquid (~> 3.0)
      mercenary (~> 0.3.3)
      pathutil (~> 0.9)
      rouge (~> 1.7)
      safe_yaml (~> 1.0)
    jekyll-email-protect (1.0.3)
    jekyll-feed (0.9.2)
      jekyll (~> 3.3)
    jekyll-sass-converter (1.5.0)
      sass (~> 3.4)
    jekyll-scholar (5.9.1)
      bibtex-ruby (~> 4.0, >= 4.0.13)
      citeproc-ruby (~> 1.0)
      csl-styles (~> 1.0)
      jekyll (~> 3.0)
    jekyll-sitemap (1.1.1)
      jekyll (~> 3.3)
    jekyll-watch (1.5.0)
      listen (~> 3.0, < 3.1)
    kramdown (1.13.2)
    latex-decode (0.2.2)
      unicode (~> 0.4)
    liquid (3.0.6)
    listen (3.0.8)
      rb-fsevent (~> 0.9, >= 0.9.4)
      rb-inotify (~> 0.9, >= 0.9.7)
    mercenary (0.3.6)
    multi_json (1.12.1)
    namae (0.11.3)
    pathutil (0.14.0)
      forwardable-extended (~> 2.6)
    public_suffix (2.0.5)
    pygments.rb (1.1.2)
      multi_json (>= 1.0.0)
    rake (12.0.0)
    rb-fsevent (0.9.8)
    rb-inotify (0.9.8)
      ffi (>= 0.5.0)
    rouge (1.11.1)
    safe_yaml (1.0.4)
    sass (3.4.23)
    unicode (0.4.4.4)
    unicode (0.4.4.4-x86-mingw32)

PLATFORMS
  ruby
  x64-mingw32
  x86-mingw32

DEPENDENCIES
  jekyll
  jekyll-email-protect
  jekyll-feed
  jekyll-scholar
  jekyll-sitemap
  kramdown
  pygments.rb
  rake
  rouge

BUNDLED WITH
   1.14.6

```

## References

1. [Install Jekyll on Ubuntu 14.04 LTS](http://sharadchhetri.com/2014/06/30/install-jekyll-on-ubuntu-14-04-lts/)