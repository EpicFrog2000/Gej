FROM python:3.12.0b4-slim-bullseye

ADD WebScrape.py .

RUN pip install selenium webdriver-manager beautifulsoup4

CMD ["python", "./WebScrape.py"]
