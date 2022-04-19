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
        
        #self.plotter.camera_position = [(0.29021832576334505, 0.2999641109829936, 1.0),
        #  (0.4061845988035202, 0.6308744549751282, 0.019136086106300354),
        #  (0.14587638746193216, -0.8380288155379086, -0.5257640002027394)]
        
        #self.plotter.camera.zoom(2)    # Note how we can now access underlying attributes
        #self.plotter.show() 
    
        #self.mesh = pv.PolyData(face_array)
        #self.mesh.plot(point_size=5, style='wireframe', show_edges=True)
    
    def Update(self, face_landmarks, image_width, image_height):
        face_array = self.LandmarksToArray(face_landmarks, image_width, image_height)
        print(face_array.shape)
        self.plotter.update_coordinates(face_array, self.mesh)
        print('camera position: ', str(self.plotter.camera_position))
        