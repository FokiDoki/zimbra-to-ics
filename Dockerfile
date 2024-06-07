FROM python:3.9.19-slim

WORKDIR /app

COPY main.py /app

RUN pip install flask requests pykeepass gevent

EXPOSE 4443

CMD ["python", "main.py"]
