---
layout: page
title: CSP Notes
permalink: /notes/
---
 
## Notes For CSP

- Markdown posts show text but don't process code
- Jupyter notebooks permit us to exemplify running code
- You can utilize markdown to make tables
- There 3 different loops you can utilize (for loop, while loop, recursive loop)
- Code.org is a simple way to learn and work with Java programming by utilizing blocks

## How to Enter and Code with wsl:

```bash
PS C:\Users\Marti> wsl
(base) martinnguyen64@LAPTOP-LDAO5KM3:/mnt/c/Users/marti$ cd ~
(base) martinnguyen64@LAPTOP-LDAO5KM3:~$ cd vscode
(base) martinnguyen64@LAPTOP-LDAO5KM3:~/vscode$ cd Martins-Blog
(base) martinnguyen64@LAPTOP-LDAO5KM3:~/vscode/Martins-Blog$ code .
```
## How to Create Notebooks Utilizing Bash
1. Enter vscode with wsl.

2. Use these commands with python:

```bash
echo "Using conditional statement to create a project directory and project"

# Variable section
export project_dir=$HOME/vscode  # change vscode to different name to test git clone
export project=$project_dir/APCSP  # change APCSP to name of project from git clone
export project_repo="https://github.com/nighthawkcoders/APCSP.git"  # change to project of choice

cd ~    # start in home directory

# Conditional block to make a project directory
if [ ! -d $project_dir ]
then 
    echo "Directory $project_dir does not exists... makinng directory $project_dir"
    mkdir -p $project_dir
fi
echo "Directory $project_dir exists." 

# Conditional block to git clone a project from project_repo
if [ ! -d $project ]
then
    echo "Directory $project does not exists... cloning $project_repo"
    cd $project_dir
    git clone $project_repo
    cd ~
fi
echo "Directory $project exists." 
```
*Change repo link to my own*

3. You can look at files in folder with this:

```bash
# You must run cells above to define variable and project

echo "Navigate to project, then navigate to area wwhere files were cloned"
cd $project
pwd

echo ""
echo "list top level or root of files with project pulled from github"
ls

echo ""
echo "list again with hidden files pulled from github"
ls -a   # hidden files flag, many shell commands have flags

echo ""
echo "list all files in long format"
ls -al   # all files and long listing
```

```bash
# You must run cells above to define variable and project

echo "Look for posts"
export posts=$project/_posts  # _posts inside project
cd $posts  # this should exist per fastpages
pwd  # present working directory
ls -l  # list posts
```

```bash
# You must run cells above to define variable and project

echo "Look for notebooks"
export notebooks=$project/_notebooks  # _notebooks is inside project
cd $notebooks   # this should exist per fastpages
pwd  # present working directory
ls -l  # list notebooks
```

```bash
# You must run cells above to define notebooks location

echo "Look for images in notebooks, print working directory, list files"
cd $notebooks/images  # this should exist per fastpages
pwd
ls -l
```

4. You can also look inside files (markdown file):

```bash
# You must run cells above to define project
echo "Navigate to project, then navigate to area wwhere files were cloned"

cd $project
echo "show the contents of README.md"
echo ""

cat README.md  # show contents of file, in this case markdown
echo ""
echo "end of README.md"
```
