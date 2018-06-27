FROM python:3.6.5-jessie

RUN sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list

RUN echo "deb http://http.debian.net/debian jessie-backports main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update

RUN apt-get install -y python3-dev

RUN mkdir /appl
RUN mkdir /appl/flask_demo
RUN mkdir /appl/flask_demo/logs
RUN mkdir /appl/flask_demo/projects

RUN touch /appl/flask_demo/logs/gunicorn.log

COPY project/ /appl/flask_demo/project
COPY runserver.sh /appl/flask_demo/

WORKDIR /appl/flask_demo

RUN pip install -r project/requirements.txt
RUN pip install gunicorn

EXPOSE 8000

CMD /appl/flask_demo/runserver.sh
