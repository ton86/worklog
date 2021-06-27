from pathlib import Path
import json 


# Directory
dir = Path().resolve()


# Configuration
with open(dir/'config.json') as config_file:
    CONFIG = json.load(config_file)


def default_md(config = CONFIG):
    """
    Return string for default markdown file path.
    """
    return(config['markdown_file']['path'])


def get_lines(md_file_path):
    """
    Return list of lines from markdown file.
    """
    with open(md_file_path, 'r', encoding="utf8") as md_file:
        lines = md_file.readlines()
        return lines     


def group_posts(lines):
    """
    Return list of posts and within each post a list of its lines.
    """
    posts = []
    post = []
    lines.append('### ')
    for line in lines:
        if line.startswith('### '):
            posts.append(post)
            post = [line]
        else:
            post.append(line)
    return posts


def source(md_source = default_md()):
    """
    Return list of lists (posts w/post lines) from a markdown file.
    """
    lines = get_lines(md_source)
    return group_posts(lines)


