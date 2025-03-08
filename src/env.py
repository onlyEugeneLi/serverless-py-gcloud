import io
import os
import pathlib
from functools import lru_cache

# from python-decouple
from decouple import Config, RepositoryEmpty, RepositoryEnv

# import google-auth
import google.auth
# import google-cloud-secret-manager
from google.cloud import secretmanager

# maps to "path/to/project"
BASE_DIR = pathlib.Path(__file__).parent.parent 

# if Using Django
# from django.conf import settings
# BASE_DIR = settings.BASE_DIR

# ensure that `.env` is listed in `.gitignore`
ENV_PATH = BASE_DIR / ".env"


# if Using Django
# from django.conf import settings
# BASE_DIR = settings.BASE_DIR


def get_google_secret_payload(gcloud_secret_name = "py-env-file"):
    """
    Load a secret from Google Cloud Secrets Manager
    """
    try:
        _, project_id = google.auth.default()
    except google.auth.exceptions.DefaultCredentialsError:
        project_id = None
    if project_id:
        client = secretmanager.SecretManagerServiceClient()
        # use an injected operating system environment variable 
        # for the gcloud secret name or 
        # the value of the "gcloud_secret_name" argument
        secret_label = os.environ.get("GCLOUD_SECRET_NAME", gcloud_secret_name)
        # project_id comes from previous step
        gcloud_secret_name_path = f"projects/{project_id}/secrets/{secret_label}/versions/latest"
        # this should print the contents of your secret
        payload = client.access_secret_version(name=gcloud_secret_name_path).payload.data.decode("UTF-8")
        return payload
    return None

class RepositoryString(RepositoryEmpty):
    """
    Retrieves option keys from an ENV string file
    """
    def __init__(self, source):
        """
        Take a string source with the dotenv file format:

        KEY=value
        
        Then parse it into a dictionary
        """
        source = io.StringIO(source)
        if not isinstance(source, io.StringIO):
            raise ValueError("source must be an instance of io.StringIO")
        self.data = {}
        file_ = source.read().split("\n")
        for line in file_:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip()
            if len(v) >= 2 and (
                (v[0] == "'" and v[-1] == "'") or (v[0] == '"' and v[-1] == '"')
            ):
                v = v[1:-1]
            self.data[k] = v

    def __contains__(self, key):
        return key in os.environ or key in self.data

    def __getitem__(self, key):
        return self.data[key]


@lru_cache()
def get_config(use_gcloud=True):
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    if use_gcloud:
        payload = get_google_secret_payload()
        if payload is not None:
            return Config(RepositoryString(payload))
    from decouple import config

    return config

config = get_config()


# lru_cache() is used to cache the result of the function
# so that it doesn't have to be re-evaluated on every call
# https://docs.python.org/3/library/functools.html#functools.lru_cache
@lru_cache()
def get_config():
    """Get configuration from .env file or os.environ"""
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    from decouple import config
    return config


# return our new default `config` call to replace `config` from `decouple`
config = get_config()