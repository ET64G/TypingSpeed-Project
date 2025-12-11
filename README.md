# Typing Speed Test Desktop Application

A desktop application built with Tkinter and Python that assesses your typing speed with WPM (Words Per Minute) calculation, accuracy tracking, and support for both fixed-time and fixed-text test modes.

## Features

- **Two Test Modes:**
  - Fixed Time: Type for a specified duration (default 60 seconds)
  - Fixed Text: Complete a full text passage

- **Real-time Statistics:**
  - Words Per Minute (WPM) calculation
  - Accuracy percentage
  - Character count
  - Timer display

- **Visual Feedback:**
  - Color-coded text display (green for correct, red for incorrect)
  - Current position indicator

## Requirements

- Python 3.7 or higher
- tkinter (included with Python)

## Installation

1. Clone or download this repository
2. Ensure Python 3.7+ is installed
3. No additional packages need to be installed

## Usage

Run the application:

```bash
python typing_test_app.py
```

1. Select your preferred test mode (Fixed Time or Fixed Text)
2. Click "Start" to begin the test
3. Type the displayed text as accurately as possible
4. View your results when the test completes
5. Click "Reset" to start a new test

## Project Structure

```
├── typing_test_app.py      # Main application
├── test_controller.py       # Test logic and calculations
├── text_generator.py        # Sample text provider
├── results_window.py        # Results display
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## License

This project is open source and available for personal and educational use.

