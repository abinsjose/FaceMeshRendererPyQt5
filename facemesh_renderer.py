# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:47:07 2022

@author: abins
"""

from PyQt5 import QtWidgets
from ui_facemesh_renderer import Ui_FaceRendererForm
import cv2_camera

class FaceMeshRenderer(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_FaceRendererForm()
        self.ui.setupUi(self)
        
        self.cam = cv2_camera.Cv2Camera(self.ui.cameraView)
        self.ui.startCaptureBtn.clicked.connect(self.cam.StartCapture)
        self.ui.stopCaptureBtn.clicked.connect(self.cam.StopCapture)
        self.cam.CaptureStatusChanged.connect(self.CameraStatusChanged)
        self.show()

    def closeEvent(self, event):
        print('Closing facemeshrenderer')
        self.cam.StopCapture();
        del self.cam
        return super().closeEvent(event)
        
    def CameraStatusChanged(self, status):
        print("Camera status changed to ", status)
        self.ui.startCaptureBtn.setEnabled(not status)
        self.ui.stopCaptureBtn.setEnabled(status)