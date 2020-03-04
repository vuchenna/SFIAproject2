FROM python:3.6
WORKDIR /app
COPY requirements.txt .
EXPOSE 5000
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
