# importing Qt widgets
from PyQt5.QtWidgets import *

# importing system
import sys

# importing numpy as np
import numpy as np

# importing pyqtgraph as pg
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt

plt.ion()

import os
os.putenv("QT_QPA_PLATFORM", "xcb")

# Image View class
class ImageView(pg.ImageView):

	# constructor which inherit original
	# ImageView
	def __init__(self, *args, **kwargs):
		pg.ImageView.__init__(self, *args, **kwargs)

class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("PyQtGraph")

		# setting geometry
		self.setGeometry(100, 100, 600, 500)

		# icon
		icon = QIcon("skin.png")

		# setting icon to the window
		self.setWindowIcon(icon)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# creating a widget object
		widget = QWidget()

		# creating a label
		label = QLabel("Geeksforgeeks Video")

		# setting minimum width
		label.setMinimumWidth(130)

		# making label do word wrap
		label.setWordWrap(True)

		# setting configuration options
		pg.setConfigOptions(antialias = True)

		# creating a graphics layout widget
		win = pg.GraphicsLayoutWidget()

		# adding view box object to graphic window
		view = win.addViewBox()

		##lock the aspect ratio so pixels are always square
		view.setAspectLocked(True)

		# Create image item
		self.img = pg.ImageItem(border='w')

		# adding image item to the view box
		view.addItem(self.img)

		# Set initial view bounds
		view.setRange(QRectF(0, 0, 600, 600))

		# Create random image
		self.data = np.random.normal(size=(15, 600, 600), 
									loc = 1024, scale = 64).astype(np.uint16)

		# helps in incrementing
		self.i = 0

		# fps
		self.fps = 0

		# method to update the data of image
		def updateData():

			## Display the data
			self.img.setImage(self.data[self.i])

			# creating new value of i
			self.i = (self.i + 1) % self.data.shape[0]

			# creating a qtimer
			QTimer.singleShot(1, updateData)

			# getting current time
			now = 1

		# call the update method
		updateData()

		# Creating a grid layout
		layout = QGridLayout()

		# minimum width value of the label
		label.setMinimumWidth(130)

		# setting this layout to the widget
		widget.setLayout(layout)

		# adding label in the layout
		layout.addWidget(label, 1, 0)

		# plot window goes on right side, spanning 3 rows
		layout.addWidget(win, 0, 1, 3, 1)

		# setting this widget as central widget of the main window
		self.setCentralWidget(widget)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

