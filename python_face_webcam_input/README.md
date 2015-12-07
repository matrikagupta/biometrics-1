Webcam Face Capturer
====================

Run the program like this:
python webcam.py "haar-cassacde-face-default-xml-location" "username" "test/train"
Eg: python webcam.py haarcascade_frontalface_default.xml ravish test
Parameters:
1) Location for haar casscade xml file.
2) username to enter/search.
3) mode: test/train model.

This part of code uses opencv to capture image samples.

git commit -m "Issue  by matrikagupta, ravyg: Main code training model."

NOTE: opencv and numpy for python is a requirments for this part for code to run.