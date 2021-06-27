from pathlib import Path
import json 


# Directory
dir = Path().resolve()


# Configuration
with open(dir/'config.json') as config_file:
    CONFIG = json.load(config_file)


def output_dir(config = CONFIG):
    """
    Return string for default output directory path.
    """
    return(config['output_dir']['path'])