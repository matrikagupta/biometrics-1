Webcam Face Capturer
====================
Face Recognition System consists of:
1) Video Image Streamer
2) Image Post Processing
3) Training Mode
(Takes multiple pictures)
4) Image Pre-Processor
5) Vector Formation
6) Face Detection
7) Eigen Vectors
8) Second level Face face size Detection
9) Image Signature
10) Adding padding to captured frame to get around 100px from all sides of frame
11) Training Set Mean Weight.
12) Testing Mode (Take one testing  picture)
13) Matching Code for Face Recognition (Using Threshold Level)
14) Authenticated / Unauthenticated

                ******************************************************************
                ******************************************************************
Requirements:
-------------
*********************************
Steps to install opencv on XOS.
*********************************

There is a simpler way to do it using Homebrew.
  1) Homebrew is a package manager for Mac OS X, more info can be found on their website.
  Installing brew is simpler than you think, just run this in terminal:
  $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
 
  2) You might need to install Python first:
  $ brew install python

  3) Add OpenCV using the following commands:
  $ brew tap homebrew/science

Install OpenCV:
  $ brew install opencv

  Your OpenCV installation will be located at: /usr/local/Cellar/opencv/2.4.10/

Python setup
The final part is to setup Python, use the following:
  $ cat ~/.bash_profile | grep PYTHONPATH
  $ ln -s /usr/local/Cellar/opencv/2.4.10/lib/python2.7/site-packages/cv.py cv.py
  $ ln -s /usr/local/Cellar/opencv/2.4.10/lib/python2.7/site-packages/cv2.so cv2.so

That’s it! If you have issue with Python when running some OpenCV samples, you need to make sure that you have numpy & matplotlib installed. You can do this using brew, in terminal enter:
  $ pip install numpy
  $ pip install matplotlib

Reference link:
https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/
http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/

*********************************
Installing in Linux (Ubuntu)
*********************************
Please use following links:

Use https://help.ubuntu.com/community/OpenCV
http://www.samontab.com/web/2014/06/installing-opencv-2-4-9-in-ubuntu-14-04-lts/


                ******************************************************************
                ******************************************************************


Run the program like this:
-------------------------
python webcam.py "haar-cassacde-face-default-xml-location" "username" "test/train"
Eg: python webcam.py haarcascade_frontalface_default.xml ravish test
Parameters:
1) Location for haar casscade xml file.
2) username to enter/search.
3) mode: test/train model.

This part of code uses opencv to capture image samples.

git commit -m "Issue  by matrikagupta, ravyg: Main code training model."

NOTE: opencv and numpy for python is a requirments for this part for code to run.


