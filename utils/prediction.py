import os
import pickle
import logging


logging.basicConfig(filename='logging')
class Prediction(object):
    def __init__(self) -> None:
        self.modelPath=f'xception.weights.best.hdf5'
        if not os.path.exists(self.modelPath):
            logging.warning("Model doesn't exists")
            
    
    def loadModel(self):
        with open(self.modelPath, 'rb') as openedModel:
            model = pickle.load(openedModel)
        return model

    
    def preprocessImage(self):
        model=self.loadModel()
        pred = model.predict_generator(test_generator,
                               steps=STEP_SIZE_TEST,
                               verbose=1)
        pred_classes = np.argmax(pred, axis=1)
        
    def makePrediction(self):
        pass