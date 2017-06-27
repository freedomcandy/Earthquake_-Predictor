# from tensorflow.examples.tutorials.mnist import input_data
# 
# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
# X_train = mnist.train.images
# Y_train = mnist.train.labels
# # print(X_train.shape)
# # print(X_train[0])
# print(Y_train.shape)
# print(Y_train[0])



from sklearn.datasets import load_boston  
from sklearn.model_selection import train_test_split  
from sklearn import preprocessing  
from sklearn.neural_network import MLPRegressor  
from sklearn.ensemble import GradientBoostingRegressor  
#波士顿房价数据  
boston=load_boston()  
x=boston.data  
y=boston.target  
print('波士顿数据:',x.shape)  
print(x[::100])  
print('波士顿房价:',y.shape)  
print(y[::100])  
  
print('##################################################################')  
  
# 随机挑选  
train_x_disorder, test_x_disorder, train_y_disorder, test_y_disorder = train_test_split(x, y,  
                                                                    train_size=0.8, random_state=33)  



#数据标准化  
ss_x = preprocessing.StandardScaler()  
train_x_disorder = ss_x.fit_transform(train_x_disorder)  
test_x_disorder = ss_x.transform(test_x_disorder)  
  
ss_y = preprocessing.StandardScaler()  
train_y_disorder = ss_y.fit_transform(train_y_disorder.reshape(-1, 1))  
test_y_disorder=ss_y.transform(test_y_disorder.reshape(-1, 1))  
  
# 多层感知器-回归模型  
model_mlp = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(60, 40, 20), random_state=1)  
model_mlp.fit(train_x_disorder,train_y_disorder.ravel())  
mlp_score=model_mlp.score(test_x_disorder,test_y_disorder.ravel())  
print('sklearn多层感知器-回归模型得分',mlp_score)  
  
  
model_gbr_disorder=GradientBoostingRegressor()  
model_gbr_disorder.fit(train_x_disorder,train_y_disorder.ravel())  
gbr_score_disorder=model_gbr_disorder.score(test_x_disorder,test_y_disorder.ravel())  
print('sklearn集成-回归模型得分',gbr_score_disorder)#准确率较高 0.853817723868  