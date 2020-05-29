# MLScraper
Web Scraper built with Selenium to extract site data and run through an SVM classifier to extract relevant text.

# How to Use :
First run redis-server. 
Then run flaskapp.py.
Then run Celery worker using celery -A flaskapp.celery worker --loglevel=info --config=celeryconfig --pool=eventlet

# To add data for training :
Inject js_click_content.js in browser and manually select important text. 
Press right-alt to download CSV of the site text. Repeat for multiple sites.
Combine CSVs with csv_merger.py and add to existing svm_training_data.csv.
Retrain model and check stats for performance.

# Others :
- Change values in multiscript_config.py to update broker URLs and SVM performance.
- Assumed average reading speed of a person is in js_mc_nc.