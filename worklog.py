import typer
from source import source
from datetime import datetime
from output import output_dir


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
    sort_due: bool = typer.Option(False, "--due", help="Sort by due date."),
    backlog: bool = typer.Option(False, "--backlog", help="Chronological backlog."),
    sort_entry: bool = typer.Option(False, "--entry", help="Sort by entry date.")
    ):
    """ 
    Print to-do check list and/or to-do backlog. Prints due list by default.
    """
    check_list = lines_start_with('- [ ]')
    due_list = [line for line in check_list if not line.endswith('Backlog\n')]
    due_list = sorted(due_list, key=lambda x: (x[-10:]))
    backlog_list = [line for line in check_list if line.endswith('Backlog\n')]
    if sort_due and backlog:
        check_list = sorted(check_list, key=lambda x: (x[-10:]))
        typer.echo('To do and backlog (sorted by due date):\n') 
        typer.echo(concat(check_list)) 
    elif sort_due:
        typer.echo('To do (sorted by due date):\n') 
        typer.echo(concat(due_list))
    elif backlog:
        typer.echo('Backlog (sorted by entry):\n') 
        typer.echo(concat(backlog_list))
    elif sort_entry:
        typer.echo('To do (sorted by entry):\n') 
        typer.echo(concat(check_list))        
    else:
        typer.echo('To do (sorted by due date):\n') 
        typer.echo(concat(due_list))


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


@app.command()
def today():
    """
    Return markdown text of today's posts.
    Output markdown file.
    """
    todays_posts = []
    yyyymmdd = datetime.today().strftime('%Y%m%d')
    header_date = f'### {yyyymmdd}'
    for post in posts:
        found = False
        for line in post:
            if header_date in line.lower():
                found = True
        if found:
            todays_posts.append(post)
            typer.echo(concat(post))
    if len(todays_posts) > 0: 
        flat_list = [item for sublist in todays_posts for item in sublist]
        string = ' '.join(map(str, flat_list))
        md_file = open(f'{output_dir()}\\worklog{yyyymmdd}.md', 'w')
        n = md_file.write(string)
        md_file.close()


if __name__ == '__main__':
    app()

         
