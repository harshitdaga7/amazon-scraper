from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time


def is_not_empty_string(field):


    if field == None or field == "" or field == " " or len(field) == 0:
        return False

    return True


def get_product_details_by_link(url):

  time.sleep(2)
  page = urlopen(url)
  html = page.read().decode('utf-8')
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
  page = urlopen(url)
  html = page.read().decode("utf-8")
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
      link = str(link_tag['href']) if link_tag else "NA"
      price = str(price_tag.string) if price_tag else "NA"
      rating = str(rating_tag.string).split(" ")[0] if rating_tag else "NA"
      reviews = str(reviews_tag.string) if reviews_tag else "NA"
      

      arr = [name,link,price,rating,reviews,"NA","NA","NA"]
      
      for i,c in enumerate(columns):
        data[c].append(arr[i])
  print("completed primary information")

  print("extracting detailed infomation")
  for i,link in enumerate(data['URL']):
    
    print(f"extracting {i}th data")

    detailed_product_data = get_product_details_by_link("https://www.amazon.in" + link)
    
    required_fields = ["Name","Description","ASIN","Manufacturer"]

    for f in required_fields:
      data[f][i] = detailed_product_data[f]
  
  print("completed detailed information")
  
  return data


