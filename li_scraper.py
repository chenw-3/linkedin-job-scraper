#AQEIACMHHKjgwQSFWGgAAAF9-bIIGgAAAYO49zHpTgAAAAAAAAAAADBGAiEA4_g4enG5kPqhxo0hlkO1AVLHwCTDec37qz74wCMbojYCIQDSR2smrSsEAyK6947J9XgCdiEQITKTpjV2DwtylygPO9UTdnhDNFdb9W20TQEPynopny2-

import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

# Fired once for each successfully processed job
def on_data(data: EventData):
    print('[ON_DATA]', data.title, data.company, data.company_link, data.date, data.link, data.insights, len(data.description))

# Fired once for each page (25 jobs)
def on_metrics(metrics: EventMetrics):
  print('[ON_METRICS]', str(metrics))

def on_error(error):
    print('[ON_ERROR]', error)

def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path= "/Users/willi/OneDrive/Documents/Job scraper/chromedriver", # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=1.3,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
    page_load_timeout=20  # Page load timeout (in seconds)    
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        options=QueryOptions(            
            limit=27  # Limit the number of jobs to scrape.            
        )
    ),
    Query(
        query='Data Analyst',
        options=QueryOptions(
            locations=['United States'],            
            apply_link = True,  # Try to extract apply link (easy applies are skipped). Default to False.
            limit=5,
            filters=QueryFilters(              
                company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies.
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                experience=None,                
            )
        )
    ),
]

results = scraper.run(queries)
print(results)

# import pandas
#import pandas as pd

#jobs = results.to_csv()