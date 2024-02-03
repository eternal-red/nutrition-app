import requests
from BarcodeReader import BarcodeReader, BarcodeVidReader

def get_gtin(image_path):
    gtin=BarcodeReader(image_path)  
    return gtin 

def search_food_in_database(gtin, api_key):
    print(len(gtin), "gtin length")
    while len(gtin) >= 12:
        print(gtin)
        url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={gtin}&pageSize=10&api_key={api_key}"
        print(f"\n-----------\n{url}\n-------------\n")
        response = requests.get(url)
        data = response.json()
        print("\n-----------\n-------------\n")
        if data["totalHits"]== 1:
            return data["foods"][0]["description"]
        gtin = gtin[1:]
    print("Food not found in the database")
    return False

def main():
    #image_path = "IMG_4317.JPG"
    api_key = "WvJcUpdiej9dX4GGDhFS6ceCzZxmwUg9SetWsqvt"
    gtin = BarcodeVidReader()
    print("entered main")
    print(gtin)
    if type(gtin)!=str:
        gtin=str(gtin, 'utf-8')  # Casting from bytes to str
    print(gtin)
    while len(gtin) < 13:
        gtin="0"+gtin
    print(search_food_in_database(gtin, api_key))

# pandas and organizing stuff blah blah blah
if __name__ == "__main__":
    main()