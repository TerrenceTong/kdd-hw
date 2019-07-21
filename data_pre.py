import pandas as pd
import numpy as np
import os

#input = ['AC 1999-2003.csv','AC 2004-2008.csv','AC 2009-2013.csv','AC 2014-2018.csv','G 1999-2003.csv','G 2004-2008.csv','G 2009-2013.csv','G 2014-2018.csv','GI 1999-2003.csv','']

input = os.listdir('D:\\python_workspace\\kdd\\linerlog\\Daily beta\\')
processed_csv = ['AC Daily 1999-2003.csv', 'AC Daily 2004-2008.csv', 'AC Daily 2009-2013.csv', 'AC Daily 2014-2018.csv', 'G Daily 1999-2003.csv', 'G Daily 2004-2008.csv']

for data_name in input:  
    if(data_name in processed_csv):
        continue
    data = pd.read_csv('D:\\python_workspace\\kdd\\linerlog\\Daily beta\\'+data_name)
    data = data.dropna(axis=0, how='any')
    data_after_produce = pd.DataFrame(columns=['fund number','Month','Return','F1','F2','F3','F4','F5','F6','F7','F8'])
    for index,row in data.iterrows():
        #print(type(row))
        print("csv_name:{}".format(data_name))
        print("processing {}!".format(row['fund number']))
        gate = 0
        for idx in row.index:
            #print(row[idx])
            if( row[idx] != 'R' and (row[idx] != '#VALUE!') and (not pd.isnull(row[idx])) ) :
                row[idx] = round(float(row[idx]),6)
            else:
                gate = 1
        if(gate == 0):
            data_after_produce.loc[data_after_produce.shape[0]] = row

    """ formater="{0:.03f}".format
    data_after_produce.applymap(formater) """
    data_after_produce.to_csv('D:\\python_workspace\\kdd\\linerlog\\processed_Daily beta\\'+data_name,index=False)
