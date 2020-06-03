import ast
import cv2
import numpy as np
import os.path
import pickle

def obtain_master_position(filename, filetype):

    with open(filename+'.'+filetype, 'rb') as f:
        if (filetype == 'pickle'):
            data = np.array(pickle.load(f))
        else:
            data_str = f.readlines()[0].decode()
            data = np.array(ast.literal_eval(data_str))

    return data

def draw_patterns(filename, pallete, pts):

    width = np.bincount(pts[:,2]).argmax()

    for i in pts:
        x, y = i[0], i[1]

        pt1 = (x, y)
        pt2 = (x+width, y+width)
        cv2.rectangle(pallete, pt1, pt2, (255, 255, 255), -1)

    cv2.imwrite(filename, pallete)

    if os.path.isfile(file):
        return filename
    else:
        return None    

def resize_image(pallete):

    return pallete

def find_patterns_by_clustering(img):

    dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    _, src_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)   
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

    observed_data = []
    final_dots_count = 0

    for i in range(1, cnt) :
        (x, y, w, h, area) = stats[i]
        if area <20:
            continue

        final_dots_count+=1
        observed_data.append([x,y,w,h])
        cv2.rectangle(dst, (x,y), (x+w, y+h), (0, 255, 0), 1)

    return observed_data, dst

def main():

    # variable
    observed_pts = []

    # Obtain master position
    # data = obtain_master_position('pts_stats', 'txt')
    # img = np.zeros((174, 471, 1))

    test_data = obtain_master_position('pts_stats_2', 'txt')
    test_img = np.zeros((174, 471, 1))

    # draw rectangle patterns
    filename_img_test = draw_patterns('result_image_for_test.png', test_img, test_data)

    # Obtain resulting image
    src = cv2.imread(filename_img, cv2.IMREAD_GRAYSCALE)
    src_test = cv2.imread(filename_img_test, cv2.IMREAD_GRAYSCALE)

    # find patterns by using binary data clustering
    observed_data, result = find_patterns_by_clustering(src)
    
    
    # resize image for human
    rows, cols, _ = result.shape
    res_resize = cv2.resize(result, dsize=(cols * 3, rows*3), interpolation=cv2.INTER_AREA)

    cv2.imshow("image", res_resize)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
