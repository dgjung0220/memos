### C++
```c
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void labeling_stats();

int dilation_size = 2;

int main()
{
	labeling_stats();
	return 0;
}

void Dilation(int, void*) {

}

void labeling_stats()
{
	Mat src_dump = imread("test_image.png", IMREAD_GRAYSCALE);

	if (src_dump.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat src;
	resize(src_dump, src, Size(src_dump.cols*3, src_dump.rows*3), 0, 0, INTER_LINEAR);


	int dilation_type = MORPH_RECT;

	Mat dilation_dst;
	Mat element = getStructuringElement(dilation_type,
		Size(2 * dilation_size + 1, 2 * dilation_size + 1),
		Point(dilation_size, dilation_size));
	erode(src, dilation_dst, element);


	Mat bin;
	threshold(dilation_dst, bin, 0, 255, THRESH_BINARY | THRESH_OTSU);

	Mat labels, stats, centroids;
	int cnt = connectedComponentsWithStats(bin, labels, stats, centroids, 8);

	Mat dst;
	cvtColor(dilation_dst, dst, COLOR_GRAY2BGR);

	int final_dots_number = 0;
	for (int i = 1; i < cnt; i++) {
		int* p = stats.ptr<int>(i);
		Point2i center_p = centroids.at<Point2i>(i);

		if (p[4] < 20) continue;			// quality
		final_dots_number++;

		printf("%d번째 : %d %d %d %d %d \n", i, p[0], p[1], p[2], p[3], p[4]);
		rectangle(dst, Rect(p[0], p[1], p[2], p[3]), Scalar(0, 255, 0), 2);
		circle(dst, Point(p[0]+ (p[2]/2), p[1]+ (p[3]/2)), 4, Scalar(255, 0, 0), 1);
		putText(dst, to_string(final_dots_number), Point(p[0], p[1]), 1.5, 1.2, Scalar::all(255));
	}

	cout << "Dot pattern " << final_dots_number << endl;

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}
```

### python
```python
import numpy as np
import cv2
import copy

def labeling_stats():

    src_origin = cv2.imread('test_image.png', cv2.IMREAD_GRAYSCALE)

    if src_origin is None:
        print('Image load failed')
        return

    rows, cols = src_origin.shape
    src_resize = cv2.resize(src_origin, dsize=(cols * 3, rows*3), interpolation=cv2.INTER_AREA)
    
    src = cv2.erode(src_resize, np.ones((5,5), np.uint8), iterations=1)
    
    _, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)


    final_dots_count = 0    
    pts_list = []

    for i in range(1, cnt) :

        (x, y, w, h, area) = stats[i]

        if area <20:
            continue

        final_dots_count+=1

        pt1 = (x,y)
        pt2 = (x+w, y+h)
        center_p = (int(x+w/2), int(y+h/2))

        pts_list.append(center_p)

        cv2.rectangle(dst, pt1, pt2, (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(dst, str(final_dots_count), pt1, font, .7, (255, 255, 255))
        cv2.circle(dst, center_p, 3, (255,0,0))

        # print("{:d}번째 : {:d} {:d} {:d} {:d}".format(final_dots_count, x, y, w, h))


    cv2.line(dst, pts_list[0], pts_list[14], (255,0,0), 1)
    cv2.line(dst, pts_list[15], pts_list[29], (255,0,0), 1)
    cv2.line(dst, pts_list[30], pts_list[44], (255,0,0), 1)
    cv2.line(dst, pts_list[45], pts_list[59], (255,0,0), 1)
    cv2.line(dst, pts_list[60], pts_list[74], (255,0,0), 1)
    cv2.line(dst, pts_list[75], pts_list[89], (255,0,0), 1)
    cv2.line(dst, pts_list[90], pts_list[104], (255,0,0), 1)


    cv2.line(dst, pts_list[0], pts_list[90], (255,0,0), 1)
    cv2.line(dst, pts_list[1], pts_list[91], (255,0,0), 1)
    cv2.line(dst, pts_list[2], pts_list[92], (255,0,0), 1)
    cv2.line(dst, pts_list[3], pts_list[93], (255,0,0), 1)
    cv2.line(dst, pts_list[4], pts_list[94], (255,0,0), 1)
    cv2.line(dst, pts_list[5], pts_list[95], (255,0,0), 1)
    cv2.line(dst, pts_list[6], pts_list[96], (255,0,0), 1)
    cv2.line(dst, pts_list[7], pts_list[97], (255,0,0), 1)
    cv2.line(dst, pts_list[8], pts_list[98], (255,0,0), 1)
    cv2.line(dst, pts_list[9], pts_list[99], (255,0,0), 1)
    cv2.line(dst, pts_list[10], pts_list[100], (255,0,0), 1)
    cv2.line(dst, pts_list[11], pts_list[101], (255,0,0), 1)
    cv2.line(dst, pts_list[12], pts_list[102], (255,0,0), 1)
    cv2.line(dst, pts_list[13], pts_list[103], (255,0,0), 1)
    cv2.line(dst, pts_list[14], pts_list[104], (255,0,0), 1)

    # make chessboard
    # for c, pts in enumerate(dots_pts[0]):
    #     # print(pts, dots_pts[2][c])
        
    #     print(pts)
    #     print(dots_pts[1][c])
        
    #     # cv2.line(dst, pts, dots_pts[6][c], (255,0,0),10)
        
    #cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    labeling_stats()
```
