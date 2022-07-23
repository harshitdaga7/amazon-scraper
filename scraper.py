from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import time
import cloudscraper


def is_not_empty_string(field):


    if field == None or field == "" or field == " " or len(field) == 0:
        return False

    return True


def get_product_details_by_link(url):

  
  time.sleep(1) #added to prevent 503 error

  scraper = cloudscraper.create_scraper()
  html = scraper.get(url).text
  soup = BeautifulSoup(html,'html.parser')

  name_tag = soup.find(id = "productTitle")
  description_tag = soup.find(id = "feature-bullets")
  asin_tag = soup.find("span",text = re.compile("^ASIN"))
  manufacturer_tag = soup.find("span",text = re.compile("^Manufacturer"))

  name = str(name_tag.string) if name_tag else "NA"
  description = str(description_tag.get_text()) if description_tag else "NA"
  asin = str(asin_tag.parent.contents[-2].string) if asin_tag else "NA"
  manufacturer = str(manufacturer_tag.parent.contents[-2].string) if manufacturer_tag else "NA"


  return {"Name":name,"Description":description,"ASIN":asin,"Manufacturer":manufacturer}


def scraper(columns, url):
  data = {}
  for c in columns:
    data[c] =[]


  scraper = cloudscraper.create_scraper()
  html = scraper.get(url).text
  soup = BeautifulSoup(html, "html.parser")
  products = soup.find_all('div',attrs={"data-asin": is_not_empty_string})

  print("No of products :", len(products))
  print("extracting primary information")
  for prod in products:

      name_tag = prod.find("span",class_ = "a-size-medium a-color-base a-text-normal")
      link_tag = prod.find("a",class_ = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
      price_tag = prod.find("span",class_ ="a-price-whole")
      rating_tag = prod.find("span",class_ = "a-icon-alt")
      reviews_tag = prod.find("span",class_ = "a-size-base s-underline-text")

      name = str(name_tag.string) if name_tag else "NA"
      link = ("https://www.amazon.in" + str(link_tag['href'])) if link_tag else "NA"
      price = str(price_tag.string) if price_tag else "NA"
      rating = str(rating_tag.string).split(" ")[0] if rating_tag else "NA"
      reviews = str(reviews_tag.string) if reviews_tag else "NA"
      

      arr = [name,link,price,rating,reviews,"NA","NA","NA"]
      if link != "NA":
        for i,c in enumerate(columns):
          data[c].append(arr[i])
  print("completed primary information")

  
  return data


