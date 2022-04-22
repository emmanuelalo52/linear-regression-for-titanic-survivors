#dawg i searched the whole stakeoverflow for the right one, damn you bozo
from linear_regression_model import *
def make_input_fn(data_df,label_df,num_epochs=10,shuffle=True,batch_size=32):
  def input_function():#inner function, this will be returned
    ds =tf.data.Dataset.from_tensor_slices((dict(data_df),label_df))#create a dict of the data frame and the representation
    if shuffle:
      ds = ds.shuffle(1000)#randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)#split dataset into batches of 32 and repeat process for number of epochs
    return ds
  return input_function#return a function object for use
train_input_fn = make_input_fn(dftrain_mode,y_train)
test_input_fn = make_input_fn(dftest_mode,y_test,num_epochs=1,shuffle=False)
