import ast
import collections
import cv2
import numpy as np
import os.path
import pickle
import copy
import math



def main():
    
    # 2. 이미지에서 패턴 인식
    test_img = cv2.imread('test_img.png', cv2.IMREAD_GRAYSCALE)

    if test_img is None:
        print('Image load failed')
        return

    _, src_bin = cv2.threshold(test_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
    test_img_dst = cv2.cvtColor(test_img, cv2.COLOR_GRAY2BGR)

    final_dots_count = 0    
    pts_list = []

    for i in range(1, cnt) :
        (x, y, w, h, area) = stats[i]

        if area <20:
            continue

        final_dots_count+=1

        pt1 = (x,y)
        pt2 = (x+w, y+h)
        center_p = (x+w//2, y+h//2)

        pts_list.append(center_p)

        cv2.rectangle(test_img_dst, pt1, pt2, (0, 255, 0), 1)

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        # cv2.putText(test_img_dst, str(final_dots_count), pt1, font, .3, (255, 255, 255))
        cv2.circle(test_img_dst, center_p, 1, (255,0,0))

    print('인식된 패턴 갯수 : {:d}'.format(final_dots_count))


    # 3. 마스터 패턴과의 차이 비교

    ## 마스터 패턴 중심 좌표 만들기
    with open('pts_stats.txt', 'rb') as f:
        data_str = f.readlines()[0].decode()
        data = np.array(ast.literal_eval(data_str))

    master_pattern_centroids = []

    for i in data:
        center_p = (i[0]+i[2]//2, i[1]+i[2]//2)
        master_pattern_centroids.append(center_p)    

    ## 테스트 이미지에 올려서 비교
    for center_p in master_pattern_centroids:
        cv2.circle(test_img_dst, center_p, 1, (0,0,255), -1)


    pts_list_temp = copy.deepcopy(pts_list)

    ## 가장 가까운 점 찾아서 거리 구하기
    # min_distance = 0
    # min_pts = ()

    for count, point in enumerate(master_pattern_centroids):
        p1_x, p1_y = point
        
        min_distance = 0
        min_pts = (0,0)

        for i, temp in enumerate(pts_list_temp):
            p2_x, p2_y = temp

            a = p2_x - p1_x
            b = p2_y - p1_y

            c = math.sqrt((a*a) + (b*b))

            if i == 0:
                min_distance = abs(c)
                min_pts = temp

            if min_distance > abs(c):
                min_distance = abs(c)
                min_pts = temp
        
        cv2.putText(test_img_dst, str(count+1), min_pts, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, .3, (255, 255, 255))

        print(min_distance)
        print(min_pts)    

    
     # 잘 보이게 사이즈 3배 확대
    rows, cols, _ = test_img_dst.shape
    resize_dump_img = cv2.resize(test_img_dst, dsize=(cols * 3, rows*3), interpolation=cv2.INTER_AREA)

    cv2.imwrite('result.png', resize_dump_img)
    cv2.imshow('dst', resize_dump_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
