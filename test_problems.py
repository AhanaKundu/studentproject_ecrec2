#from exception import customException
#import src.exception
import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))
from sklearn.linear_model import _base

import pickle


with open('artifacts/model.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)