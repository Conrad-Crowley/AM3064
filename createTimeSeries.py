import pandas as pd
import glob

path = './individual_stocks/' 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    # take time and closing prices
    df = pd.read_csv(filename, index_col=None, header=0, usecols=[0,4])
    # reverse order of list to give newest first
    # purpose of this is to account for diffent lengths of time series
    df = df.iloc[::-1].reset_index(drop=True)
    li.append(df)

frame = pd.concat(li, axis=1, ignore_index=True)
frame.to_csv('output.csv')