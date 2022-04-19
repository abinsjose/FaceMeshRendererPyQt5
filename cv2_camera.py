# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:51:17 2022

@author: abins
"""
from PyQt5.QtCore import QObject, QTimer, pyqtSignal


import cv2
import facemesh
import renderer

class Cv2Camera(QObject):
    captureStatusChanged = pyqtSignal(bool)
    
    def __init__(self, parent):
        self.parent = parent
        self.timer = QTimer()
        self.timer.timeout.connect(self.capture)
        self.id = 0
        super().__init__()
        
    def __del__(self):
        if (hasattr(self, 'renderer')):
            self.renderer.destroy()

    def startCapture(self):
        self.videoCap = cv2.VideoCapture(0)
        
        # Check if the webcam is opened correctly
        if not self.videoCap.isOpened():
            raise IOError("Cannot open webcam")
            
        print('Starting capture')
        self.timer.start(30)
        self.captureStatusChanged.emit(True)
        
    def stopCapture(self):
        if (hasattr(self, 'videoCap')):
            self.videoCap.release()
            del self.videoCap
        print('Stopping capture')
        self.timer.stop()
        self.captureStatusChanged.emit(False)

        
    def processVideo(self, image):
        #cv2.imwrite('capture.png',image)
        face_landmarks = []
        print('Image shape:', image.shape)
        if (not hasattr(self, 'fm')):
            self.fm = facemesh.FaceMesh()
        
        multi_face_landmarks = self.fm.Generate(image)
        
        for face_landmarks in multi_face_landmarks:
            #print(face_landmarks)

            if (not hasattr(self, 'renderer')):
                print('creating renderer')
                self.renderer = renderer.Renderer()
                self.renderer.create(self.parent, face_landmarks, image.shape[1], image.shape[0])
            else:
                print('updating renderer')
                self.renderer.update(face_landmarks, image.shape[1], image.shape[0])
            
    def capture(self):
        ret, frame = self.videoCap.read()
        if ret:
            print('Image captured ', self.id)
            self.id = self.id + 1
            self.processVideo(frame)
        else:
            print('Failed to capture image')

