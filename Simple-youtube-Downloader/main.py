# main module
from PyQt5.QtCore import Qt
import os
import threading
import time
from pytube import YouTube, Playlist
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QComboBox,
)

# resuluion = ["720", "Two", "Three", "Four"]
resuluion = ["720"]

# main app object
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Youtube Downloader")
# main_window.resize(400,100)

# app object
txt_box = QLineEdit()
dropdown = QComboBox()
title = QLabel("YT Downloader")
Status = QLabel("Update soon")

clear = QPushButton("Clear")
delete = QPushButton("<")
check = QPushButton("Check")
dow = QPushButton("Download")


# desing of application
master_layout = QVBoxLayout()
master_layout.addWidget(title)

# button row-1
btn_row = QHBoxLayout()
btn_row.addWidget(txt_box)
btn_row.addWidget(check)


# function


# Download Code start


class DownloadThread(threading.Thread):
    def __init__(self, stream, output_path):
        super().__init__()
        self.stream = stream
        self.output_path = output_path
        self.daemon = True
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        while self._running:
            time.sleep(1)
            print(
                f"Downloaded: {self.stream.filesize / (1024 * 1024):.2f} MB / {self.stream.filesize / (1024 * 1024):.2f} MB ({self.stream.progress:.2f}%)",
                end="\r",
            )

        print("\nDownload completed successfully!")

def get_available_resolutions(video):
    return [stream.resolution for stream in video.streams if stream.resolution]


def choose_resolution(video):
    print("Available Resolutions:")
    resolutions = get_available_resolutions(video)
    for i, res in enumerate(resolutions):
        print(f"{i+1}. {res}")

    while True:
        choice = input("Enter the number corresponding to your preferred resolution: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(resolutions):
                return resolutions[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a number.")


def download_video(video_url, output_path, resolution=None):
    try:
        yt = YouTube(video_url)
        video_title = yt.title
        if resolution:
            stream = yt.streams.filter(res=resolution).first()
        else:
            stream = (
                yt.streams.first()
            )  # Get the first available stream (usually highest resolution)

        print(f"Downloading video: {video_title}")
        stream.download(output_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")


def download_playlist(playlist_url, resolution=None):
    try:
        playlist = Playlist(playlist_url)
        output_path = os.path.join(os.path.dirname(__file__), "Playlist Downloads")
        os.makedirs(output_path, exist_ok=True)

        for video_url in playlist.video_urls:
            download_video(video_url, output_path, resolution)
            print()

    except Exception as e:
        print(f"Error downloading playlist: {e}")


# Download Code end


def checkRes():
    # butto row-2
    btn_row2 = QHBoxLayout()
    dropdown.addItems(resuluion)
    btn_row2.addWidget(dropdown)
    btn_row2.addWidget(dow)
    master_layout.addLayout(btn_row2)


def click():
    new_btn = app.sender()
    txt = new_btn.text()
    # txt_box.setText(str(txt)) #we can see witch button click

    if txt == "Clear":
        txt_box.clear()
    elif txt == "<":
        current_val = txt_box.text()
        txt_box.setText(current_val[:-1])


# butto row-2
# btn_row2 = QHBoxLayout()
# dropdown.addItems(resuluion)
# btn_row2.addWidget(dropdown)
# btn_row2.addWidget(dow)

# butto row-3
btn_row3 = QHBoxLayout()
btn_row3.addWidget(clear)


# butto row-4
btn_row4 = QHBoxLayout()
btn_row4.addWidget(Status)

# add rows
master_layout.addLayout(btn_row)
master_layout.addLayout(btn_row3)
master_layout.addLayout(btn_row4)

main_window.setLayout(master_layout)


# events
# clear.clicked.connect(click)
# delete.clicked.connect(click)
check.clicked.connect(checkRes)

# show and run
main_window.show()
app.exec_()
