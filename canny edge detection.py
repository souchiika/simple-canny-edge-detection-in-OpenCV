import cv2 #ext library

cv2.namedWindow('window') #plop UI

def nothing(x):
    pass

# img = cv2.imread('FRAME00300.png') #image name, this probably wont be here in final thing TEST

cap = cv2.VideoCapture('fatalhamburger.mp4')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale

while True:

    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale

    edge = cv2.Canny(gray, 130, 0) #scaling,, can be between 0 and 255 on both X and Y

    cv2.imshow('window', edge)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break