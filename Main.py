import requests
from BarcodeReader import BarcodeReader

def main():
    apiKey="WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt"
    image="Img.jpg"
    gtin=BarcodeReader(image)
    #sample gtin
    #gtin=856579002927
    url=f"https://api.nal.usda.gov/fdc/v1/foods/search?query={gtin}&pageSize=10&api_key={apiKey}"
    #sample link
    #'''https://api.nal.usda.gov/fdc/v1/foods/search?query=856579002927&pageSize=10&api_key=WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt'''
    response=requests.get(url)
    print(response)
    print(response.content)
    print("sucess") 
 
#pandas and organizing  stuff blah blah blah
if __name__ == "__main__":
 main()

 