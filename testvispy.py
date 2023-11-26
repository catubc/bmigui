import sys
import numpy as np
import cv2
from vispy import app, visuals, scene

class VideoPlayerCanvas(app.Canvas):
    def __init__(self, video_path):
        app.Canvas.__init__(self, keys='interactive', size=(800, 600))

        # Set up video capture
        self.video_capture = cv2.VideoCapture(video_path)

        # Create Quad visual to display the video frames
        self.visual = visuals.ImageVisual(method='auto')

        # Create a SceneCanvas and add the visual
        self.scene = scene.SceneCanvas(keys='interactive', show=True)
        self.view = self.scene.central_widget.add_view()
        self.view.add(self.visual)

        # Timer for updating video frames
        self.timer = app.Timer('auto', connect=self.update_video, start=True)

    def on_draw(self, event):
        self.scene.draw()

    def update_video(self, event):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.visual.set_data(np.flipud(frame))
            self.update()

def run_app(video_path):
    canvas = VideoPlayerCanvas(video_path)
    app.run()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py path/to/your/video.mp4")
        sys.exit(1)

    video_path = sys.argv[1]
    run_app(video_path)

