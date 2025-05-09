import cv2
import mediapipe as mp

# Initialize MediaPipe Hands solution for hand detection and tracking
mp_hands = mp.solutions.hands
# Initialize MediaPipe drawing utilities for rendering hand landmarks
mp_drawing = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, max_hands=2, detection_confidence=0.7, tracking_confidence=0.7):
        """
        Initialize the HandDetector with MediaPipe Hands configuration.

        Args:
            max_hands (int): Maximum number of hands to detect (default: 2).
            detection_confidence (float): Minimum confidence for hand detection (default: 0.7).
            tracking_confidence (float): Minimum confidence for hand tracking (default: 0.7).
        """
        # Create MediaPipe Hands instance with specified parameters
        self.hands = mp_hands.Hands(
            static_image_mode=False,  # Continuous video mode (not single images)
            max_num_hands=max_hands,  # Limit number of detectable hands
            min_detection_confidence=detection_confidence,  # Threshold for initial detection
            min_tracking_confidence=tracking_confidence,  # Threshold for tracking existing hands
        )
        # Store drawing utilities for rendering landmarks
        self.drawing = mp_drawing

    def detect_hands(self, image):
        """
        Detect hands in the input image using MediaPipe Hands.

        Args:
            image: Input image (BGR format) from OpenCV.

        Returns:
            results: MediaPipe results object containing detected hand landmarks.
        """
        # Convert BGR image to RGB, as MediaPipe requires RGB input
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Process the image to detect hands and return results
        results = self.hands.process(image_rgb)
        return results

    def draw_landmarks(self, image, results):
        """
        Draw hand landmarks and connections on the input image.

        Args:
            image: Input image (BGR format) to draw on.
            results: MediaPipe results object containing detected hand landmarks.

        Returns:
            image: Image with drawn landmarks and connections.
        """
        # Check if any hand landmarks were detected
        if results.multi_hand_landmarks:
            # Iterate through each detected hand
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections using MediaPipe drawing utilities
                self.drawing.draw_landmarks(
                    image,  # Target image to draw on
                    hand_landmarks,  # Landmark coordinates for one hand
                    mp_hands.HAND_CONNECTIONS  # Predefined connections between landmarks
                )
        return image

    def extract_landmark_positions(self, image, hand_landmarks):
        """
        Extract pixel coordinates of hand landmarks from MediaPipe results.

        Args:
            image: Input image (BGR format) to determine dimensions.
            hand_landmarks: MediaPipe hand landmarks for a single hand.

        Returns:
            landmarks: List of (x, y) tuples representing landmark positions in pixels.
        """
        # Get image dimensions (height, width)
        h, w, _ = image.shape
        landmarks = []
        # Iterate through each landmark in the hand
        for lm in hand_landmarks.landmark:
            # Convert normalized coordinates (0 to 1) to pixel coordinates
            landmarks.append((int(lm.x * w), int(lm.y * h)))
        return landmarks