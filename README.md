# Drowsiness-detection-2.0

# Description

The Driver Drowsiness and Uneasiness Detection System is designed to enhance road safety by using Computer Vision to alert drivers when they show signs of drowsiness or cases of severe medical emergencies like stroke, etc. This is done using dlib, a cross-platform software library, that uses pre-trained facial landmark detectors to estimate the location of 68 coordinates that map facial structures to draw predictions.

Beeping noise is produced to alert the driver if he/she is found to be drowsy or inactive for more than 3 seconds. A switch is provided that is to be turned off manually to stop the beep alert signal. In case of a medical condition, for example stroke, the driver becomes unconscious, the beeping of signal continues and an emergency help signal is sent to ambulance and other rescuing teams. The tail lights of car turns on and an alert signal is sent in all directions to alert the drivers against a possible road accident and take necessary precautions.

# Table of Content

- [Libraries used](https://github.com/gjyotk/Drowsiness-detection-2.0/edit/main/README.md#libraries-used)
- [Approach](https://github.com/gjyotk/Drowsiness-detection-2.0/edit/main/README.md#approach)
- [Output images](https://github.com/gjyotk/Drowsiness-detection-2.0/edit/main/README.md#approach)
- [Model scores](https://github.com/gjyotk/Drowsiness-detection-2.0/edit/main/README.md#approach)
- [Future Scope](https://github.com/gjyotk/Drowsiness-detection-2.0/edit/main/README.md#approach)
- [Credits](https://github.com/gjyotk/Drowsiness-detection-2.0/edit/main/README.md#approach)




# Libraries Used

- dlib: A versatile library with a wide range of features, and it is often used in various applications, including facial recognition, object detection, image processing, and more. Dlib is particularly well-known for its robust facial landmarks detection and shape prediction capabilities.

- scipy.spatial: a subpackage of the SciPy library. It provides various functions and classes for working with spatial data and performing spatial computations.

- imutils: It provides a collection of convenience functions and utilities to perform various image processing operations, such as resizing, rotating, displaying, and working with OpenCV.

- numpy: It provides support for working with large, multi-dimensional arrays and matrices, as well as a collection of mathematical functions to operate on these arrays.

- argparse:  It simplifies the process of creating command-line interfaces for Python scripts or applications.

- imutils: Itmakes it easier to work with images and video streams in computer vision and image processing.

- time: It provides various functions for working with time, including measuring time intervals, formatting time and dates, and performing various time-related calculations.

# Approach

<img src= "https://github.com/gjyotk/Drowsiness-detection-2.0/assets/112189682/f3f1ef98-7808-4bd8-b497-a11ba1fc48be"  width= "700" height= "350">

  
# Output Images
<img src="https://github.com/gjyotk/Drowsiness-detection-2.0/assets/112189682/ffbe9f0f-584d-4629-aeb7-5d9f4b073237" width= "650" height= "350">



<img src="https://github.com/gjyotk/Drowsiness-detection-2.0/assets/112189682/43867719-aea4-4c48-9a39-ba1eb02711d0"  width= "650" height= "350">


# Model Score



# Future Scope

-  Implementation acn be done on a kernel level thread. This will increase the processing speed drastically which will be helpful to prevent life-threatening situations. It will result in a faster and more efficient deployment of the algorithm, reduce processing power required and the time taken to analyse the data.

- Work can be done on model using data with drivers wearing spectacles/ glasses.



# Credits

gurojaschadha Palak-Kaushik gjyotk





