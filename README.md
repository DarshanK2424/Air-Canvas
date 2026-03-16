# 🎨 Virtual Paint using OpenCV

A real-time **Virtual Paint application** built with **Python and OpenCV**.
This project tracks a **blue colored object through a webcam** and allows users to draw on the screen by moving the object in the air.

The application detects the object's position using color tracking and converts its movement into drawing strokes in real time.

---

## 🚀 Features

* **Real-Time Color Tracking**
  Uses HSV color filtering and contour detection for fast and accurate object tracking.

* **Persistent Canvas**
  A separate NumPy canvas is used to store drawings so strokes remain visible on the screen.

* **Full-Screen Mode**
  Provides an immersive drawing experience.

* **Simple Controls**

  * Press **C** to clear the canvas
  * Press **Q** to quit the application

---

## 🛠 Technologies Used

* **Python 3.x**
* **OpenCV** – For image processing and webcam capture
* **NumPy** – For creating the drawing canvas and handling arrays

---

## ⚙️ How It Works

1. The webcam captures frames in real time.
2. Frames are converted from **BGR to HSV color space**.
3. A **color mask** detects the blue object.
4. **Contours are detected** to find the position of the object.
5. The object's movement is used to draw strokes on a virtual canvas.

---

## ▶️ How to Run

### 1. Install Required Libraries

pip install opencv-python numpy

### 2. Run the Program

python virtual_paint.py

### 3. Start Drawing

* Hold a **blue colored object** in front of the webcam.
* Move the object to **draw on the screen in mid-air**.

---

## 💡 Future Improvements

* Support for multiple colors
* Adjustable brush thickness
* Gesture-based controls
* Option to save drawings as images
