# Importing library
import cv2
from pyzbar.pyzbar import decode
  
 
def BarcodeReader(image):
    detectedBarcodes = decode(image)    
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected")
        return 0
    else:    
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:        
            (x, y, w, h) = barcode.rect        
            cv2.rectangle(image, (x-10, y-10),
                          (x + w+10, y + h+10), 
                          (255, 0, 0), 2)
            #print(barcode.type)       
            #print(len(barcode.data))
            if barcode.data!="":         
                #print(barcode.data, "\n")
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

def BarcodeScanner():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if BarcodeReader(ret)!=0:
            return BarcodeReader
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()