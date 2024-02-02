import requests
from BarcodeReader import BarcodeReader, getImage, BarcodeScanner

def main():
    apiKey="WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt"
    image="IMG_4313.JPG"
    gtin=str(BarcodeScanner()) #casting from bytes to str
    gtin=gtin[2:len(gtin)-1] #2 or 3?
    while True:   
        if len(gtin)<12:
           print("food not in database")
           break 
        print(gtin)
        url=f"https://api.nal.usda.gov/fdc/v1/foods/search?query={gtin}&pageSize=10&api_key={apiKey}"
        print("\n-----------",url,"\n-------------\n")
        #sample link
        #'''https://api.nal.usda.gov/fdc/v1/foods/search?query=856579002927&pageSize=10&api_key=WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt'''
        response=requests.get(url)
        data = response.json()
        #print(response) 
        print("\n-----------\n-------------\n")
        if data["totalHits"]==1:
            print(data["foods"][0]["description"])
            break
        else: 
            print("error!")
            gtin=gtin[1:len(gtin)-1]
     
 
#pandas and organizing  stuff blah blah blah
if __name__ == "__main__":
 main()

  