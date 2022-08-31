import numpy as np 
import pandas as pd 

raw_df = pd.read_csv('data\cups.csv')
df = raw_df.drop(['third','fourth'], axis=1)

print(df)
print(df.columns)

#employee_1은 여기서부터 작업해주세요! 
#네 알겠습니다! 여기서부터 작업하겠습니다!

print(df[df["goals_scored"]>100])

#여기서 조금만 수정해 보겠습니다. 
