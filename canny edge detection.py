import cv2 

cv2.namedWindow('window') 

def nothing(x):
    pass

# img = cv2.imread('FILENAME HERE') #enable to use edge detection for IMAGE FILES (.png, .jpg etc.)

# cap = cv2.VideoCapture('FILENAME HERE') #enable to use edge detection for VIDEO FILES (.mp4, .flv etc.) to use on webcam put 0 in place of FILENAME

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts to grayscale (enable to use edge detection for IMAGE FILES (.png, .jpg etc.)

while True:

    # _, img = cap.read() #enable to use edge detection for VIDEO FILES (.mp4, .flv etc.)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale #enable to use edge detection for VIDEO FILES (.mp4, .flv etc.)

    edge = cv2.Canny(gray, 130, 0) #scaling,, can be between 0 and 255 on both X and Y

    cv2.imshow('window', edge)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
