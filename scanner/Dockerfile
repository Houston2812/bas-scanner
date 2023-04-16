FROM python:alpine3.17

WORKDIR /scanner
RUN mkdir -p /scanner/logs
COPY ./requirements.txt /scanner/requirements.txt
COPY ./src  /scanner/src
#COPY ./tests  /scanner/test
COPY ./payloads /scanner/payloads

RUN pip3 install -r /scanner/requirements.txt
RUN sh -c 'echo SCANNER_DIR="$(pwd)" > src/.env'
CMD ["python3", "/scanner/src/scanner.py", "-s", "directory_traversal_basic"]
# CMD ["python3", "/scanner/test/test.py"]

