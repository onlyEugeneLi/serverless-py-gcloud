import pathlib
from functools import lru_cache
from decouple import Config, RepositoryEnv # Configuring environment variables

# Get the path of the .env file in the project
# Don't have to hard code the path
BASE_DIR = pathlib.Path(__file__).parent.parent # parent.parent = ../.. (going back two directories)
# .env path: /Users/maceugene/Documents/Projects/serverless-py/.env
print(BASE_DIR)
ENV_PATH = BASE_DIR / '.env'
print(ENV_PATH)

# Cache the envrionment settings, when it gets cold
@lru_cache
def get_config():
    # decouple package looks for the .env file
    if ENV_PATH.exists():
        # Found .env file, read the file specified by ENV_PATH.
        return Config(RepositoryEnv(str(ENV_PATH)))
        # Returns a Config object that looks for variables in the .env file. 
    # If it the env file does not exist
    from decouple import config
    return config


config = get_config()