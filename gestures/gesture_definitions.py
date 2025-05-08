def detect_gesture(landmarks, image_shape):
    """Detect hand gestures based on landmark positions.

    Args:
        landmarks: List of (x, y) tuples for hand landmarks from HandDetector.
        image_shape: Tuple of (height, width, channels) for the input image.

    Returns:
        str or None: Name of detected gesture or None if no gesture is detected.
    """
    h, w, _ = image_shape
    thumb_tip = landmarks[4]   # Thumb tip
    index_tip = landmarks[8]   # Index finger tip
    middle_tip = landmarks[12] # Middle finger tip
    ring_tip = landmarks[16]   # Ring finger tip
    pinky_tip = landmarks[20]  # Pinky finger tip
    wrist = landmarks[0]       # Wrist

    # Helper: Check if finger is extended (higher than its base)
    def is_finger_extended(tip, base_idx):
        base = landmarks[base_idx]
        return tip[1] < base[1] - 50  # y-coordinate check (inverted)

    # Thumbs up: Thumb extended up, other fingers folded
    if (thumb_tip[1] < wrist[1] - 100 and
        not is_finger_extended(index_tip, 5) and
        not is_finger_extended(middle_tip, 9)):
        return "thumbs_up"

    # Thumbs down: Thumb extended down, other fingers folded
    if (thumb_tip[1] > wrist[1] + 100 and
        not is_finger_extended(index_tip, 5) and
        not is_finger_extended(middle_tip, 9)):
        return "thumbs_down"

    # Peace sign: Index and middle fingers extended, others folded
    if (is_finger_extended(index_tip, 5) and
        is_finger_extended(middle_tip, 9) and
        not is_finger_extended(ring_tip, 13) and
        not is_finger_extended(pinky_tip, 17)):
        return "peace_sign"

    # Fist: No fingers extended
    if (not is_finger_extended(index_tip, 5) and
        not is_finger_extended(middle_tip, 9) and
        not is_finger_extended(ring_tip, 13) and
        not is_finger_extended(pinky_tip, 17)):
        return "fist"

    # Open palm: All fingers extended
    if (is_finger_extended(index_tip, 5) and
        is_finger_extended(middle_tip, 9) and
        is_finger_extended(ring_tip, 13) and
        is_finger_extended(pinky_tip, 17)):
        return "open_palm"

    # Rock sign: Index and pinky extended, others folded
    if (is_finger_extended(index_tip, 5) and
        is_finger_extended(pinky_tip, 17) and
        not is_finger_extended(middle_tip, 9) and
        not is_finger_extended(ring_tip, 13)):
        return "rock_sign"

    return None