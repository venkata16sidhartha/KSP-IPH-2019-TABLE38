import cv2

def lap(x):
    img = cv2.imread('C:\\Users\\gopik\\Desktop\\RVCE_map.jpg', 1)
    img1 = img.copy()
    img2 = img.copy()
    img3 = img.copy()
    img4 = img.copy()
    temp = img.copy()
    height, width = img.shape[:2]
    h,w = int(height/2), int(width/2)

    img1[:h,:w, 0] = 127
    img1[:h,:w, 1] = 127

    img2[h+1:,:w, 0] = 127
    img2[h+1:,:w, 1] = 127

    img3[:h,w+1:, 0] = 127
    img3[:h,w+1:, 1] = 127

    img4[h+1:,w+1:, 0] = 127
    img4[h+1:,w+1:, 1] = 127

    imgs = [img1, img2, img3,img4]
    for i in x:
        temp = cv2.addWeighted(temp, x[i], imgs[i-1], 1-x[i], 0)
        # cv2.imshow('image', temp)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    cv2.imwrite(filename, temp)

x = {1:0.2, 2:0.3, 3:0.7, 4:0.8}
lap(x)
