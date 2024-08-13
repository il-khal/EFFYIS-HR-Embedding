FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Download spaCy models
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download fr_core_news_sm  # For French stop words if needed

CMD ["python", "-u", "rp_handler.py"]
