# MLScraper
Web Scraper built with Selenium to extract site data and run through an SVM classifier to extract relevant text.

# How to Use :
First run redis-server. 
Then run flaskapp.py.
Then run Celery worker using celery -A flaskapp.celery worker --loglevel=info --config=celeryconfig --pool=eventlet