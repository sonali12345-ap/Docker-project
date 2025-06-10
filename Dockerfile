FROM python:3.7
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python","run.py"]
