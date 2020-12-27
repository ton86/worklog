# from pathlib import Path
from source import source
import json 
import sys
import typer
import re


# Start a typer app
# https://github.com/tiangolo/typer
app = typer.Typer()


# Imports list of posts from worklog file.
posts = source()


def lines_start_with(substring):
    # Return list of lines that start with a substring
    # return [l for l in lines if l.startswith(substring)]
    lines_found = []
    for post in posts:
        for line in post:
            if line.startswith(substring):
                lines_found.append(line)
    return lines_found


def concat(list):
    # Return string of concatenated list str objects
    return ''.join(list)


@app.command()
def to_do(
    sort_due: bool = typer.Option(False, "--due", help="Sort by due date.")):
    """ 
    Print to-do check list.
    """
    check_list = lines_start_with('- [ ]')
    if sort_due:
        check_list = sorted(check_list, key=lambda x: (x[-10:]))
        typer.echo('To do (sorted by due date):\n') 
        typer.echo(concat(check_list))
    else:
        typer.echo('To do (sorted by entry):\n') 
        typer.echo(concat(check_list))


@app.command()
def done():
    """
    Print completed to-do list.
    """
    checked_list = lines_start_with('- [x]')
    typer.echo(concat(checked_list))


@app.command()
def search(string: str):
    """
    Return list of posts based on user defined search string.
    """
    typer.echo('\n Search results:\n \n')
    posts_found = []
    for post in posts:
        found = False
        for line in post:
            if string.lower() in line.lower():
                found = True
        if found:
            posts_found.append(post)
            typer.echo(concat(post))


if __name__ == '__main__':
    app()

         
