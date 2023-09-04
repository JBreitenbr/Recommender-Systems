import pandas as pd
import numpy as np
import warnings
import heapq
warnings.filterwarnings("ignore")

svd0=pd.read_excel("Assignment-6.xls",sheet_name=0)
weights=svd0.iloc[0].tolist()[2:]
svd0.drop(0,inplace=True)
nrs=svd0["Unnamed: 0"].tolist()[1:]
movies=svd0["Unnamed: 1"].tolist()[1:]
fac1=svd0[1].tolist()[1:]
fac1_mv=[]
top_fac1=[]
ids1=[fac1.index(i) for i in heapq.nlargest(5,fac1)]
for i in range(5):
  fac1_mv.append(movies[ids1[i]])
  top_fac1.append(round(fac1[ids1[i]],6))
res1=list(zip(fac1_mv,top_fac1))
print(res1)
"""
Output:
[("Charlie's Angels (2000)", 0.28199), ('Batman Forever (1995)', 0.218089), ('Ace Ventura: Pet Detective (1994)', 0.190879), ('Dumb & Dumber (1994)', 0.190638), ('The Mask (1994)', 0.158601)]
"""

fac2=svd0[2].tolist()[1:]
fac2_mv=[]
top_fac2=[]
ids2=[fac2.index(i) for i in heapq.nlargest(5,fac2)]
for i in range(5):
  fac2_mv.append(movies[ids2[i]])
  top_fac2.append(round(fac2[ids2[i]],6))
res2=list(zip(fac2_mv,top_fac2))
print(res2)

"""
Output:
[('American Beauty (1999)', 0.198715), ('Pulp Fiction (1994)', 0.189565), ('Kill Bill: Vol. 1 (2003)', 0.18157), ('Fargo (1996)', 0.161559), ('Eternal Sunshine of the Spotless Mind (2004)', 0.161058)]
"""

svd1=pd.read_excel("Assignment-6.xls",sheet_name=1)
users=svd1["User"]

svd0.iloc[1].tolist()
mv_dims=[]
for i in range(100):
  mv_dims.append(svd0.iloc[i+1].tolist()[2:])

u_dic1={}
for i in range(25):
  u_dic1[i]=int(svd1.iloc[i].tolist()[0])
u_dic2={}
for k,v in u_dic1.items():
  u_dic2[v]=k

def scores(user):
  scores=[]
  a=svd1.iloc[u_dic2[user]].tolist()[1:]
  for i in range(100):
    score=0
    for j in range(15):
      score+=mv_dims[i][j]*a[j]*weights[j]
    scores.append(score)
  return scores

def top_5(user):
  lst=scores(user)
  sc=[]
  mv=[]
  ids=[lst.index(i) for i in heapq.nlargest(5,lst)]
  for i in range(5):
    mv.append(str(nrs[ids[i]])+": "+str(movies[ids[i]]))
    sc.append(round(lst[ids[i]],6))
  return list(zip(mv,sc))
print(top_5(4469))
"""
Output:
[('278: The Shawshank Redemption (1994)', 0.20768), ('453: A Beautiful Mind (2001)', 0.183286), ('98: Gladiator (2000)', 0.173611), ('238: The Godfather (1972)', 0.17218), ('13: Forrest Gump (1994)', 0.170744)]
"""
