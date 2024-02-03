# Importing library
import cv2
from pyzbar.pyzbar import decode
  
 
def BarcodeReader(image):
    img = cv2.imread(image)    
    detectedBarcodes = decode(img)    
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected")
    else:    
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:        
            (x, y, w, h) = barcode.rect        
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10), 
                          (255, 0, 0), 2)
            #print(barcode.type)       
            #print(len(barcode.data))
            if barcode.data!="":         
                print(barcode.data, "\n")
                return barcode.data             
 
def getImage():
  vid = cv2.VideoCapture(0) 
  while(True): 
      ret, frame = vid.read() 
      cv2.imshow('frame', frame) 
      if cv2.waitKey(1) & 0xFF == ord('q'): 
          break
  vid.release()
  cv2.destroyAllWindows() 

  