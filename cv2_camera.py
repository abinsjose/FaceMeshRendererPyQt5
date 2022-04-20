# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:51:17 2022

@author: abins
"""
from PyQt5.QtCore import QObject, QTimer, pyqtSignal
import cv2

class Cv2Camera(QObject):
    CaptureStatusChanged = pyqtSignal(bool)
    
    def __init__(self, parent, image_processor):
        self.parent = parent
        self.image_processor = image_processor
        self.timer = QTimer()
        self.timer.timeout.connect(self.Capture)
        self.id = 0
        super().__init__(parent)
        
    def __del__(self):
        print('Cv2Camera destroyed')
        if (hasattr(self, 'videoCap')):
            self.videoCap.release()
            del self.videoCap

    def StartCapture(self):
        self.videoCap = cv2.VideoCapture(0)
        
        # Check if the webcam is opened correctly
        if not self.videoCap.isOpened():
            raise IOError("Cannot open webcam")
            
        print('Starting capture')
        self.timer.start(30)
        self.CaptureStatusChanged.emit(True)

    def StopCapture(self):
        print('Stopping capture')
        self.timer.stop()
        if (hasattr(self, 'videoCap')):
            self.videoCap.release()
            del self.videoCap
        if (hasattr(self, 'CaptureStatusChanged')):
            self.CaptureStatusChanged.emit(False)

    def Capture(self):
        ret, frame = self.videoCap.read()
        if ret:
            print('Image captured ', self.id)
            self.id = self.id + 1
            self.image_processor.Process(frame)
        else:
            print('Failed to capture image')

