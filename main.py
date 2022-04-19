# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:47:07 2022

@author: abins
"""
from PyQt5 import QtWidgets
from facemesh_renderer import FaceMeshRenderer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    faceMeshRenderer = FaceMeshRenderer()
    sys.exit(app.exec_())