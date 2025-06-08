import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
FaceDetection = mpFaceDetection.FaceDetection()
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = FaceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        
    ctime = time.time()
    fps = 1 / (ctime - pTime) if (ctime - pTime) != 0 else 0
    pTime = ctime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.VideoCapture(0).release()
cv2.destroyAllWindows()

