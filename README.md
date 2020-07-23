# OpenCVProject1
 This simple yet cool script uses OpenCV's color detection capabilities to track movement of colored markers and draws them on screen.
 Multiple markers can be used at once.
 
# Screenshots
<img src="https://raw.githubusercontent.com/Tavishi123-singh/OpenCV_VirtualPaint/master/Screenshot%20(396).png">

# Getting Started
1. Clone this repo.
1. Make sure `python` is installed.
1. Open Project in an IDE (`Pycharm` Recommended)
1. Make sure to configure the python interpreter.
1. Also download and add two modules : `opencv` and `numpy` to the project.
1. Run the `Project1.py` file.

# Adding Custom Colors
1. Run the `Resources/ColorPicker.py` file to precisely find out the HSV color ranges for you desired marker.
1. Adjust the values until you can only see the marker and its stable during movement.
1. Note down the newly generated values and add them as a `new list` into the `myColors` list in the `Project1.py` file.
1. The sequence is : first the three lower hsv values then the next three upper hsv values.
