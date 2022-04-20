# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:19:47 2022

@author: abins
"""

import numpy as np
import pyvista as pv
import pyvistaqt as pvqt
from PyQt5 import QtWidgets

class Renderer():
    
    def __init__(self):
        print('Renderer constructed')
    
    def __del__(self):
        print('Renderer destroyed')

    def Destroy(self):
        if (hasattr(self, 'plotter')):
            print('Closing plotter')
            self.plotter.close()
            
    def LandmarksToArray(self, face_landmarks, image_width=1, image_height=1):
        landmark_gen = [[landmark.x * image_width,
                         landmark.y * image_height,
                         landmark.z * image_width]
                        for landmark in face_landmarks.landmark]
           
        return np.array(landmark_gen, dtype='float')
    
       
    def Create(self, parent, face_landmarks, image_width, image_height):
    
        face_array = self.LandmarksToArray(face_landmarks, image_width, image_height)
        print(face_array.shape)
        
        self.plotter = pvqt.QtInteractor()
        self.vlayout = QtWidgets.QVBoxLayout(parent)
        self.vlayout.addWidget(self.plotter.interactor)
        self.mesh = pv.PolyData(face_array)
        self.plotter.add_mesh(self.mesh)    # add a mesh to the scene
        self.plotter.camera_position = [(271.17795442515796, 373.32732951080106, -368.10150608187024),
                                        (260.26798248291016, 327.3098945617676, 12.291778326034546),
                                        (0.06920632076548205, -0.9906165211668803, -0.11785326960815704)]
   
    def Update(self, face_landmarks, image_width, image_height):
        face_array = self.LandmarksToArray(face_landmarks, image_width, image_height)
        print(face_array.shape)
        self.plotter.update_coordinates(face_array, self.mesh)
        #print('camera position: ', str(self.plotter.camera_position))
        