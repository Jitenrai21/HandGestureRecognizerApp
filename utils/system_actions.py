import os
import webbrowser
import pyautogui
import platform
import cv2
from datetime import datetime
import numpy as np

# Optional: for Windows volume control
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ImportError:
    AudioUtilities = None  # fallback if pycaw not available

def volume_up(step=0.1):
    """Increase system volume"""
    if AudioUtilities:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(min(current + step, 1.0), None)

def volume_down(step=0.1):
    """Decrease system volume"""
    if AudioUtilities:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(max(current - step, 0.0), None)

def open_browser(url="https://www.linkedin.com/in/jiten-rai-42b540264/"):
    """Open default web browser"""
    webbrowser.open(url)

def mute():
    """Toggle mute"""
    if platform.system() == "Windows":
        pyautogui.press("volumemute")
    else:
        print("Mute not implemented for this OS")

def greet(frame, message="Hello! Nice to see you!"):
    """Display greeting message on frame if frame is valid."""
    if frame is not None and isinstance(frame, np.ndarray):
        cv2.putText(frame, message, (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3, cv2.LINE_AA)
    return frame


def screenshot(subdir="screenshots"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    save_dir = os.path.join(base_dir, subdir)

    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Create a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    save_path = os.path.join(save_dir, filename)

    # Capture and save
    image = pyautogui.screenshot()
    image.save(save_path)

    print(f"📸 Screenshot saved to {save_path}")

def display_volume_feedback(frame, action):
    """Display volume feedback message on frame if frame is valid."""
    if frame is not None and isinstance(frame, np.ndarray):
        message = "Volume Up" if action == volume_up else "Volume Down"
        cv2.putText(frame, message, (50, 130), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3, cv2.LINE_AA)
    return frame