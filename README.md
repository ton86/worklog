# Worklog

## What is this?

A super simple CLI app with a few simple commands to search and display content from a "worklog.md" file using the "typer" python package.

## More info

Lately, I've been doing my personal journal in a single markdown file named "worklog.md".
 
So far, it has been a big boost to my productivity compared to trying to use multiple markdown files that later become difficult to find and review.

I wanted a simple CLI app to do the following with my "worklog.md" file with the following sample commands:

1. Search and display posts by date, word, string, #hashtag or @name. For example:

    $ python worklog.py search #ufos

    $ python worklog.py search football

    $ python worklog.py search "fantasy football"

    $ python worklog.py search 20201226

2. Display "to-do" check lists (sortable by entry or due date). Like this:

    $ python worklog.py to-do
    
    $ python worklog.py to-do --due

3. Display completed "to-do" checked lists:

    $ python worklog.py done

I felt this would be a good learning experience to get some reps in using the "typer" CLI package, using markdown formatting decorators, json config files, venv, gitignore, setup.py, github, complex list comprehension or list for loops, test-driven development, creating a standalone CLI app that doesn't require typing "python" beforee it, etc.

## Data entry rules for markdown file

Each time I make a new post in my markdown file I timestamp it with a header 2 (##) and the YYYYMMDD HHMM (military time. This is very important for proper parsing of posts. 

Example:

    ## 20201226 1400

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ...

I also use the checklist format in markdown to keep track of my to-do list.

Example:

    ## 20201226 1405

    - [x] Lorem ipsum dolor sit amet. Due: 20201230
    - [ ] Xonsectetur adipiscing elit. Due: 20201231
    - [ ] Sed do eiusmod tempor incididunt. 20200103

As long as the "- [ ]" markdown format is used at the beginning of the line any of the checkboxes will be pulled in the search and displayed even if it's in the middle of a post with other paragraphs.

A double line space (Enter, Enter) to set new paragraphs is required between posts and at the end of to-do lists.

## In testing and development

The first iteration of worklog.py will:

* Use a single markdown (md) file for the worklog.
* Use a json config file to configure the path to the default worklog md file.
* Find all check list lines in md file. (to-do list)
* Find all checked list lines in md file. (checked to-do list)
* Sort to-do lists by due date.
* Find all posts containing a string (i.e. date, word, string).
* Searches will not be case-sensitive. Strings will get converted to lowercase for all searches.

Future iterations will:
* Allow user to configure source markdown file path with a CLI command.
* Output the results of a search to new markdown, html, and pdf documents.
* For now will stick with one markdown file for everything, but if speed starts to become an issue may develop a sql db for the lines/posts in a markdown file.

## Installation

Save the files to a directory. Install python packages indicated in requirements.txt.

Future development - WIll soon package this to be callable from command line as it's own app without having to type 'python'.







