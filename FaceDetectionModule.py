import cv2
import mediapipe as mp
import time
import tkinter as tk


def get_screen_size():
    root = tk.Tk()
    root.withdraw()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height


class FaceDetection:
    def __init__(self, camera_index=0, video_path=None, min_detection_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence

        if video_path:
            self.cap = cv2.VideoCapture(video_path)
        else:
            self.cap = cv2.VideoCapture(camera_index)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        self.mpFaceDetection = mp.solutions.face_detection
        self.faceDetection = self.mpFaceDetection.FaceDetection(min_detection_confidence=self.min_detection_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.pTime = 0
        self.results = None

    def process_frame(self):
        success, img = self.cap.read()
        if not success:
            return None

        #Resize to fit screen
        screen_w, screen_h = get_screen_size()
        h, w = img.shape[:2]
        scale = min(screen_w / w, screen_h / h)
        new_w, new_h = int(w * scale), int(h * scale)
        img = cv2.resize(img, (new_w, new_h))

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        faces = self.findFaces(img, draw=True)

        cTime = time.time()
        fps = 1 / (cTime - self.pTime) if (cTime - self.pTime) != 0 else 0
        self.pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        return img, faces

    def findFaces(self, img, draw=True):
        """
        Returns a list of (id, x, y, w, h, score) for each detected face.
        """
        faces = []
        if self.results and self.results.detections:
            ih, iw, _ = img.shape
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                score = detection.score[0]
                faces.append((id, x, y, w, h, score))
                if draw:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                    cv2.putText(img, f'{int(score * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        return faces

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    face_detection = FaceDetection(video_path="FaceVideos/5.mp4")
    try:
        while True:
            img, faces = face_detection.process_frame()
            if img is None:
                break

            #Example: print face bounding boxes and scores
            for face in faces:
                print(f"Face {face[0]}: x={face[1]}, y={face[2]}, w={face[3]}, h={face[4]}, score={face[5]:.2f}")

            cv2.imshow("Face Detection", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        face_detection.release()


if __name__ == "__main__":
    main()