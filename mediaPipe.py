import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

text = "Not Detecting"
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    max_num_hands=6,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        if (hand_landmarks.landmark[8].y > hand_landmarks.landmark[5].y)\
          and (hand_landmarks.landmark[12].y > hand_landmarks.landmark[9].y)\
          and (hand_landmarks.landmark[16].y > hand_landmarks.landmark[13].y)\
          and (hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y):
          print("Rock")
          text = "Rock"
        elif (hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y)\
          and (hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y)\
          and (hand_landmarks.landmark[16].y > hand_landmarks.landmark[13].y)\
          and (hand_landmarks.landmark[20].y > hand_landmarks.landmark[17].y):
          print("Scissors")
          text = "Scissors"
        elif (hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y)\
          and (hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y)\
          and (hand_landmarks.landmark[16].y < hand_landmarks.landmark[13].y)\
          and (hand_landmarks.landmark[20].y < hand_landmarks.landmark[17].y):
          print("Paper")
          text = "Paper"
          
        # Draw the hand annotations on the image.
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (0, 25)
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    image = cv2.flip(cv2.resize(image, (800, 600)), 1)
    image = cv2.putText(image, text, org, font, fontScale, 
                    color, thickness, cv2.LINE_AA, False)
    cv2.imshow('MediaPipe Hands',image )
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()