# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:36:12 2022

@author: abins
"""

from abc import ABC, abstractmethod
from facemesh import FaceMesh
from renderer import Renderer

class ImageProcessor(ABC):
    @abstractmethod
    def Process(self, image):
        pass
            
class ImagePipeline(ImageProcessor):
    def __init__(self, widget):
        print('ImagePipeline created')
        self.camera_view = widget
        
    def __del__(self):
        print('ImagePipeline destroyed')
        #if (hasattr(self, 'renderer')):
        #    self.renderer.Destroy()
    
    def Process(self, image):
        #cv2.imwrite('capture.png',image)
        face_landmarks = []
        #print('Image shape:', image.shape)
        if (not hasattr(self, 'fm')):
            self.fm = FaceMesh()
        
        multi_face_landmarks = self.fm.Generate(image)
        
        for face_landmarks in multi_face_landmarks:
            if (not hasattr(self, 'renderer')):
                print('creating renderer')
                self.renderer = Renderer()
                self.renderer.Create(self.camera_view, face_landmarks, 
                                     image.shape[1], image.shape[0])
            else:
                #print('updating renderer')
                self.renderer.Update(face_landmarks, 
                                     image.shape[1], image.shape[0])