FROM ubuntu:latest

ARG PROJECT_NAME
ARG PROJECT_VERSION
ARG PROJECT_DIST_VERSION
ARG PROJECT_DIST

RUN apt-get -y update
RUN apt-get -y install python3 python3-pip
COPY $PROJECT_DIST/dist/*.whl .
RUN pip3 install *.whl
RUN rm *.whl

CMD ["python3", "-m", "simple_package"]