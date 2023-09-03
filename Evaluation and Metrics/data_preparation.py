import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")
df0=pd.read_excel("Metric-SpreadSheet-Assignment.xlsx",sheet_name=0)
lst0=df0.iloc[0].tolist()
lst0[0]="User"
lst0[-1]="MAE"
lst0[-3]="#"
df0.columns=lst0
del df0["#"]
df0.drop(0,inplace=True)

pt1=df0.iloc[0:10,:]
pt2=df0.iloc[14:24,:]
pt=pd.concat([pt1,pt2],ignore_index=True)
maes1=[]
mses1=[]
rmses1=[]
# number of ratings by user
anz1=df0["Rating Count"].tolist()[0:10]
for j in range(10):
  mae1=0
  mse1=0
  lst1=pt.iloc[j].tolist()[:-2]
  lst2=pt.iloc[j+10].tolist()[:-2]
  for i in range(11):
    if not np.isnan(lst1[i]):
       mae1+=abs(lst1[i]-lst2[i])
       mse1+=(lst1[i]-lst2[i])**2
  maes1.append(round(mae1/anz1[j],6))
  mses1.append(round(mse1/anz1[j],6))
  rmses1.append(round((mse1/anz1[j])**0.5,6))
pt1["MAE"]=maes1
pt1["MSE"]=mses1
pt1["RMSE"]=rmses1

# number of ratings for movie
maes2=[]
mses2=[]
rmses2=[]
anz2=df0.iloc[11].tolist()[1:-2]
movie_cols=pt1.columns[1:-2]
for j in range(10):
  mae2=0
  mse2=0
  lst3=pt1[movie_cols[j]].tolist()
  lst4=pt2[movie_cols[j]].tolist()
  for i in range(10):
    if not np.isnan(lst3[i]):
      mae2+=abs(lst3[i]-lst4[i])
      mse2+=(lst3[i]-lst4[i])**2
  maes2.append(round(mae2/anz2[j],6))
  mses2.append(round(mse2/anz2[j],6))
  rmses2.append(round((mse2/anz2[j])**0.5,6))

tr=pt1.T
users=pt1["User"].tolist()
tr.columns=users
tr.drop(["User","Rating Count","MAE","MSE","RMSE"],inplace=True)
tr.index.name="Movie"
tr["MAE"]=maes2
tr["MSE"]=mses2
tr["RMSE"]=rmses2
tr.to_csv("by_movie.csv")

# MAE concerning all predictions
cols=pt1.columns
r=[] #ratings
p=[] #predictions
for i in range(10):
  for j in range(10):
    r.append(pt1[cols[i+1]].tolist()[j])
    p.append(pt2[cols[i+1]].tolist()[j])
dic1={}
dic1["ratings"]=r
dic1["predictions"]=p
pr=pd.DataFrame(dic1)
corr=round(pr.corr().iloc[0,1],6)
mae_total=0
mse_total=0
mrse_total=0
for i in range(len(r)):
  if not np.isnan(r[i]):
    mae_total+=abs(r[i]-p[i])
    mse_total+=(r[i]-p[i])**2
mae_total=round(mae_total/sum(anz1),6)
mse_total=round(mse_total/sum(anz1),6)
mrse_total=round(mse_total**0.5,6)

# MAE by user
mae_by_user=pt1["MAE"].mean()

# MAE by movie
mae_by_movie=tr["MAE"].mean()

dic2={}
dic2["MAE total"]=mae_total
dic2["MAE by user"]=mae_by_user
dic2["MAE by movie"]=mae_by_movie
dic2["MSE total"]=mse_total
dic2["RMSE total"]=mrse_total
dic2["Correlation total"]=corr
mets=pd.DataFrame(dic2,index=["Metrics"])
mets.to_csv("overall_metrics.csv",index=False)
tr2=pt2.T
users2=pt2["User"].tolist()
for i in range(10):
  users2[i]=str(users2[i])+"_"
tr2.columns=users2
tr2.drop(["User","Rating Count","MAE"],inplace=True)
tr2.index.name="Movie"
corrs=[]
for i in range(10):
  c1=tr[users[i]]
  c2=tr2[users2[i]]
  tst=pd.DataFrame([c1,c2])
  T=tst.T
  c=round(T.corr().iloc[0,1],6)
  corrs.append(c)
pt1["corr"]=corrs
pt1.to_csv("by_user.csv",index=False)
      
       
  
  










  

