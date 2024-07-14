import pickle
import tensorflow as tf
from keras.models import load_model
from PIL import Image
import numpy as np

import warnings
warnings.filterwarnings(action="ignore")

class Prediction(object):
    def __init__(self) -> None:
        pass
    
    def loadModel():
        with open('model_labels.pkl', 'rb') as labelPickle:
            modelLabels=pickle.load(labelPickle)[0]
            
        model=load_model('model.h5')
        
        return modelLabels, model
            
    def preprocessImage(self, imageFile):
        image=np.array(Image.open(imageFile).convert('RGB').resize(224, 224))
        image=image/255
        imageArray=tf.expand_dims(image, 0)
        return imageArray
        
    def makePrediction(self, imageFile):
        modelLabels, model=self.loadModel()
        imageArray=self.preprocessImage(imageFile=imageFile)
        
        prediction=model.predict(imageArray)
        prediction=modelLabels[np.argmax(prediction[0])]
        confidence=round(100 * (np.max(prediction[0])), 2)
        
        return prediction, confidence
        
        