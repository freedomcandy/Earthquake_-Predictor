'''
Created on 2017年6月13日

@author: RoyGuo
'''
import tensorflow as tf
from tensorflow.contrib.tensor_forest.python import tensor_forest as rfr
from tensorflow.contrib.tensor_forest.client import random_forest

hparams = rfr.ForestHParams()
classifier = random_forest.TensorForestEstimator(hparams)



