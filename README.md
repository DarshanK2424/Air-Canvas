Virtual Paint (OpenCV Project)

A real-time Virtual Paint application built using Python and OpenCV.
This project allows users to draw in the air using a colored object (Blue) detected through a webcam.

By tracking the colored object in real-time, the application converts its movement into digital strokes on the screen, creating an interactive drawing experience.

🚀 Features
🎯 Real-Time Color Tracking

Uses HSV color filtering and contour detection to track a specific color with low latency, enabling smooth drawing.

🖌 Persistent Canvas

A separate NumPy canvas array is used to store drawings so that strokes remain visible even when the tracked object moves away.

🖥 Full-Screen Drawing Mode

Provides an immersive full-screen drawing experience for better usability.

⌨ Simple Controls
Key	Action
C	Clear the canvas
Q	Quit the application
