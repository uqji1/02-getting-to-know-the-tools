import pandas as pd
import os
from os import path

data_folder = path.join(
    path.abspath('..'),  # '..' means the directory above this one
    'data')

def load_data():
    fault_file = path.join(data_folder, 'Mains Faults Data_SAP_2010-2016.xlsx')
    df = faults_xl.parse('All Notifications_2010-2016')
    return df

df = load_data()

df