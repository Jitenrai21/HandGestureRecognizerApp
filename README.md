# HandGestureRecognizerApp 🤝📸

A Python-based gesture recognition system for controlling system actions via webcam.

---

## 👋 Welcome

Welcome to **HandGestureRecognizerApp**!  
This Python project lets you control your computer using hand gestures captured via a webcam. Built with **OpenCV** and **MediaPipe**, it’s a fun way to:

- Adjust volume  
- Take screenshots  
- Open a browser  
- Mute your system  

All with a wave of your hand! 🚀

---

## 🌟 What It Does

### 🤖 Recognize Gestures:
Detects the following hand gestures:

- **👍 Thumbs Up** – Increase volume  
- **👎 Thumbs Down** – Decrease volume  
- **✌️ Peace Sign** – Open a browser  
- **✊ Fist** – Toggle mute/unmute  
- **🖐️ Open Palm** – Display greeting message  
- **🤘 Rock Sign** – Take a screenshot  

### 📺 Show Feedback:
- Gesture name overlay  
- Visual progress bar for gesture detection  
- Status messages for system actions  

### 🔧 Customizable:
All gesture-to-action mappings are defined in `gesture_config.json`. Easily modify or add gestures and actions!

---

## 📂 Project Layout

```

HandGestureRecognizerApp/
├── env/                    # 🌐 Virtual environment
├── utils/                  # 🛠️ Helper scripts
│   ├── hand_utils.py       # 🖐️ Hand detection
│   └── system_actions.py   # 🎮 System actions
├── gestures/               # 🤲 Gesture logic
│   └── gesture_definitions.py
├── config/                 # ⚙️ Settings
│   └── gesture_config.json
├── test/                   # 🧪 Unit tests
│   ├── hand_utils_test.py
│   └── gesture_recognition_test.py
├── screenshots/            # 📸 Screenshot storage
├── main.py                 # 🚀 Main application
├── requirements.txt        # 📋 Dependencies
├── README.md               # 📖 This file

````

---

## 🛠️ Getting Started

### 📋 Prerequisites

- Python 3.8+  
- Webcam  

### 🧱 Required Packages

- `opencv-python`  
- `mediapipe`  
- `pyautogui`  
- `pycaw`  
- `comtypes`

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jitenrai21/HandGestureRecognizerApp.git
cd HandGestureRecognizerApp
````

### 2. Set Up Virtual Environment

```bash
python -m venv env
```

**Activate Virtual Environment**

* **Windows:**

```bash
.\env\Scripts\activate
```

* **macOS/Linux:**

```bash
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

---

## 🎮 How to Use

* Perform a gesture and **hold for \~0.5 seconds** to trigger the action.
* Press `q` to exit the application.

### ✋ Supported Gestures:

| Gesture        | Action             |
| -------------- | ------------------ |
| 👍 Thumbs Up   | Increase Volume    |
| 👎 Thumbs Down | Decrease Volume    |
| ✌️ Peace Sign  | Open Browser       |
| ✊ Fist         | Mute/Unmute        |
| 🖐️ Open Palm  | Show Greeting (5s) |
| 🤘 Rock Sign   | Save Screenshot    |

### 📊 On-Screen Feedback:

* Gesture name displayed at the top
* Progress bar shows gesture hold duration
* Temporary messages for volume, mute, and greetings

---

## 🧩 Customize It

* **Add New Gestures:**
  Modify `gestures/gesture_definitions.py` and `config/gesture_config.json`

* **Change Actions:**
  Edit `utils/system_actions.py` to redefine behavior

* **Timing Configs:**
  Adjust `debounce_interval` or `greet_duration` in `main.py`

---

## 🐞 Troubleshooting

* **Webcam Not Working?**
  Ensure it's connected. Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` in `main.py`

* **Dependencies Issue?**
  Make sure you’re in the virtual environment when running `pip install`

* **Gestures Not Detected?**
  Improve lighting or adjust detection thresholds in `gesture_definitions.py`

---

## 🤝 Contribute

Want to improve this app? Here’s how:

```bash
# Fork the repo
# Create a new branch
git checkout -b feature/your-feature-name

# Commit your changes
git commit -m "Add new feature"

# Push to GitHub
git push origin feature/your-feature-name

# Open a Pull Request 🚀
```

---

## 🙏 Acknowledgments

* **MediaPipe** – For hand tracking
* **OpenCV** – For real-time computer vision
* **You** – For checking out this project! ❤️

---

Built by **[Jitenrai21](https://github.com/Jitenrai21)**
**Happy gesturing! 🎉**

```
