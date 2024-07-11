import pickle

class Prediction(object):
    def __init__(self) -> None:
        pass
    
    def loadModel():
        with open('model_labels.pkl', 'rb') as labelPickle:
            modelLabels=pickle.load(labelPickle)
            
        with open('model.pkl', 'rb') as modelPickle:
            model=pickle.load(modelPickle)
            
        return modelLabels, modelPickle
            
    def preprocessImage(imageFile):
        pass
        
    def makePrediction():
        pass