FROM ubuntu:20.04 AS sensdb_container

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common curl python2 virtualenv
RUN apt-get install -y --no-install-recommends git

RUN mkdir -p -v /src/django_example
WORKDIR /src/pip_cache
RUN curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
RUN python2 get-pip.py

#WORKDIR /src/django_example
#COPY requirements.txt .
#RUN virtualenv --python=python2 venv
#RUN . venv/bin/activate && pip install psycopg2-binary && python -m pip install pip-tools && pip install -r requirements.txt
#RUN echo "INSTALLED DEPENDENCIES SUCCESSFULLY"
#
#COPY . .
#RUN chmod 0777 docker_entrypoint.sh
#RUN pip install -e .

EXPOSE 8000
RUN ls -a

