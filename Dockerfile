# Which version of python
# -slim, smaller container

# Here we use conda as I use conda 
# to manage my python environments on my local machine.
FROM conda/miniconda3:latest

# What code and docs
# COPY ./src /opt/app/
COPY ./src /app/
# What requriements are needed
COPY requriements /app/requriements.txt 
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
RUN conda create --name cloud python=3.11 && \
    conda run -n cloud pip install -r requirements.txt

# Purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Run the app
CMD ["./entrypoint.sh"]