# amazon-scraper
A simple scraping script to scrap amazon.  
These are the fields which are scraped  
``` 
"Name"
"URL"
"Price"
"Ratings"
"Reviews"
"Description"
"ASIN"
"Manufacturer" 
```

base url : https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1

**Note - you can access already scraped data in data folder**. 

**Note - 20 pages were traversed from above given base url and fetched about 466 products information**.  
  

---
## Libraries used

```
beautifulsoup4  
pandas  
requests  
cloudscraper  
```


# setup and run
1. run ```pip install -r requirements.txt```
2. first run  ```py main.py fetch-urls ``` , this will fetch all the urls and store in the data folder ,        ```master_data.csv```
3. then again run  ```py main.py add-data``` , this will additional data like asin, description, manufacturer and store in ```master_data.csv ```.  
 It will also save data every 50 process.
4. If ran successfully final data will be in ```data/master_data.csv```
