import cv2
from deepface import DeepFace
import threading

print("🧠 Loading DeepFace model... (this may take 1–2 min)")
model = DeepFace.build_model("VGG-Face")
print("✅ Model loaded successfully!")


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

emotion_result = "Detecting..."
lock = threading.Lock()

def analyze_frame(frame):
    global emotion_result
    try:
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend='retinaface'
        )
        with lock:
            emotion_result = result[0]['dominant_emotion']
    except Exception:
        pass

counter = 0
print("🎥 Running emotion detection — press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Camera not accessible.")
        break


    if counter % 10 == 0:
        threading.Thread(target=analyze_frame, args=(frame.copy(),), daemon=True).start()
    counter += 1

  
    with lock:
        cv2.putText(frame, f"Emotion: {emotion_result.upper()}",
                    (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Real-Time Emotion Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Exiting gracefully...")
        break

cap.release()
cv2.destroyAllWindows()
