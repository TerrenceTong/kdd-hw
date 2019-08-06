import os
import gc
import sys
import pandas as pd

def typicalsamling(group,typicalNDict):
    name = group.name
    n=typicalNDict[name]
    return group.sample(n=n)

def replaced_typicalsamling(group,typicalNDict):
    name = group.name
    n=typicalNDict[name]
    return group.sample(n=n,replace=True)
def sample_time(TICKERS_DIR,BETA_DIR,RESULT_DIR,TIME,NUM_XLSX_BASE):
        fund_number_filenames = os.listdir(BETA_DIR)
        fund_number_filenames.sort()
        print("fundnumber_files: \n {}".format(fund_number_filenames))
        tickers_filenames = os.listdir(TICKERS_DIR)
        tickers_filenames.sort()
        print("tickers_files: \n {}".format(tickers_filenames))
        """ already = os.listdir(RESULT_DIR) """
        for fund_number_filename in fund_number_filenames:
                """ if(fund_number_filename in already):
                        print("continue")
                        continue """
                RESULT = pd.DataFrame(columns=['fund number','time','return','isreplace'])
                df_beta = pd.read_csv(BETA_DIR+fund_number_filename)
                for idx, row in df_beta.iterrows():
                        #print(row)
                        typicalNDict = {
                                1: int(100*row[1]),
                                2: int(100*row[2]),
                                3: int(100*row[3]),
                                4: int(100*row[4]),
                                5: int(100*row[5]),
                                6: int(100*row[6]),
                                7: int(100*row[7]),
                                8: int(100*row[8])
                        }
                        print(typicalNDict)
                        num_xlsx = NUM_XLSX_BASE
                        #num_xlsx = 3
                        for i in range(5):
                                df_ticker_groupby_time = pd.read_excel(TICKERS_DIR+tickers_filenames[num_xlsx]).groupby(TIME)
                                print("open {}".format(tickers_filenames[num_xlsx]))
                                num_xlsx = num_xlsx+1
                                #df_ticker_groupby_time = df_ticker.groupby(TIME)
                                """ del df_ticker
                                gc.collect() """
                                for name,group in df_ticker_groupby_time:
                                        #fund_number = row[0]
                                        return_bar = 0
                                        isreplace = 0
                                        try:
                                                sample_result = group.groupby('Type',group_keys=False).apply(typicalsamling,typicalNDict)
                                                return_bar = round(sample_result['Returns without Dividends'].mean(),5)
                                        except Exception as e:
                                                #print("replaced sample.")
                                                isreplace = 1
                                                sample_result = group.groupby('Type',group_keys=False).apply(replaced_typicalsamling,typicalNDict)
                                                return_bar = round(sample_result['Returns without Dividends'].mean(),5)
                                        result_series = pd.Series({'fund number':row[0],'name':name,'return':return_bar,'isreplace':isreplace})
                                        RESULT.loc[RESULT.shape[0]] = result_series
                                        print('{},{},{},{} has done.'.format(row[0],name,return_bar,isreplace))
                                del name
                                del group
                                del df_ticker_groupby_time
                                del return_bar
                                del isreplace
                                del sample_result
                                del result_series
                                gc.collect()
                                """ del df_ticker_groupby_time
                                gc.collect() """
                        print("--------df_ticker_groupby_time----countnumber:{}".format(sys.getrefcount(df_ticker_groupby_time)))
                        del df_ticker_groupby_time
                        gc.collect()
                del num_xlsx
                del typicalNDict
                del idx
                del row
                gc.collect()
                NUM_XLSX_BASE = (NUM_XLSX_BASE+5)%20
                RESULT.to_csv(RESULT_DIR+fund_number_filename,index=False)      
        print("--------df_beta----countnumber:{}".format(sys.getrefcount(df_beta)))
        del df_beta
        gc.collect()
#sample_time('Monthly Final Database/','result_monthly/','mean_of_sample_monthly/','Month',0)
sample_time('Daily Final Database/','result_daily/','mean_of_sample_daily/','Names Date',0)
