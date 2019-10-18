# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:02:52 2019

@author: dungn
"""
import pandas as pd
import os

def initialize_dataframe():
    data_frame = pd.DataFrame()
    data_frame.to_pickle('resources/dump.pkl')

def update_bookings(dictt):
    fileName = input("resources/dump.pkl")
    if  os.path.isFile(fileName)==0 or os.path.exists(fileName)==0:
        initialize_dataframe()
    else:
        datata = pd.read_pickle('resources/dump.pkl')
        datata.append(pd.DataFrame.from_dict(dictt))
        datata.to_pickle('resources/dump.pkl')

    
#def save_obj(obj, name ):
#    with open('resources/'+ name + '.pkl', 'wb') as f:
#        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
#
#def load_obj(name ):
#    with open('resources/' + name + '.pkl', 'rb') as f:
#        return pickle.load(f)
#
#def update_dict(dict):
#    directlist = load_obj('dump')
#    directlist.append(dict)
#    save_obj(directlist, "dump")
#    print(directlist)
#    load_obj(dict)



