import requests
from BarcodeReader import BarcodeReader, getImage

def main():
    apiKey="WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt"
    image="IMG_3958.JPG"
    gtin=str(BarcodeReader(image)) #casting from bytes to str
    gtin=gtin[3:len(gtin)-1] #2 or 3??
    print(gtin)
    #sample gtin
    #gtin=856579002927
    url=f"https://api.nal.usda.gov/fdc/v1/foods/search?query={gtin}&pageSize=10&api_key={apiKey}"
    print("\n-----------",url,"\n-------------\n")
    #sample link
    #'''https://api.nal.usda.gov/fdc/v1/foods/search?query=856579002927&pageSize=10&api_key=WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt'''
    response=requests.get(url)
    data = response.json()
    #print(response)
    print(data["foods"][0]["description"])
    print("sucess") 
 
#pandas and organizing  stuff blah blah blah
if __name__ == "__main__":
 main()

 
# b'0052603041843'
# b'0016000124790'