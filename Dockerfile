FROM python:alpine

ADD storageavailability.py /

ENTRYPOINT ["python", "-u", "storageavailability.py"]