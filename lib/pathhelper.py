# -*- coding: utf-8 -*-
import os

'''当前路径'''
current_path = __file__
'''项目的根目录'''
father_path = os.path.abspath(os.path.dirname(current_path)+os.path.sep+"..")
'''项目数据目录'''
data_path = os.path.join(father_path, 'Datas')

'''观测站位置文件'''
station_path = os.path.join(data_path, 'station_latlon.txt')

if __name__ == '__main__':
    print('\n'.join((current_path, father_path, data_path)))
