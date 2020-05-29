# MLScraper
Web Scraper built with Selenium to extract site data and run through an SVM classifier to extract relevant text.

Run flaskapp.py followed by Celery worker using celery -A flaskapp.celery worker --loglevel=info --config=celeryconfig --pool=eventlet