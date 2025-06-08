# Face Detection with OpenCV and Mediapipe

This project demonstrates real-time face detection using [OpenCV](https://opencv.org/) and [Mediapipe](https://mediapipe.dev/) in Python. It detects faces from your webcam feed or video files and can be easily extended for applications like attendance systems, emotion recognition, or interactive demos.

## Features

- Real-time face detection and bounding box drawing
- Configurable camera index or video file input
- FPS display on video feed
- Modular code with resource management

## Requirements

- Python 3.7+
- opencv-python
- mediapipe

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Usage

Run the main script:

```sh
python FaceDetectionModule.py
```

- Press `q` to quit the video window.
- The script prints the bounding box and confidence score for each detected face.

## Customization

- To use a different camera, change `camera_index` in `main()` or the class constructor.
- To use a video file, pass `video_path="your_video.mp4"` to the class.

## File Structure

- `FaceDetection.py` – Simple script for face detection.
- `FaceDetectionModule.py` – Modular, class-based version with more features.
- `requirements.txt` – Python dependencies.

## Screenshot
<!-- Replace the link below with your actual screenshot if available -->
![Face Detection Screenshot](https://github.com/PrabeshPathak2002/Face-Detection-using-opencv-and-Mediapipe/blob/main/screenshot.png "Screenshot")

## Face Detection Landmarks

<!-- Replace the link below with your actual face landmarks image if available -->
![Face Detection Landmarks](https://github.com/PrabeshPathak2002/Face-Detection-using-opencv-and-Mediapipe/blob/main/face-landmarks.png "Face Detection Landmarks")

## License

MIT License

---

```
MIT License

Copyright (c) 2025 Prabesh Pathak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
