#### calibration.py 소스 분석



​	calibration_camera 함수는 캘리브레이션 샘플 이미지를 이용하여 카메라를 캘리브레이션하고, .pickle 파일로 캘리브레이션 결과를 반환하는 함수이다.

```python
def calibrate_camera(nx, ny, basepath):
    """

    :param nx: number of grids in x axis
    :param ny: number of grids in y axis
    :param basepath: path contains the calibration images
    :return: write calibration file into basepath as calibration_pickle.p
    """
    
    objp = np.zeros((nx*ny,3), np.float32)
    objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)
    
    ...
```

``objp`` : 샘플 체스보드판의 각 그리드의 좌표를 저장할 배열. 

``objp = np.zeros((nx*ny,3), np.float32)`` : Grids (9, 6칸) 좌표 (x,y,z) 배열

``objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)`` : 각 좌표에 배열의 index 값 입력 (z=0 인 배열 index 좌표 집합

```python
 # Arrays to store object points and image points from all the images.
 objpoints = [] # 3d points in real world space
 imgpoints = [] # 2d points in image plane.

 # Make a list of calibration images
 images = glob.glob(path.join(basepath, 'calibration*.jpg'))
```

​	3D object 및 이미지 좌표가 저장될 배열을 선언하고, 샘플 캘리브레이션 이미지들을 glob 라이브러리를 이용하여 리스트로 불러온다. ``glob`` 은 많이 유용하니 항상 쓰는 버릇을 들이자.

```python
# Step through the list and search for chessboard corners
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx,ny),None)

    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (nx,ny), corners, ret)
        cv2.imshow('input image',img)
        cv2.waitKey(500)

cv2.destroyAllWindows()
```

​	opencv 내장함수가 없었다면 좀 복잡했겠지만 이해하기 쉽다. 불러 온 샘플 이미지들을 하나씩 불러와 opencv 함수인 ``findChessboardCorners`` 를 이용하여 코너점을 찾고, 찾은 좌표를 imgpoints 에 저장하고, ``drawChessboardCorners`` 함수를 이용하여 코너점을 표시하고 출력한다.

```python
 # calibrate the camera
 img_size = (img.shape[1], img.shape[0])
 ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)

 # Save the camera calibration result for later use (we don't use rvecs / tvecs)
 dist_pickle = {}
 dist_pickle["mtx"] = mtx
 dist_pickle["dist"] = dist
 destnation = path.join(basepath,'calibration_pickle.p')
 pickle.dump( dist_pickle, open( destnation, "wb" ) )
 print("calibration data is written into: {}".format(destnation))
```

​	opencv 내장함수인 calibrateCamera 를 이용한다. 이 함수는 캘리브레이션 결과(ret), 카메라 행렬(mtx), 왜곡 계수(dist), 회전과 이동벡터(rvecs, tvecs) 등을 반환한다. 자세한 함수 설명은 https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html 참고. 코드에서는 캘리브레이션의 결과인 행령과 왜곡 계수를 pickle로 저장한다.





