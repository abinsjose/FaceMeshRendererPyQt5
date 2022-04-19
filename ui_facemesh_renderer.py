# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facemesh_renderer.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceRendererForm(object):
    def setupUi(self, FaceRendererForm):
        FaceRendererForm.setObjectName("FaceRendererForm")
        FaceRendererForm.resize(658, 558)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FaceRendererForm.sizePolicy().hasHeightForWidth())
        FaceRendererForm.setSizePolicy(sizePolicy)
        FaceRendererForm.setMinimumSize(QtCore.QSize(640, 480))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FaceRendererForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cameraView = QtWidgets.QWidget(FaceRendererForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraView.sizePolicy().hasHeightForWidth())
        self.cameraView.setSizePolicy(sizePolicy)
        self.cameraView.setMinimumSize(QtCore.QSize(640, 480))
        self.cameraView.setObjectName("cameraView")
        self.verticalLayout_2.addWidget(self.cameraView, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.startCaptureBtn = QtWidgets.QPushButton(FaceRendererForm)
        self.startCaptureBtn.setObjectName("startCaptureBtn")
        self.verticalLayout_2.addWidget(self.startCaptureBtn)
        self.stopCaptureBtn = QtWidgets.QPushButton(FaceRendererForm)
        self.stopCaptureBtn.setObjectName("stopCaptureBtn")
        self.verticalLayout_2.addWidget(self.stopCaptureBtn)

        self.retranslateUi(FaceRendererForm)
        QtCore.QMetaObject.connectSlotsByName(FaceRendererForm)

    def retranslateUi(self, FaceRendererForm):
        _translate = QtCore.QCoreApplication.translate
        FaceRendererForm.setWindowTitle(_translate("FaceRendererForm", "Face Mesh Renderer"))
        self.startCaptureBtn.setText(_translate("FaceRendererForm", "Start Capture"))
        self.stopCaptureBtn.setText(_translate("FaceRendererForm", "Stop Capture"))
