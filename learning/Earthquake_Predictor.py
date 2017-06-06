#coding=utf-8
from obspy.core import read
#Before
BHZ = read('./Datas/before/SC.XJI.2008131160000.D.00.BHZ.sac', debug_headers=True) #纵波
BHE = read('./Datas/before/SC.XJI.2008131160002.D.00.BHE.sac', debug_headers=True) #横波东西
BHN = read('./Datas/before/SC.XJI.2008131160002.D.00.BHN.sac', debug_headers=True) #横波南北
print(BHZ)
print(BHE)
print(BHN)


print()
print()



#After
aBHZ = read('./Datas/after/SC.XJI.2008133160000.D.00.BHZ.sac', debug_headers=True) #纵波
aBHE = read('./Datas/after/SC.XJI.2008133160001.D.00.BHE.sac', debug_headers=True) #横波东西
aBHN = read('./Datas/after/SC.XJI.2008133160000.D.00.BHN.sac', debug_headers=True) #横波南北
print(aBHZ)
print(aBHE)
print(aBHN)


# import tflearn
print('sunny_test')


import tflearn

def threeLayerDNN(data,labels):
    net = tflearn.input_data(shape=[None, None])
    net = tflearn.fully_connected(net, 0)
    net = tflearn.fully_connected(net, 0)
    net = tflearn.fully_connected(net, 0, activation='softmax')
    #categorical_crossentropy
    net = tflearn.regression(net, optimizer='sgd', loss='mean_square')

    # Define model
    model = tflearn.DNN(net)
    # Start training (apply gradient descent algorithm)
    model.fit(data, labels, n_epoch=10, batch_size=16, show_metric=True)
    return model.predict(data)