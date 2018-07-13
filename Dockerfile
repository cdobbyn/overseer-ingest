FROM python:3.6

# OR, if you’re using a directory for your requirements, copy everything (comment out the above and uncomment this if so):
# ADD requirements /requirements

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN set -ex \
    && apt update \
    && apt install -y \
            libffi-dev \
            gcc \
            g++ \
            make \
            libc-dev \
            musl-dev \
            libjpeg-dev \
            zlib1g-dev \
            libpq-dev \
            ntp \
            tzdata

RUN python3.6 -m venv /opt/venv
RUN /opt/venv/bin/pip install -U pip

# Copy in the requirements file
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/opt/venv/bin/pip install --no-cache-dir uWSGI==2.0.15"
ADD requirements.txt /opt/requirements.txt
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/opt/venv/bin/pip install --no-cache-dir -r /opt/requirements.txt"

# Copy your application code to the container
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY  ./src /opt/app

COPY docker-entrypoint.sh /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]