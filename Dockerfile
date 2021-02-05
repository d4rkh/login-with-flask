FROM ubuntu:18.04
MAINTAINER Madhav Purohit "foritprotv@gmail.com"

RUN apt-get update -y && apt-get install python3-pip python3-dev -y
CMD ["ufw allow 5000"]

RUN pip3 install flask
COPY ./* /app
WORKDIR /app

ENTRYPOINT ["python3"]
cmd ["main.py"]