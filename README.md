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

![Face Detection Screenshot](https://github.com/PrabeshPathak2002/Face-Detection-using-opencv-and-Mediapipe/blob/main/Screenshot.png "Screenshot")

