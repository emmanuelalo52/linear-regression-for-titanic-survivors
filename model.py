from linear_regression_model import *
from clear_console import *
#making this model
linear_est=tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(train_input_fn)#train model
result=linear_est.evaluate(test_input_fn)#get model metrics and stats trough tests

clear_output()#clear console input
print(result['accuracy'])# the result variable is simply a dict of stats about our model
print(result)
