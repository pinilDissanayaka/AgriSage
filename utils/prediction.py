import pickle
import tensorflow as tf
from keras.models import load_model
import keras.utils as kerasUtils
from PIL import Image
from werkzeug.utils import secure_filename
import numpy as np

import warnings
warnings.filterwarnings(action="ignore")

class Prediction(object):
    def __init__(self) -> None:
        pass
    
    def loadModel(self):
        with open('model_labels.pkl', 'rb') as labelPickle:
            modelLabels=pickle.load(labelPickle)[0]
            
        model=load_model('model.h5')
        
        return modelLabels, model
            
    def preprocessImage(self, imageFile):
        imageArray=kerasUtils.img_to_array(imageFile)
        imageArray=imageArray/255
        imageArray=np.expand_dims(imageArray, axis=0)
        return imageArray
        
    def makePrediction(self, imagePath):
        modelLabels, model=self.loadModel()
        
        imageFile=kerasUtils.load_img(path=imagePath, target_size=(224, 224))
        
        imageArray=self.preprocessImage(imageFile=imageFile)
        
        prediction=model.predict(imageArray)
        
        confidence=round(100 * (np.max(prediction[0])), 2)
        
        prediction=modelLabels[np.argmax(prediction[0])]
                
        return prediction, confidence
        
        