import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

df0=pd.read_excel("Assignment 2.xls")
cols=df0.columns

del df0[cols[11]]
del df0[cols[13]]
del df0[cols[16]]
del df0[cols[17]]
del df0[cols[18]]
df0.drop(20,inplace=True)
df0.drop([22,23,24,25,26],inplace=True)
df=df0.copy()
df.fillna(0,inplace=True)
buzz=df.columns[1:-3]

users=pd.DataFrame(columns=buzz,index=["User 1","User 2"])

for i in range(len(buzz)):
  users.loc["User 1",buzz[i]]=np.dot(df["User 1"],df[buzz[i]])
  users.loc["User 2",buzz[i]]=np.dot(df["User 2"],df[buzz[i]])
dlst=[]
for i in range(20):
  dlst.append(df.iloc[i,1:11].tolist())
p1=users.loc["User 1"].tolist()
p2=users.loc["User 2"].tolist()
vals1_1=[]
vals2_1=[]
for i in range(20):
  vals1_1.append(np.dot(dlst[i],p1))
  vals2_1.append(np.dot(dlst[i],p2))

df2=df.copy()
df2.drop(21,inplace=True)
df2["fac"]=1/df2["num-attr"]**0.5
for i in range(len(buzz)):
  df2[buzz[i]]=df2["fac"]*df2[buzz[i]]
dlst2=[]
users2=pd.DataFrame(columns=buzz,index=["User 1","User 2"])

for i in range(len(buzz)):
  users2.loc["User 1",buzz[i]]=np.dot(df2["User 1"],df2[buzz[i]])
  users2.loc["User 2",buzz[i]]=np.dot(df2["User 2"],df2[buzz[i]])
p1_n=users2.loc["User 1"].tolist()
p2_n=users2.loc["User 2"].tolist()


for i in range(20):
  dlst2.append(df2.iloc[i,1:11].tolist())
vals1_2=[]
vals2_2=[]
for i in range(20):
  vals1_2.append(round(np.dot(dlst2[i],p1_n),5))
  vals2_2.append(round(np.dot(dlst2[i],p2_n),5))

DF=df.iloc[20,1:11].tolist()
idf=[]
for i in range(len(DF)):
  idf.append(1/DF[i])

df3=df2.copy()
users3=pd.DataFrame(columns=buzz,index=["User 1","User 2"])
dlst3=[]
for i in range(len(buzz)):
  users3.loc["User 1",buzz[i]]=np.dot(df3["User 1"],df3[buzz[i]])*idf[i]
  users3.loc["User 2",buzz[i]]=np.dot(df3["User 2"],df3[buzz[i]])*idf[i]

p1_n_idf=users3.loc["User 1"].tolist()
p2_n_idf=users3.loc["User 2"].tolist()


for i in range(20):
  dlst3.append(df3.iloc[i,1:11].tolist())

vals1_3=[]
vals2_3=[]
for i in range(20):
  vals1_3.append(round(np.dot(dlst3[i],p1_n_idf),5))
  vals2_3.append(round(np.dot(dlst3[i],p2_n_idf),5))

docs=["doc1","doc2","doc3","doc4","doc5",
"doc6","doc7","doc8","doc9","doc10","doc11","doc12","doc13","doc14","doc15","doc16","doc17","doc18","doc19","doc20"
]
result=pd.DataFrame(columns=docs,index=["User 1 (basic)","User 2 (basic)","User 1 (normed)","User 2 (normed)","User 1 (n. and idf)","User 2 (n. and idf)"])
result.loc["User 1 (basic)"]=vals1_1
result.loc["User 2 (basic)"]=vals2_1
result.loc["User 1 (normed)"]=vals1_2
result.loc["User 2 (normed)"]=vals2_2
result.loc["User 1 (n. and idf)"]=vals1_3
result.loc["User 2 (n. and idf)"]=vals2_3
result.to_csv("result.csv")
