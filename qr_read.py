import cv2
# initalize the cam
cap = cv2.VideoCapture(0)



# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    success, img = cap.read()
    img = cv2.resize(img,(640, 480))
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        n_lines = len(bbox)
        # for i in range(len(bbox[0])):
        #     # draw all lines
        #     print('found')
        #     print(bbox)
        #     print(bbox[i][0])
        #     print(bbox[i][1])
        #     print(bbox[i+1][0])
        #     print(bbox[i+1][1])
        #     # print(bbox[0][0])
        #     # point1 = tuple(bbox[i][0])
        #     # point2 = tuple(bbox[(i+1) % n_lines][0])
        #
        #     # cv2.line(img, (int(bbox[0][0]), int(bbox[0][0])+5), (int(bbox[0][0])+5, int(bbox[0][0])+5), color=(255, 0, 0), thickness=2)
        #     # cv2.line(img, (bbox[0][i][0], bbox[0][i][1]), (bbox[0][i+1][0], bbox[0][i+1][1]), color=(255, 0, 0), thickness=2)
        #     # cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

        cv2.line(img, (int(bbox[0][0][0]), int(bbox[0][0][1])), (int(bbox[0][1][0]), int(bbox[0][1][1])), color=(255, 0, 0), thickness=2)
        cv2.line(img, (int(bbox[0][1][0]), int(bbox[0][1][1])), (int(bbox[0][2][0]), int(bbox[0][2][1])), color=(255, 0, 0), thickness=2)
        cv2.line(img, (int(bbox[0][2][0]), int(bbox[0][2][1])), (int(bbox[0][3][0]), int(bbox[0][3][1])), color=(255, 0, 0), thickness=2)
        cv2.line(img, (int(bbox[0][3][0]), int(bbox[0][3][1])), (int(bbox[0][0][0]), int(bbox[0][0][1])), color=(255, 0, 0), thickness=2)
        # cv2.line(img, (int(15.2), int(25.4)), (int(45.6), int(65.7)), color=(255, 0, 0), thickness=2)
        if data:
            print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
