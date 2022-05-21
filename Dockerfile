FROM python:3.9

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install -r requirements.txt

EXPOSE 5001

COPY *.py /opt/app/

CMD python3 server.py
