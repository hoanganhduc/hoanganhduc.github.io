---
layout: blog-post
title: "Some notes on using Windows Subsystem for Linux"
author: "Duc A. Hoang"
categories:
  - windows
comment: true
last_modified_at: 2024-11-15
description: This post describes some notes on using Windows Subsystem for Linux
keywords: file permission, wsl, import, export
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>
This post contains some notes on using Windows Subsystem for Linux.

* TOC
{:toc}
</div>

# File permissions in WSL

Here, we describe how to handle file permission in Windows Subsystem for Linux. 
It was originally from [here](https://www.turek.dev/post/fix-wsl-file-permissions/).

Windows Subsystem for Linux (WSL) usually mounts Windows drives under `/mnt`.
However, the Linux file permission seems to be awful.
To fix this issue, simply add to `/etc/wsl.conf` (if the file does not exist, simply create it):

```bash
[automount]
enabled = true
options = "metadata,umask=22,fmask=11"
```

In short, every files now have permission `0644` and every directories have permission `0755`.

Also, add the following to `~/.profile` to fix the permission of newly created files and directories.

```bash
if [[ "$(umask)" = "0000" ]]; then
	umask 0022
fi
```

# Export and import WSL Distros

* **Export:** Let say I want to export my `Arch` WSL Distro which I downloaded from [this page](https://github.com/yuk7/ArchWSL) and customized for my personal use (it was pretty much like [what I did in my real Arch system]({% link _posts/2018-05-26-some-notes-on-installing-and-using-arch-linux.md %})). The following command, executed in `cmd`, will compress the distro into a single file `%userprofile%\Desktop\ArchWSL.tar`. (The `%userprofile%` directory is `C:\Users\[your-username]`.)

  ```bash
  wsl --export Arch %userprofile%\Desktop\ArchWSL.tar
  ```
  
  Additionally, as the size of my `ArchWSL.tar` is too big (around 8GB), I decided to compress it with [7-Zip](https://www.7-zip.org/) using the following command
  
  ```bash
  "C:\Program Files\7-Zip\7z.exe" a -tzip %userprofile%\Desktop\ArchWSL.tar.zip -m0=LZMA -mx=9 %userprofile%\Desktop\ArchWSL.tar
  ```
  
  Basically, the above command will create an archive `ArchWSL.tar.zip` in the folder `%userprofile%\Desktop` with "ultra" compression (option `-mx=9`, the highest compression level used by `7-Zip`) using the [LZMA compression method](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm) (option `-m0=LZMA`), which is the default and general compression method of `7z` format. Use the `-sdel` option if you want to delete `%userprofile%\Desktop\ArchWSL.tar` after compression (Be careful!). If you want to protect the archive with a password, use the option `-p[your-password]` (there is no space between `-p` and your password) or simply just `-p` and you will later be asked to enter your password.

* **Import:** To import back the exported distro, in case we compressed `ArchWSL.tar` with `7-Zip` before, we first need to extract `ArchWSL.tar.zip`, say, to the `%userprofile%\Desktop` folder. 
  
  ```bash
  "C:\Program Files\7-Zip\7z.exe" x ArchWSL.tar.zip -o%userprofile%\Desktop
  ```
  
  If the archive is password-protected, the program will ask you to enter the password you used at the time it was created.
  Now, we can import back the distro by running in `cmd` the following command:
  
  ```bash
  wsl --import Arch %localappdata%\Packages\yuk7.archwsl_35zwpb4sx6e50\LocalState %userprofile%\Desktop\ArchWSL.tar
  ```
  
# Copy contents of a file to clipboard

```bash
clip.exe < file.txt # do not miss the .exe part
```
# SSH

I use `keychain` to avoid typing SSH passphrases multiple times. After installing `keychain` in my Arch WSL, I simply put the following to `.bashrc`

```bash
/usr/bin/keychain --nogui $HOME/.ssh/id_rsa
source $HOME/.keychain/$HOST-sh
```

In this way, I have to type in the passphrase for the first time I open a Arch WSL terminal. As long as the distribution is running (which can be veerified by typing `wsl -l --running` in a `cmd` windows), I don't have to type it again when using `ssh`.

Another way is to use [wsl-ssh-agent](https://github.com/rupor-github/wsl-ssh-agent). 
If you are using WSL1, the steps are simple.

* Download `wsl-ssh-agent.zip` from [this page](https://github.com/rupor-github/wsl-ssh-agent/releases) and extract it to the `%USERPROFILE%\wsl-ssh-agent` folder. The `%USERPROFILE%` corresponds to your Windows home folder `C:\Users\<your-username>\`, which is known in your WSL as `/mnt/c/Users/<your-username>/`.

* Enable Windows 10 `ssh-agent` service by running the following in `powershell` as admin:
  ```bash
  Start-Service ssh-agent
  Set-Service -StartupType Automatic ssh-agent
  ```

* Run `wsl-ssh-agent-gui.exe` in `cmd` using the command
  ```bash
  %USERPROFILE%\wsl-ssh-agent\wsl-ssh-agent-gui.exe -socket %USERPROFILE%\ssh-agent.sock
  ``` 
  
  I created a shortcut in `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` with the `Target` as in the above command, so that `wsl-ssh-agent-gui.exe` opens every time Windows starts.

* Add the following to your WSL1 system's `$HOME/.bashrc` file:
  ```bash
  export SSH_AUTH_SOCK=/mnt/c/Users/<your-username>/wsl-ssh-agent/ssh-agent.sock
  ```

If you are using WSL2, you need some workaround.

* You will need [npiperelay.exe](https://github.com/jstarks/npiperelay). 
  * Install `go` and `socat` in your WSL2 system. (In ArchLinux, use `yay -S go socat`. In Ubuntu, use `sudo apt-get install golang-go socat`.)
  * In your WSL terminal, run
    ```bash
	env GOOS=windows GOARCH=amd64 go get -d github.com/jstarks/npiperelay
	env GOOS=windows GOARCH=amd64 go build -o /mnt/c/Users/<your-username>/wsl-ssh-agent/npiperelay.exe github.com/jstarks/npiperelay
	```
* Put the following to your WSL2 system's `$HOME/.bashrc` (I copied almost everything from [this page](https://stuartleeks.com/posts/wsl-ssh-key-forward-to-windows/)).
  ```bash
  # Configure ssh forwarding
  export SSH_AUTH_SOCK=$HOME/.ssh/agent.sock
  # need `ps -ww` to get non-truncated command for matching
  # use square brackets to generate a regex match for the process we want but that doesn't match the grep command running it!
  ALREADY_RUNNING=$(ps -auxww | grep -q "[n]piperelay.exe -ei -s //./pipe/openssh-ssh-agent"; echo $?)
  if [[ $ALREADY_RUNNING != "0" ]]; then
      if [[ -S $SSH_AUTH_SOCK ]]; then
          # not expecting the socket to exist as the forwarding command isn't running (http://www.tldp.org/LDP/abs/html/fto.html)
          echo "removing previous socket..."
          rm $SSH_AUTH_SOCK
      fi
      echo "Starting SSH-Agent relay..."
      # setsid to force new session to keep running
      # set socat to listen on $SSH_AUTH_SOCK and forward to npiperelay which then forwards to openssh-ssh-agent on windows
      (setsid socat UNIX-LISTEN:$SSH_AUTH_SOCK,fork EXEC:"/mnt/c/Users/<your-username>/wsl-ssh-agent/npiperelay.exe -ei -s //./pipe/openssh-ssh-agent",nofork &) >/dev/null 2>&1
  fi
  ```

<!-- 

# Install SageMath 9.3 in Ubuntu WSL

## Enable WSL2

Follow [this official instruction](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Install Ubuntu (version 18.04 or newer) as a WSL

Follow [this official instruction](https://ubuntu.com/wsl).
After finishing installation, run the following in a `cmd` or `powershell` (if you run `wsl --set-default-version 2`, you don't need to do this):

```bash
wsl --set-version Ubuntu 2
```

Adjust file permissions in Ubuntu if necessary, following the [above instruction](#file-permissions-in-wsl).

## Installation

Follow [this instruction](https://doc.sagemath.org/html/en/installation/source.html).
I recorded the steps here.
Open a Ubuntu terminal and run:

```bash
sudo apt update
sudo apt upgrade
```

```bash
sudo apt-get install  bc binutils bzip2 ca-certificates cliquer curl eclib-tools fflas-ffpack flintqs g++ g++ gcc gcc gfan gfortran glpk-utils gmp-ecm lcalc libatomic-ops-dev libboost-dev libbraiding-dev libbrial-dev libbrial-groebner-dev libbz2-dev libcdd-dev libcdd-tools libcliquer-dev libcurl4-openssl-dev libec-dev libecm-dev libffi-dev libflint-arb-dev libflint-dev libfreetype6-dev libgc-dev libgd-dev libgf2x-dev libgiac-dev libgivaro-dev libglpk-dev libgmp-dev libgsl-dev libhomfly-dev libiml-dev liblfunction-dev liblrcalc-dev liblzma-dev libm4rie-dev libmpc-dev libmpfi-dev libmpfr-dev libncurses5-dev libntl-dev libopenblas-dev libpari-dev libpcre3-dev libplanarity-dev libppl-dev libpython3-dev libreadline-dev librw-dev libsqlite3-dev libssl-dev libsuitesparse-dev libsymmetrica2-dev libz-dev libzmq3-dev libzn-poly-dev m4 make nauty openssl palp pari-doc pari-elldata pari-galdata pari-galpol pari-gp2c pari-seadata patch perl pkg-config planarity ppl-dev python3 python3 python3-distutils r-base-dev r-cran-lattice sqlite3 sympow tachyon tar xcas xz-utils yasm
```

```bash
sudo apt-get install  cmake coinor-cbc coinor-libcbc-dev git graphviz libboost-dev libfile-slurp-perl libigraph-dev libisl-dev libjson-perl libmongodb-perl libnauty-dev libperl-dev libsvg-perl libterm-readkey-perl libterm-readline-gnu-perl libterm-readline-gnu-perl libxml-libxslt-perl libxml-writer-perl libxml2-dev libxml2-dev lrslib ninja-build pari-gp2c tox
```

```bash
wget http://www.mirrorservice.org/sites/www.sagemath.org/src/sage-9.3.tar.gz
echo "e826c848c6bb972a188d5ddd4dc48308 sage-9.3.tar.gz" | md5sum -c
tar -xvf sage-9.3.tar.gz -C $HOME
cd $HOME/sage-9.3
./configure
make
```

**Note:** 
* The compilation may take very long time (around 4 hours in my computer).
* Copy the compiled SageMath from one computer to another may not work, due to the difference in hardwares.

Some extra packages I installed with `sage`:

```bash
sage -i plantri sage_sws2rst rst2ipynb
```

## Open SageMath Jupyter notebook in Google Chrome

In Ubuntu Terminal. run:

```bash
cd $HOME/sage-9.3
sage jupyter notebook –generate-config
```

Edit `$HOME/.sage/jupyter-4.1/jupyter_notebook_config.py` by adding the following content to the end:

```
#——————————————————————————
# NotebookApp(JupyterApp) configuration
#——————————————————————————
c.NotebookApp.use_redirect_file = False
```

Finally, add the following to `$HOME/.bashrc`:

```bash
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
```

Note that `C:\Program Files\Google\Chrome\Application\chrome.exe` is the location of Google Chrome installed in my computer.

If you want to open the notebook in a specific folder, say `C:\Users\<your-username>\SageMath`, run the following command in Ubuntu Terminal:

```bash
sage -n jupyter --notebook-dir="/mnt/c/Users/<your-username>/SageMath"
```

## Create shortcuts in Windows desktop

* Download [sagemath.ico](https://raw.githubusercontent.com/sagemath/sage-windows/master/resources/sagemath.ico), and save it to some folder, say `C:\Users\<your-username>\Pictures\Icons`.
* Create desktop shorcuts:
  * For accessing *Jupyter notebook*: Use the "Target" as `C:\Windows\System32\wsl.exe --distribution Ubuntu --exec /bin/bash -c "$HOME/sage-9.3/sage --notebook jupyter"`, and name the shortcut as you like, for example, "SageMath 9.3 Notebook". You can also point the shortcut's icon to `C:\Users\<your-username>\Pictures\Icons\sagemath.ico`.
  You can also append `--notebook-dir="/mnt/c/Users/<your-username>/SageMath` to the "Target" command above to open the directory `C:\Users\<your-username>\SageMath` every time you start the notebook.
  * For accessing *SageMath subshell*: Use the "Target" as `C:\Windows\System32\wsl.exe --distribution Ubuntu --exec /bin/bash -c "$HOME/sage-9.3/sage -sh"`.
  * For accessing *SageMath console*: Use the "Target" as `C:\Windows\System32\wsl.exe --distribution Ubuntu --exec /bin/bash -c "$HOME/sage-9.3/sage"`.
* If you want to open SageMath with [Windows Terminal](https://github.com/microsoft/terminal), simply just put `wt.exe` at the beginning of the command. For example, to open SageMath console with Windows Terminal, use `wt.exe C:\Windows\System32\wsl.exe --distribution Ubuntu --exec /bin/bash -c "$HOME/sage-9.3/sage"`. If you use this command, the SageMath console will be opened at the folder `/mnt/c/Users/<your-username>`. To open it at a specific folder, say `C:\Users\<your-username>\SageMath`, add option `-d C:\Users\<your-username>\SageMath` right after `wt.exe`.
  
## Add/Remove Right Click/Shift + Right Click "Open SageMath Notebook here" context menu

Create a `Add_Open_SageMath_Notebook_here_context_menu.reg` file with the following contents (I modified the downloaded registry file from [this guide](https://www.tenforums.com/tutorials/110473-add-remove-open-linux-shell-here-context-menu-windows-10-a.html). Remeber to change the path to `sagemath.ico` appropriately):

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\SageMathWSL]
@="Open SageMath Jupyter Notebook here"
"Extended"=-
"Icon"="C:\\Users\\<your-username>\\Pictures\\Icons\\sagemath.ico"
"NoWorkingDirectory"=""
"ProgrammaticAccessOnly"=-

[HKEY_CLASSES_ROOT\Directory\Background\shell\SageMathWSL\command]
@="wsl.exe --cd \"%V\" --distribution Ubuntu --exec /bin/bash -c \"$HOME/sage-9.3/sage --notebook jupyter\""



[HKEY_CLASSES_ROOT\Directory\shell\SageMathWSL]
@="Open SageMath Jupyter Notebook here"
"Extended"=-
"Icon"="C:\\Users\\<your-username>\\Pictures\\Icons\\sagemath.ico"
"NoWorkingDirectory"=""
"ProgrammaticAccessOnly"=-

[HKEY_CLASSES_ROOT\Directory\shell\SageMathWSL\command]
@="wsl.exe --cd \"%V\" --distribution Ubuntu --exec /bin/bash -c \"$HOME/sage-9.3/sage --notebook jupyter\""



[HKEY_CLASSES_ROOT\Drive\shell\SageMathWSL]
@="Open SageMath Jupyter Notebook here"
"Extended"=-
"Icon"="C:\\Users\\<your-username>\\Pictures\\Icons\\sagemath.ico"
"NoWorkingDirectory"=""
"ProgrammaticAccessOnly"=-

[HKEY_CLASSES_ROOT\Drive\shell\SageMathWSL\command]
@="wsl.exe --cd \"%V\" --distribution Ubuntu --exec /bin/bash -c \"$HOME/sage-9.3/sage --notebook jupyter\""
```

To remove these items from the context menu, create a `Remove_Open_SageMath_Notebook_here_context_menu.reg` file with:

```
Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\Directory\Background\shell\SageMathWSL]

[-HKEY_CLASSES_ROOT\Directory\shell\SageMathWSL]

[-HKEY_CLASSES_ROOT\Drive\shell\SageMathWSL]
```

-->

# Install SageMath 10.4 in Ubuntu WSL

## Enable WSL2

Follow [this official instruction](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Install Ubuntu (version 24.04) as a WSL

Follow [this official instruction](https://ubuntu.com/wsl) or install from the Microsoft Store.
After finishing installation, run the following in a `cmd` or `powershell` (if you run `wsl --set-default-version 2`, you don't need to do this):

```bash
wsl --set-version Ubuntu-24.04 2
```

Adjust file permissions in Ubuntu if necessary, following the [above instruction](#file-permissions-in-wsl).
Additionally, create a new user in Ubuntu terminal by running the following command as `root`:

```bash 
adduser <username>
usermod -a G adm,dialout,cdrom,floppy,sudo,audio,dip,video,plugdev,netdev <username>
```

Run the command `ubuntu2404.exe config --default-user <username>` to set the default user for the Ubuntu WSL.

## Installation

Follow [this instruction](https://doc.sagemath.org/html/en/installation/source.html) and [this instruction](https://sagemanifolds.obspm.fr/install_ubuntu.html).
I recorded the steps here.
Open a Ubuntu terminal and run:

```bash
sudo apt update
sudo apt upgrade
```

```bash
sudo apt install autoconf automake gh git gpgconf libtool openssh-client pkg-config \
  automake bc binutils bzip2 ca-certificates cliquer cmake curl ecl \
  eclib-tools fflas-ffpack flintqs g++ gengetopt gfan gfortran git glpk-utils gmp-ecm lcalc \
  libatomic-ops-dev libboost-dev libbraiding-dev libbz2-dev libcdd-dev libcdd-tools \
  libcliquer-dev libcurl4-openssl-dev libec-dev libecm-dev libffi-dev libflint-dev \
  libfreetype-dev libgc-dev libgd-dev libgf2x-dev libgiac-dev libgivaro-dev libglpk-dev \
  libgmp-dev libgsl-dev libhomfly-dev libiml-dev liblfunction-dev liblrcalc-dev liblzma-dev \
  libm4rie-dev libmpc-dev libmpfi-dev libmpfr-dev libncurses-dev libntl-dev libopenblas-dev \
  libpari-dev libpcre3-dev libplanarity-dev libppl-dev libprimesieve-dev libpython3-dev \
  libqhull-dev libreadline-dev librw-dev libsingular4-dev libsqlite3-dev libssl-dev \
  libsuitesparse-dev libsymmetrica2-dev zlib1g-dev libzmq3-dev libzn-poly-dev m4 make nauty \
  openssl palp pari-doc pari-elldata pari-galdata pari-galpol pari-gp2c pari-seadata patch perl \
  pkg-config planarity ppl-dev python3-setuptools python3-venv r-base-dev r-cran-lattice singular \
  sqlite3 sympow tachyon tar tox xcas xz-utils \
  texlive-full latexmk pandoc dvipng     
```

```bash
wget https://github.com/sagemath/sage/releases/download/10.4/sage-10.4.tar.gz
echo "dcecdbdc2091798b6f85d1a5300f5f8f sage-10.4.tar.gz" | md5sum -c
tar -xvf sage-10.4.tar.gz -C $HOME
cd $HOME/sage-10.4
rm -rf configure
make configure
./configure
MAKE="make -j8" make
```

**Note:** 
* The option `-j8` is to launch the build in parallel on 8 threads. You can adapt it to your CPU (usually you may choose a number of threads that is twice the number of cores of your CPU). You can also add `SAGE_KEEP_BUILT_SPKGS=yes` at the beginning of the final command to keep the built packages in case the build fails and you want to restart it.
* The compilation may take very long time (around 4 hours in my computer).
* Copy the compiled SageMath from one computer to another may not work, due to the difference in hardwares.

Some extra packages I installed with `sage`:

```bash
sage -i plantri sage_sws2rst rst2ipynb notebook
```

## Aliases in `$HOME/.bashrc`

Add the following to `$HOME/.bashrc`:

```bash
alias sage="~/sage-10.4/sage"
alias sage-notebook="cd <your-sagemath-notebook-dir> && ~/sage-10.4/sage -n jupyter"
alias sage-clear="echo yes | ~/sage-10.4/sage -ipython history clear"
```

## Terminal Colors

See [this page](https://ask.sagemath.org/question/10060/sage-terminal-colors/) for more details.
First, run `sage -ipython profile create` to create the default profile.
Then, in Ubuntu terminal, run:

```bash
export IPYTHON_CONFIG=$(sage -ipython locate)
echo "c.TerminalInteractiveShell.colors = 'Linux'" >> $IPYTHON_CONFIG/profile_default/ipython_config.py
```

## Open SageMath Jupyter notebook in Google Chrome

In Ubuntu Terminal. run:

```bash
cd $HOME/sage-10.4
sage-notebook --generate-config
```

Edit `$HOME/.sage/jupyter-4.1/jupyter_notebook_config.py` by adding the following content to the end:

```
c.SeverApp.use_redirect_file = False
import webbrowser
webbrowser.register('chrome', None, webbrowser.GenericBrowser(u'/mnt/c/Program Files/Google/Chrome/Application/chrome.exe'))
c.ServerApp.browser = 'chrome'
```

On the other hand, you can also add the following to `$HOME/.bashrc`:

```bash
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
```

Note that `C:\Program Files\Google\Chrome\Application\chrome.exe` is the location of Google Chrome installed in my computer.

If you want to open the notebook in a specific folder, say `C:\Users\<your-username>\SageMath`, run the following command in Ubuntu Terminal:

```bash
sage -n jupyter --notebook-dir="/mnt/c/Users/<your-username>/SageMath"
```

## Create shortcuts in Windows desktop

* Download [sagemath.ico](https://raw.githubusercontent.com/sagemath/sage-windows/master/resources/sagemath.ico), and save it to some folder, say `C:\Users\<your-username>\Pictures\Icons`.
* Create desktop shorcuts:
  * For accessing *Jupyter notebook*: Use the "Target" as `C:\Windows\System32\wsl.exe --distribution Ubuntu-24.04 --exec /bin/bash -c "$HOME/sage-10.4/sage --notebook jupyter"`, and name the shortcut as you like, for example, "SageMath 9.3 Notebook". You can also point the shortcut's icon to `C:\Users\<your-username>\Pictures\Icons\sagemath.ico`.
  You can also append `--notebook-dir="/mnt/c/Users/<your-username>/SageMath` to the "Target" command above to open the directory `C:\Users\<your-username>\SageMath` every time you start the notebook.
  * For accessing *SageMath subshell*: Use the "Target" as `C:\Windows\System32\wsl.exe --distribution Ubuntu-24.04 --exec /bin/bash -c "$HOME/sage-10.4/sage -sh"`.
  * For accessing *SageMath console*: Use the "Target" as `C:\Windows\System32\wsl.exe --distribution Ubuntu-24.04 --exec /bin/bash -c "$HOME/sage-10.4/sage"`.
* If you want to open SageMath with [Windows Terminal](https://github.com/microsoft/terminal), simply just put `wt.exe` at the beginning of the command. For example, to open SageMath console with Windows Terminal, use `wt.exe C:\Windows\System32\wsl.exe --distribution Ubuntu --exec /bin/bash -c "$HOME/sage-10.4/sage"`. If you use this command, the SageMath console will be opened at the folder `/mnt/c/Users/<your-username>`. To open it at a specific folder, say `C:\Users\<your-username>\SageMath`, add option `-d C:\Users\<your-username>\SageMath` right after `wt.exe`.
  
## Add/Remove Right Click/Shift + Right Click "Open SageMath Notebook here" context menu

Create a `Add_Open_SageMath_Notebook_here_context_menu.reg` file with the following contents (I modified the downloaded registry file from [this guide](https://www.tenforums.com/tutorials/110473-add-remove-open-linux-shell-here-context-menu-windows-10-a.html). Remeber to change the path to `sagemath.ico` appropriately):

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\SageMathWSL]
@="Open SageMath Jupyter Notebook here"
"Extended"=-
"Icon"="C:\\Users\\<your-username>\\Pictures\\Icons\\sagemath.ico"
"NoWorkingDirectory"=""
"ProgrammaticAccessOnly"=-

[HKEY_CLASSES_ROOT\Directory\Background\shell\SageMathWSL\command]
@="wsl.exe --cd \"%V\" --distribution Ubuntu --exec /bin/bash -c \"$HOME/sage-10.4/sage --notebook jupyter\""



[HKEY_CLASSES_ROOT\Directory\shell\SageMathWSL]
@="Open SageMath Jupyter Notebook here"
"Extended"=-
"Icon"="C:\\Users\\<your-username>\\Pictures\\Icons\\sagemath.ico"
"NoWorkingDirectory"=""
"ProgrammaticAccessOnly"=-

[HKEY_CLASSES_ROOT\Directory\shell\SageMathWSL\command]
@="wsl.exe --cd \"%V\" --distribution Ubuntu --exec /bin/bash -c \"$HOME/sage-10.4/sage --notebook jupyter\""



[HKEY_CLASSES_ROOT\Drive\shell\SageMathWSL]
@="Open SageMath Jupyter Notebook here"
"Extended"=-
"Icon"="C:\\Users\\<your-username>\\Pictures\\Icons\\sagemath.ico"
"NoWorkingDirectory"=""
"ProgrammaticAccessOnly"=-

[HKEY_CLASSES_ROOT\Drive\shell\SageMathWSL\command]
@="wsl.exe --cd \"%V\" --distribution Ubuntu --exec /bin/bash -c \"$HOME/sage-10.4/sage --notebook jupyter\""
```

To remove these items from the context menu, create a `Remove_Open_SageMath_Notebook_here_context_menu.reg` file with:

```
Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\Directory\Background\shell\SageMathWSL]

[-HKEY_CLASSES_ROOT\Directory\shell\SageMathWSL]

[-HKEY_CLASSES_ROOT\Drive\shell\SageMathWSL]
```