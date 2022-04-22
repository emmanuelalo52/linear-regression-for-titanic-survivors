# -*- coding: utf-8 -*-
"""linear regression model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nKPO-pvEy-sOzAAhbyRgN4QH3LErHR4k
"""

!pip install -q sklearn

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

dftrain_mode=pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')#training data
dftest_mode=pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')#tesing data
y_train=dftrain_mode.pop('survived')
y_test=dftest_mode.pop('survived')

CATEGORICAL_COLUMNS = ['sex','n_siblings_spouses','parch','class','deck','embark_town','alone']
NUMERICAL_COLUMNS = ['age','fare']

feature_columns=[]
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary=dftrain_mode[feature_name].unique()#gets all unique values of a given column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name,vocabulary))

for feature_name in NUMERICAL_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name,dtype=tf.float32))

print(feature_columns)


