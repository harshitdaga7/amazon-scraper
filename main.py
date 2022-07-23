from scraper import scraper
from scraper import get_product_details_by_link
import json
import pandas as pd
import sys

def add_additonal_data():

        
    master_df = pd.read_csv('./data/master_data.csv')
    print(master_df.size)
    
    for i,link in enumerate(master_df['URL']):
        
        print("processing",i,"index")
        if link != "NA":
            detailed_data = get_product_details_by_link(link)
            required_fields = ["Name","Description","ASIN","Manufacturer"]

            for f in required_fields:
                master_df[f][i] = detailed_data[f]
            
            if i%50 == 0:
                master_df.to_csv('./data/master_data.csv',index = False,header = True)
                print("saved master data to master_data.csv")

    
    master_df.to_csv('./data/master_data.csv',index = False,header = True)
    print("saved master data to master_data.csv")


if __name__ == '__main__':
    

    if len(sys.argv) == 1: print("missing arguments ,fetch-urls, additional-data")
    elif sys.argv[1] == "fetch-urls":

        columns = ["Name","URL","Price","Ratings","Reviews","Description","ASIN","Manufacturer"]
        master_df = pd.DataFrame(columns = columns)
        total_pages = 20

        # iteration 1 to get all the urls
        for page_no in range(1,total_pages + 1):
        
            print("processing page",page_no)
            url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page_no}"
            print("url: ",url)
            data = scraper(columns,url)

            with open(f"./data/data_{page_no}.json",'w') as f:
                json.dump(data,f)
            
            print(f'saved in data_{page_no}.json')

            df = pd.DataFrame(data,columns = columns)
            master_df = master_df.append(df)
            df.to_csv(f'./data/data_{page_no}.csv',index = False,header = True)
            print(f'saved to data_{page_no}.csv')
        
        master_df.to_csv('./data/master_data.csv',index = False,header = True)
        print("saved master data to master_data.csv")\
    
    elif sys.argv[1] == "add-data":
        add_additonal_data()
    else:
        print("unknown argument")


    



    



   