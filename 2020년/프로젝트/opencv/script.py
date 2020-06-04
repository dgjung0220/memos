import ast
import cv2
import numpy as np
import os.path
import pickle

if __name__ == "__main__":

    # 1. 인식할 이미지 만들기
    test_img = np.zeros((174, 471, 1))

    with open('pts_stats_2.txt', 'rb') as f:
        data = f.readlines()[0].decode()
        test_data = np.array(ast.literal_eval(data))

    width = np.bincount(test_data[:,2]).argmax()

    for i in test_data:
        x, y = i[0], i[1]

        pt1 = (x, y)
        pt2 = (x+width, y+width)
        cv2.rectangle(test_img, pt1, pt2, (255, 255, 255), -1)

    cv2.imwrite('test_img.png', test_img)

    if os.path.isfile('test_img.png'):
        print('test image make success!')
    else:
        print('retry')
