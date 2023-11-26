import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class VideoPlayer(QMainWindow):
    def __init__(self):
        super(VideoPlayer, self).__init__()

        self.setup_ui()
        self.setup_video()

    def setup_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.video_label = QLabel(self)
        self.layout.addWidget(self.video_label)

    def setup_video(self):
        self.video_capture = cv2.VideoCapture("/media/cat/4TBSSD/dan/simba/2020_07_30_15_43_41_766841.mp4")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 milliseconds

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Convert BGR image to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to QImage
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Display the QImage in the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.video_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setGeometry(100, 100, 800, 600)
    player.setWindowTitle('Video Player')
    player.show()
    sys.exit(app.exec_()) 
