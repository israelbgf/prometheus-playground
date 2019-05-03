FROM python:3.7.3-alpine
WORKDIR /application/
COPY application .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "entrypoint.py"]