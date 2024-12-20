---
layout: blog-post
title: "A Workflow with GitHub and Overleaf"
author: "Duc A. Hoang"
categories:
  - tex
  - linux
  - windows
<!--comment: true-->
last_modified_at: 2024-12-20
description: This post contains a workflow that I use to write LaTeX documents with Overleaf and GitHub.
keywords: LaTeX, Overleaf, GitHub, workflow, git, version control, collaboration, Duc A. Hoang
<!--published: false-->
---

<div class="alert alert-info" markdown="1">
<h1 class="alert-heading">Summary</h1>

This post contains a workflow that I use to write LaTeX documents with Overleaf and GitHub. What I want to achieve is to have a local copy of the LaTeX project on my computer, and to be able to push changes to GitHub and pull changes from GitHub. I also want to be able to work on the project on Overleaf (which is good for collaboration), and to be able to pull changes from Overleaf to my local copy and sync with GitHub. Additionally, I don't want to upload some extra files such as `Makefile`, `.devcontainer`, `.vscode`, etc. to Overleaf but still want to have them in my local copy for my own convenience. Moreover, you can have many branches on GitHub but not on Overleaf. Thus, you can, for example, use the `master` branch for the main project, `overleaf` branch for the project on Overleaf (which is used for collaboration), and other branches for old versions, testing, etc.

For illustration, all commands are in Linux. For Windows, you can use Git Bash or WSL.

**Automated Scripts:** I have created two scripts to automate the workflow, one for Linux and one for Windows 10. You can download them here: {% include files.html name="run.sh" text="run.sh" %} (Linux) and {% include files.html name="run.bat" text="run.bat" %} (Windows). Feel free to modify the scripts to suit your needs.

* TOC
{:toc}
</div>

# Basic Idea

Basically, I will have two branches: `master` and `overleaf`. The `master` branch is for GitHub, and the `overleaf` branch is for Overleaf. I will push changes to GitHub from the `master` branch, and pull changes from Overleaf to the `overleaf` branch. I will also pull changes from Overleaf to the `overleaf` branch, merge these changes to the `master` branch, and push changes to GitHub. I will use the `master` branch as the main branch.

# Initialization

1. Create a new empty repository on GitHub, note your repository ID, i.e., the part after `https://github.com/<your-username>/` in the repository's URL.
2. Create a blank Overleaf project, note your overleaf project ID, i.e., the part after `https://www.overleaf.com/project/` in the project's URL.
3. In your local PC, create a new directory for your LaTeX project, say `test-project`. Put your LaTeX files in this directory. For example, I will use my [article template](https://github.com/hoanganhduc/TeX-Templates/tree/master/A%20Simple%20Article%20Template) as the starting point.
4. Push the local project to GitHub. 
   ```bash
   cd test-project
   git init
   git remote add origin <your-github-repo-url>
   git add --all .
   git commit -S -m "first commit $(date +'%Y-%m-%d  %H:%M:%S %Z')" 
   # you can change the message and remove -S if you don't sign your commits
   git push -u origin master
   ```
5. Create a new `overleaf` branch, merge the `master` branch to the `overleaf` branch, and push the `overleaf` branch to GitHub and Overleaf.
   ```bash
   git checkout --orphan overleaf
   git rm -rf .
   git remote add overleaf https://git@git.overleaf.com/<your-overleaf-project-id>
   git pull overleaf master --allow-unrelated-histories
   ```
   Before continuing, you need to manually modify the content of `.git/config` file. Check if something like the following is there:
   ```bash
   [remote "overleaf"]
       url = https://git@git.overleaf.com/<your-overleaf-project-id>
	   fetch = +refs/heads/*:refs/remotes/overleaf/*
	   pushurl = https://git@git.overleaf.com/<your-overleaf-project-id>
   [branch "overleaf"]
       remote = overleaf
	   merge = refs/heads/master
   ```
   If not, add it. Then, push the `overleaf` branch to GitHub and Overleaf.
   ```bash
   git merge --no-commit --no-ff --allow-unrelated-histories master
   # Delete any file you do not want to upload to Overleaf
   git add --all .
   git commit -S -m "Merge master onto overleaf $(date +'%Y-%m-%d  %H:%M:%S %Z')" 
   # you can change the message and remove -S if you don't sign your commits
   git push -u origin overleaf # push to GitHub 'overleaf' branch
   git push overleaf overleaf:master # push to Overleaf
   ```

# Workflow

Now, you have a copy of the LaTeX project on your computer, GitHub, and Overleaf. 

## Work on the project on your computer, push changes to GitHub and Overleaf

To make sure you do not miss any changes, pull changes from GitHub and Overleaf before you start working on the project.
```bash
git pull --all
```

If there is any change from the `overleaf` branch, merge it to the `master` branch.
```bash
git checkout overleaf
git push -u origin overleaf # push to GitHub 'overleaf' branch
git checkout master
git merge --no-commit --no-ff --allow-unrelated-histories overleaf
git commit -S -m "Merge overleaf onto master $(date +'%Y-%m-%d  %H:%M:%S %Z')"
git push -u origin master # push to GitHub 'master' branch
```

OK, now you can work on the project locally. After you finish, push changes to GitHub and Overleaf.
First, push changes to GitHub.
```bash
git add --all .
git commit -S -m "Your commit message $(date +'%Y-%m-%d  %H:%M:%S %Z')"
git push -u origin master
```

Then, merge changes to `overleaf` branch and push changes to both GitHub and Overleaf.
```bash
git checkout overleaf
git merge --no-commit --no-ff --allow-unrelated-histories master
# Delete any file you do not want to upload to Overleaf
git add --all .
git commit -S -m "Merge master onto overleaf $(date +'%Y-%m-%d  %H:%M:%S %Z')"
git push -u origin overleaf # push to GitHub 'overleaf' branch
git push overleaf overleaf:master # push to Overleaf
```

## Work on the project on Overleaf, pull changes from Overleaf to your local copy, and sync with GitHub

To pull changes from Overleaf to your local copy
```bash
git checkout overleaf
git pull overleaf master
```

To sync with GitHub
```bash
git checkout overleaf
git push -u origin overleaf # push to GitHub 'overleaf' branch
git checkout master
git merge --no-commit --no-ff --allow-unrelated-histories overleaf
git commit -S -m "Merge overleaf onto master $(date +'%Y-%m-%d  %H:%M:%S %Z')"
git push -u origin master # push to GitHub 'master' branch
```

## Work on the project on GitHub, sync with Overleaf and your local copy

You can also work on the project on GitHub using [GitHub Codespaces](https://docs.github.com/en/codespaces/overview). For this purpose, you need to configure your codespace by creating a `.devcontainer` directory with a `devcontainer.json` file. You can use my [devcontainer.json](https://hoanganhduc.github.io/tex/devcontainer.json) as a starting point. 

To start, create `.devcontainer` directory and put `devcontainer.json` in it. Then, push the changes to GitHub.
```bash
git checkout master
git add .devcontainer
git commit -S -m "Add .devcontainer $(date +'%Y-%m-%d  %H:%M:%S %Z')"
git push -u origin master
```

Now, you can go to your GitHub repository, click on the `Code` button, and select `Open with Codespaces`. After the codespace is created, you can work on the project on GitHub. 

Once you finish, you can push changes to GitHub and Overleaf using the same steps as when you work on the project on your computer.
Finally, you can pull changes to your local copy by simply running
```bash
git pull --all
```