import requests
from BarcodeReader import BarcodeReader, BarcodeVidReader
import json
#---get gtin from image file---
def get_gtin(image_path):
    gtin=BarcodeReader(image_path)  
    return gtin 

def get_nutrients(data,nutrients):
    for i in range(len(data["foods"][0]["foodNutrients"])): #getting nutrition information
                nutrient=data["foods"][0]["foodNutrients"][i]["nutrientName"]
                for j in nutrients.keys():
                    if j==nutrient:
                        nutrients[j]=data["foods"][0]["foodNutrients"][i]["value"]
    return
                       
#---get nutrition data---
def search_food_in_database(gtin, api_key,nutrients):

    #print(len(gtin), "gtin length")
    while len(gtin) >= 12:
        url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={gtin}&pageSize=10&api_key={api_key}"
        print(f"\n-----------\n{url}\n-------------\n")
        response = requests.get(url) #get data on product
        data = response.json()
        print("\n-----------\n-------------\n")
        if data["totalHits"]== 1:
            get_nutrients(data,nutrients)
            return
        gtin = gtin[1:]
    print("Food not found in the database")
    return False

def main():
    #stores results of nutrients and vitamins
    nutrients={ 
        "Vitamin B-12": 0, 
        "Iron, Fe": 0,
        "Calcium, Ca" : 0,
        "Magnesium, Mg": 0,
        "Zinc, Zn": 0
    }
     #---mode for image file---
    #image_path = "IMG_4317.JPG"
    api_key = "WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt"
    #---mode for barcode scanner---
    gtin = BarcodeVidReader()
    if type(gtin)!=str:
        gtin=str(gtin, 'utf-8')  # Casting from bytes to str
    while len(gtin) < 13:        # resize to size 13
        gtin="0"+gtin
    search_food_in_database(gtin, api_key,nutrients) 
    print(nutrients)
    return nutrients

# pandas and organizing stuff blah blah blah
if __name__ == "__main__":
    main()