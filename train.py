import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

model = LinearRegression()

def softmax(x):
    e = np.exp(x)
    e_sum = np.sum(e)
    
    ret = e/e_sum
    return ret.tolist()


def train(ID_START, id_and_X, RESULT, model):
    X_TRAIN_NOW = []
    Y_TRAIN_NOW = []
    id_now = ID_START
    for index,row in id_and_X.iterrows():
        #print(index,row['F1'])
        #print(("F1: {}").format(row[1]))
        if(id_now != row['fund number'] or index == id_and_X.shape[0]-1 ):
            print("-------------------------------------------------------------------")
            """ print("the shape of X_TRAIN_NOW is {}.".format(np.array(X_TRAIN_NOW).shape))
            print("the shape of Y_TRAIN_NOW is {}.".format(np.array(Y_TRAIN_NOW).shape)) """
            model.fit(X_TRAIN_NOW,Y_TRAIN_NOW)
            #print(model.coef_[0])
            beta_now = softmax(model.coef_[0])
            #print(type(beta_now))
            result_series = pd.Series({'Beta1':beta_now[0],'Beta2':beta_now[1],'Beta3':beta_now[2],\
                'Beta4':beta_now[3],'Beta5':beta_now[4],'Beta6':beta_now[5],'Beta7':beta_now[6],\
                    'Beta8':beta_now[7],'fund number':id_now})
            #print(result_series)
            for idx in result_series.index:
                result_series[idx] = round(result_series[idx], 5)
        
            RESULT.loc[RESULT.shape[0]] = result_series
            #print(RESULT)

            print("{} is training".format(id_now))
            print("Betas are:{}".format(beta_now))
            #if( type(row[1]) !='R' ):
            
            id_now = row['fund number']
            X_TRAIN_NOW = [row[2:]]
            Y_TRAIN_NOW = [[row[1]]]

        else:
            #if( type(row[1]) !='R' ):
            temp_list_x = row[2:]
            temp_list_y = [row[1]]
            X_TRAIN_NOW.append(temp_list_x)
            Y_TRAIN_NOW.append(temp_list_y)

        """ temp = 0
        for i in range(8):
            temp += beta_now[i]*X_TRAIN_NOW[0][i]
        print(Y_TRAIN_NOW[0][0]) """
    RESULT.insert(0,'fund number',RESULT.pop('fund number'))

""" x = [[1,1,1],[1,1,2],[1,2,1]]
y = [[6],[9],[8]]
 """
""" model.fit(x,y)
y2 = model.predict(x2)
print(y2)
 """

def main():
    input= os.listdir('D:\\python_workspace\\kdd\\linerlog\\processed_Monthly beta\\')
    for data_name in input:
        data = pd.read_csv('D:\\python_workspace\\kdd\\linerlog\\processed_Monthly beta\\'+data_name)
        id_and_features = ['fund number','Return','F1','F2','F3','F4','F5','F6','F7','F8']
        id_and_X = data[id_and_features]

        RESULT = pd.DataFrame(columns=['Beta1','Beta2','Beta3','Beta4','Beta5','Beta6','Beta7','Beta8','fund number'])
        ID_START = id_and_X.loc[0][0]
        train(ID_START, id_and_X, RESULT, model)
        RESULT.to_csv('D:\\python_workspace\\kdd\\linerlog\\result\\'+data_name,index=False)

if __name__ == "__main__":
    main()