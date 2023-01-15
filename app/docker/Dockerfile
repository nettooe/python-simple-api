FROM python:3.10

WORKDIR /home

COPY src/ /home/src/

RUN pwd
RUN python3.10 --version
RUN ls -la /home/src

CMD [ "python", "/home/src/controller.py"] 