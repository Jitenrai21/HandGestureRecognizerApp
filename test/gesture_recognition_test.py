import cv2
import sys
import os
from datetime import datetime
import numpy as np
import logging

# Suppress MediaPipe warnings
logging.getLogger('mediapipe').setLevel(logging.ERROR)

# Adjust sys.path to import from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.hand_utils import HandDetector
from utils.system_actions import volume_up, volume_down, open_browser, mute, greet, screenshot
from gestures.gesture_definitions import detect_gesture

# Gesture-to-action mapping from provided JSON
GESTURE_ACTIONS = {
    "thumbs_up": volume_up,
    "thumbs_down": volume_down,
    "peace_sign": open_browser,
    "fist": mute,
    "open_palm": greet,
    "rock_sign": screenshot
}

def display_greeting(frame, message="Hello! Nice to see you!"):
    """Display greeting message on frame if frame is valid."""
    if frame is not None and isinstance(frame, np.ndarray):
        cv2.putText(frame, message, (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3, cv2.LINE_AA)
    return frame

def main():
    # Initialize webcam and hand detector
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    detector = HandDetector(max_hands=1)

    # Debounce and stability logic
    last_action_time = datetime.now()
    debounce_interval = 5.0  # Seconds between actions
    last_gesture = None
    current_gesture = None
    gesture_frame_count = 0
    required_frames = 15  # Approx 0.5 seconds at 30 FPS
    greet_start_time = None
    greet_duration = 5.0  # Seconds to display greeting

    while cap.isOpened():
        try:
            ret, frame = cap.read()
            if not ret or frame is None:
                print("Error: Failed to capture frame from webcam")
                break
            frame = cv2.flip(frame, 1)  # Mirror frame for intuitive interaction

            # Check if greeting should be displayed
            if greet_start_time is not None:
                time_since_greet = (datetime.now() - greet_start_time).total_seconds()
                if time_since_greet < greet_duration:
                    frame = display_greeting(frame)
                else:
                    greet_start_time = None

            # Detect hands
            results = detector.detect_hands(frame)
            frame = detector.draw_landmarks(frame, results)

            # Process gestures
            detected_gesture = None
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    landmarks = detector.extract_landmark_positions(frame, hand_landmarks)
                    detected_gesture = detect_gesture(landmarks, frame.shape)

            # Gesture stability tracking
            if detected_gesture:
                if detected_gesture == current_gesture:
                    gesture_frame_count += 1
                else:
                    current_gesture = detected_gesture
                    gesture_frame_count = 1

                # Display gesture name and confirmation progress
                if isinstance(frame, np.ndarray):
                    cv2.putText(frame, f"Gesture: {detected_gesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 255, 0), 2, cv2.LINE_AA)

                # Execute action if gesture is stable and debounce allows
                if gesture_frame_count >= required_frames:
                    current_time = datetime.now()
                    time_since_last = (current_time - last_action_time).total_seconds()
                    if (detected_gesture != last_gesture or time_since_last > debounce_interval):
                        action = GESTURE_ACTIONS.get(detected_gesture)
                        if action:
                            if action == greet and greet_start_time is None:
                                frame = action(frame)
                                greet_start_time = datetime.now()
                            else:
                                action()  # Other actions
                            last_action_time = current_time
                            last_gesture = detected_gesture
                            gesture_frame_count = 0  # Reset after action
                            current_gesture = None

            else:
                # Reset stability tracking if no gesture detected
                current_gesture = None
                gesture_frame_count = 0

            # Display frame if valid
            if frame is not None and isinstance(frame, np.ndarray):
                cv2.imshow("Gesture Recognition Test", frame)
            else:
                print("Error: Invalid frame for display")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(f"Error in main loop: {e}")
            continue

    cap.release()
    cv2.destroyAllWindows()
    detector.hands.close()

if __name__ == "__main__":
    main()