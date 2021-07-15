<img src="https://user-images.githubusercontent.com/49658988/125802715-0cba16b2-1bc1-479d-a9bd-1e963f9c8146.png" alt="logo-py-qt-yt" width="300" height="300"/>

# py-qt-youtube-downloader

Simple downloader, built with QtDesigner and Python

# How to launch using python

1. `pip install youtube-dl`
2. `pip install pyqt5-tools`
3. `git clone https://github.com/T-Damer/py-qt-youtube-downloader`
4. `cd py-qt-youtube-downloader`
5. `py main.py` OR `python3 main.py`

# How to edit interface?

1. Install [qt.designer](https://www.qt.io/download-qt-installer)
2. Open `YTWindow.ui`
3. Edit whatever you want (styles made with RMB on element -> stylesheet. Use CSS to edit)
4. Convert file to `.py` using `pyuic5 YTWindow.ui -o des.py`
   > Remember to install `pyuic` using `pip install pyuic5-tool` also you must `pip install pyqt5-tools`
