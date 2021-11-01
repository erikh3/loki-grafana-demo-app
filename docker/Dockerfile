ARG PYTHON_VERSION=3.9.6-slim-buster

###########
# BUILDER #
###########

# pull official base image
FROM python:${PYTHON_VERSION} as builder

# upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# copy source code & set the work directory
COPY . /usr/src
WORKDIR /usr/src

# install python dependencies
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:${PYTHON_VERSION}

# Set variables
ENV APPDIR /opt/logger_demo_app
ENV USER app
ENV GROUP app

# create directory for the app user & create the app user
RUN mkdir -p ${APPDIR} \
    && addgroup --system ${GROUP} \
    && adduser --system ${USER} --group --home ${APPDIR}

# set the work directory
WORKDIR ${APPDIR}

# update & install packages & dependencies
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir /wheels/*

# copy entrypoint.sh
COPY docker/entrypoint.sh .

# copy project files
COPY --from=builder /usr/src .

# chown all the files to the app user
RUN chown -R ${USER}:${GROUP} .
# change to the app user
USER ${USER}

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]
