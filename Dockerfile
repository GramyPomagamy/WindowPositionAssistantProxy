FROM python:3.13-slim

EXPOSE 80/tcp

RUN mkdir /app
WORKDIR /app

COPY requirements.txt wpap.py wsgi.py /app/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:80"]
CMD ["--threads", "4"]
