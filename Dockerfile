# Which version of python
# -slim, smaller container

# Here we use conda as I use conda 
# to manage my python environments on my local machine.
FROM python:3.8.16-slim 

# What code and docs
# COPY ./src /opt/app/
COPY . /app
WORKDIR /app/

# Default installs in linux
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    gcc && \
    make

# Create a virtual environment
RUN python3 -m venv /opt/py38 && \
    /opt/py38/bin/python -m pip install pip --upgrade && \
    /opt/py38/bin/python -m pip install -r /app/src/requirements.txt

# Purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Make entrypoint.sh executable
RUN chmod +x ./src/entrypoint.sh

# Run the app
CMD ["./entrypoint.sh"]