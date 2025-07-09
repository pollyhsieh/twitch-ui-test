# Twitch UI Automation Test

This project contains automated UI tests for [Twitch mobile site](https://m.twitch.tv), built using **Selenium** and **Pytest**.

## 🧪 How to Run

```bash
# Set up environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run UI tests
pytest -m ui

## 🖥️ Demo (Test Running Locally)
Below is a demo showing Twitch UI tests running locally using Pytest + Selenium:

https://github.com/user-attachments/assets/83ab7a51-831c-4d6e-9ce2-3a004ac6481d


## 📁 Project Structure
tests/
├── ui_test/
│ └── test_twitch_ui.py
pages/
├── base_page.py
├── home_page.py
├── stream_page.py
utils/
├── logger.py
├── config.py
└── helpers.py
└── logging_decorator.py

## 🗂️ Notes
Logs and screenshots will be saved in the /logs folder
Requires Chrome and chromedriver installed
Mobile emulation is configured for Pixel 2


