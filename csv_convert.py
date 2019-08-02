# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv("data/unicode.txt",delimiter="|",header=None,names={"A","B","C"})
str = pd.read_csv("data/input.txt",header=None)
text = str.iloc[1,0]
print(data['B'])


print(str)
for i in range(len(str)):
    text = str.iloc[i,0]
    output_str = ""
    for j in range(len(text)):
        target_str = 'B == ' + '\"' + text[j] + '\"'
        num = data.reset_index().query(target_str).index[0]
        #print(data.iloc[num,0],data.iloc[num,1])
        output_str += data.iloc[num,1]
    print(output_str)
