FROM python:alpine

ADD storageavailability.py /

ENTRYPOINT ["python", "storageavailability.py"]