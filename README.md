# Hand Scroll Controller

This project is a Python-based application that uses a webcam to detect hand gestures and perform scrolling actions on the computer. It uses **MediaPipe** for hand detection and **PyAutoGUI** for scrolling. The number of raised fingers determines the scrolling direction.

---

## Features
- Detects hand landmarks using MediaPipe.
- Counts the number of raised fingers.
- Performs scrolling actions:
  - **One raised finger**: Scroll down.
  - **Two raised fingers**: Scroll up.

---

## Requirements

### Hardware
- A computer with a webcam.

### Software
- Python 3.7 or higher.
- The following Python packages:
  - OpenCV (`cv2`)
  - MediaPipe (`mediapipe`)
  - PyAutoGUI (`pyautogui`)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hand-scroll-controller.git
   cd hand-scroll-controller
   ```

2. **Install dependencies**:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

---

## Usage

1. Run the script:
   ```bash
   python hand_scroll_controller.py
   ```

2. Make gestures in front of the webcam:
   - **One finger raised**: Scroll down.
   - **Two fingers raised**: Scroll up.

3. Press **'q'** to quit the application.

---

## How It Works
1. The script captures webcam video using OpenCV.
2. MediaPipe processes the video to detect hand landmarks.
3. The number of raised fingers is counted based on the relative position of finger tips and their base joints.
4. Depending on the count:
   - Scrolling down occurs when one finger is raised.
   - Scrolling up occurs when two fingers are raised.
5. PyAutoGUI executes the scroll commands.

---

## Customization

You can modify the scroll sensitivity by changing the `scroll_amount` variable in the script:
```python
scroll_amount = 70
```

---

## Limitations
- Works best in well-lit environments.
- May not perform accurately if hands are partially obscured or if there is excessive motion blur.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

---


## Acknowledgments
- [MediaPipe](https://mediapipe.dev) for hand detection.
- [PyAutoGUI](https://pyautogui.readthedocs.io) for GUI automation.
- OpenCV for real-time video processing.

---

## Author
Anunaya R Pillai

Happy scrolling! 😊
