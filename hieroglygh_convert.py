# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv("data/unicode.txt",delimiter="|",names=["A","B","C"])
str = pd.read_csv("data/input.txt",header=None)

print("------- input text -------")
for i in range(len(str)):
    print(str.iloc[i,0])

print("------- convert  -------")
with open("data/output.txt", mode='w') as f:
    for i in range(len(str)):
        text = str.iloc[i,0]
        output_str = ""
        for j in range(len(text)):
            target_str = 'A == ' + '\"' + text[j] + '\"'
            num = data.reset_index().query(target_str).index[0]
            #print(data.iloc[num,0],data.iloc[num,1])
            output_str += data.iloc[num,1]
        f.write(output_str)
        print(output_str)


