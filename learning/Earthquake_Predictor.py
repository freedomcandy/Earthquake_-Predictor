#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor


from obspy import read
from obspy.signal.trigger import plot_trigger

st = read("../Datas/after/SC.XJI.2008133160000.D.00.BHN.sac")
# st = read("../Datas/after/GS.WDT.2008213000000.BHZ")
trace = st[0]
df = trace.stats.sampling_rate
print(trace.stats.starttime)
print(trace.stats.endtime)

from obspy.signal.trigger import classic_sta_lta
cft = classic_sta_lta(trace.data, int(5 * df), int(10 * df))
for i in cft:
    if i == 0:
        print('===============')

# print(len(cft))
# for i in cft:
#     if i <= 0.0:
#         print('Z')
#     else:
#         print('N')
plot_trigger(trace, cft, 1.5, 0.5)



# clean_before = pd.read_csv('../CleanData/clean_before', sep='\n', encoding='utf8')
# print(clean_before)

# from sklearn.cluster import KMeans
# y_pred = KMeans(n_clusters=4, random_state=9).fit_predict(clean_before)
# print(y_pred)
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)
# plt.show()