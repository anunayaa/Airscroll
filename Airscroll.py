import cv2
import pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


scroll_amount = 70


def count_raised_fingers(hand_landmarks):

    landmarks = hand_landmarks.landmark
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    thumb_base = landmarks[mp_hands.HandLandmark.THUMB_CMC]
    index_base = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_base = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_base = landmarks[mp_hands.HandLandmark.RING_FINGER_MCP]
    pinky_base = landmarks[mp_hands.HandLandmark.PINKY_MCP]

    raised_fingers = 0
    if index_tip.y < index_base.y:
        raised_fingers += 1
    if middle_tip.y < middle_base.y:
        raised_fingers += 1
    if ring_tip.y < ring_base.y:
        raised_fingers += 1
    if pinky_tip.y < pinky_base.y:
        raised_fingers += 1
    if thumb_tip.y < thumb_base.y:
        raised_fingers += 1

    return raised_fingers


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            raised_fingers = count_raised_fingers(hand_landmarks)

            if raised_fingers == 1:
                pyautogui.scroll(-scroll_amount)
            elif raised_fingers == 2:
                pyautogui.scroll(scroll_amount)
    cv2.imshow('Hand Scroll', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
