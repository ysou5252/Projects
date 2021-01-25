import cv2

import serial

arduino = serial.Serial('COM12', 9600)

cap = cv2.VideoCapture(0)

while (True):

    # Capture frame-by-frame

    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):

        break

    elif key == ord('a'):  # 왼쪽

        arduino.write(b'1\n')

        print(b'1\n')

    elif key == ord('d'):  # 오른쪽

        arduino.write(b'2\n')

        print(b'2\n')

    elif key == ord('w'):  # 위

        arduino.write(b'3\n')

        print(b'3\n')

    elif key == ord('s'):  # 아래

        arduino.write(b'4\n')

        print(b'4\n')

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()