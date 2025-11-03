import cv2
from deepface import DeepFace

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analyze emotions in the frame
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Extract the dominant emotion
        emotion = result[0]['dominant_emotion']

        # Display the emotion on screen
        cv2.putText(frame, f'Emotion: {emotion}', (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    except Exception as e:
        print("Error:", e)

    cv2.imshow('Emotion Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
