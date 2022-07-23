from scraper import scraper
import json
import pandas as pd

if __name__ == '__main__':
    
    columns = ["Name","URL","Price","Ratings","Reviews","Description","ASIN","Manufacturer"]
    master_df = pd.DataFrame(columns = columns)

    total_pages = 20

    for page_no in range(1,total_pages + 1):
    
        print("processing page",page_no)
        url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{page_no}"
        print("url: ",url)
        data = scraper(columns,url)

        with open(f"data_{page_no}.json",'w') as f:
            json.dump(data,f)
        
        print(f'saved in data_{page_no}.json')

        df = pd.DataFrame(data,columns = columns)
        master_df = master_df.append(df)
        df.to_csv(f'data_{page_no}.csv',index = False,header = True)
        print(f'saved to data_{page_no}.csv')
    
    master_df.to_csv('master_data.csv',index = False,header = True)
    print("saved master data to master_data.csv")



   