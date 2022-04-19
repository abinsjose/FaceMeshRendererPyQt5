# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:36:12 2022

@author: abins
"""

import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

class FaceMesh():
    def Generate(self, image):
        with mp_face_mesh.FaceMesh(
            static_image_mode=False,
            refine_landmarks=True,
            max_num_faces=2,
            min_detection_confidence=0.5) as face_mesh:
            
            # Convert the BGR image to RGB and process it with MediaPipe Face Mesh.
            results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            
            if not results.multi_face_landmarks:
                print("No faces detected")
                return []
            return results.multi_face_landmarks


            