"A real-time Virtual Paint application built with Python and OpenCV. By tracking a specific color (Blue) through a webcam, users can draw on their screen in mid-air and clear the canvas with a single keystroke."

2. Key Features
Real-time Tracking: Uses HSV color filtering and Contours for low-latency tracking.

Persistent Canvas: Uses a separate NumPy array to store drawings so they don't disappear.

Full-Screen Mode: Immersive drawing experience.

Controls: Press 'c' to clear the canvas and 'q' to quit.

3. Technologies Used
Python 3.x

OpenCV: For image processing and webcam handling.

NumPy: For canvas creation and mathematical operations.
