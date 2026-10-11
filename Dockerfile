FROM python:3.13-slim
WORKDIR /srv
COPY app ./app
USER nobody
EXPOSE 8080
CMD ["python", "-m", "app.main"]
