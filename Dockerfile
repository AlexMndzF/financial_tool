FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get intall python 3.7
RUN apt-get install -y python3-pip python-dev build-essential
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]