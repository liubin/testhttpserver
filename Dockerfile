FROM python:alpine

EXPOSE 80

COPY app.py /
CMD ["python", "/app.py"]
