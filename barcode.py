import cv2
import time
from pyzbar import pyzbar

used_codes = []
font = cv2.FONT_HERSHEY_DUPLEX

def read_barcodes(frame, cap, timer):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1 Dibujo rectangulo
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 2 Put Text
        barcode_info = barcode.data.decode('utf-8')
        
        cv2.putText(frame, barcode_info, (x + 6, y - 6),
                    font, 1.0, (255, 255, 255), 1)

        # 3 Save Data y el Timer
        if barcode_info not in used_codes:
          used_codes.append(barcode_info)

          with open("barcode_result.txt", mode='a') as file:
              file.write(barcode_info + 
                      " Type: " + barcode.type + 
                      " Timer: " + str(timer) + "\n")

    return frame

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
#cap = cv2.VideoCapture('video2.mp4')
cap = cv2.VideoCapture(0)

# Video height and width
#height = cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT)
#width = cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH)
#print(f'Width {width}, Height {height}')

framesVideo = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('Total de Frames: ' + str(framesVideo))

#FPS
#fps = cap.get(cv2.cv2.CAP_PROP_FPS)
#print(f'FPS : {fps:0.2f}')

#Longitud del video
#longVideo = framesVideo / fps
#print(f'Longitud del video: {longVideo:0.2f}')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error abriendo el archivo")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if  ret == True:
 
    ret, frame = cap.read()

    #Print Timer
    timer = "%0.2f" % (cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)

    frame = read_barcodes(frame, cap, timer)

    # put the Timer variable over the video frame
    cv2.putText(frame, timer,
                        (10, 30),
                        font, 1,
                        (0, 255, 0),
                        4, cv2.LINE_8)

    # Display the resulting frame
    cv2.imshow('Barcode/QR code reader', frame)
                        
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
      break  
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
