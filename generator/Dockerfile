FROM python:3.8-bullseye
ENV LC_ALL=C.UTF-8
RUN apt update && apt upgrade -y && \
    useradd -m worker
USER worker
RUN mkdir /home/worker/src && \
    mkdir /home/worker/src/output
WORKDIR /home/worker/src
RUN chown -R worker:worker /home/worker/src

COPY requirements.txt .
RUN pip3 install -r requirements.txt && \
    rm -f requirements.txt

COPY --chown=worker:worker generateToDos.py .
ENTRYPOINT ["python", "generateToDos.py"]