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


