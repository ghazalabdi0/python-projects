from PySide6.QtWidgets import QApplication, QWidget, QTimeEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox
import sys
from PySide6.QtCore import QTime, QTimer, Qt
from PySide6.QtGui import QFont

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("countdown")
layout = QVBoxLayout()
window.setLayout(layout)
window.resize(300, 200)  

#time input
time_input = QTimeEdit()
time_input.setDisplayFormat("HH:mm:ss")
layout.addWidget(time_input)

label = QLabel("00:00:00")
font = QFont()
font.setPointSize(30)
font.setBold(True)
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

timer = QTimer()
total_seconds = 0
is_running = False


def update_countdown():
    global total_seconds

    if total_seconds > 0:
        total_seconds -= 1

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
    else:
        timer.stop()
        QMessageBox.information(
            window,
            "Time's up!",
            "⏰ Your time has finished!"
        )


def start_counting():
    global total_seconds
    global is_running

    if not is_running:
        t = time_input.time()

        total_seconds = (
            t.hour() * 3600
            + t.minute() * 60
            + t.second()
        )

    is_running = True
    timer.start(1000)


def stop_counting():
    timer.stop()


timer.timeout.connect(update_countdown)

start_button = QPushButton("Start")
start_button.clicked.connect(start_counting)
layout.addWidget(start_button)

stop_button = QPushButton("Stop")
stop_button.clicked.connect(stop_counting)
layout.addWidget(stop_button)

window.show()
app.exec()