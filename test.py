from model import *
result= list(linear_est.predict(test_input_fn))# to check the actual predictions of the model
print(dftrain_mode.loc[3])
print(result[2]['probabilities'][1])