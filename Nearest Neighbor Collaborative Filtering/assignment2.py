import pandas as pd
import numpy as np
import warnings
import heapq
warnings.filterwarnings("ignore")

df0=pd.read_excel("Assignment 5.xls",sheet_name=0)
l2=df0.iloc[20].tolist()[1:-1]

df0.drop(20,inplace=True)
cols=df0.columns
means=df0[cols[-1]]
df=df0[cols[1:-1]]
df.fillna(0,inplace=True)
u_dic1={}
u_dic2={}
for i in range(20):
  u_dic1[i]=df0.iloc[i,0]
for k,v in u_dic1.items():
  u_dic2[v]=k
m_dic1={}
m_dic2={}
movie_names=df.columns
for i in range(20):
  m_dic1[i]=movie_names[i]
for k,v in m_dic1.items():
  m_dic2[v]=k

#1 Raw Ratings
def cos_sim(c):
  clst=[]
  for i in range(20):
    clst.append(df[cols[i+1]].tolist())
  rlst=[]
  for i in range(20):
    rlst.append(np.dot(clst[i],clst[c])/(l2[i]*l2[c]))
  return rlst

bp=pd.read_excel("Assignment 5.xls",sheet_name=2)
bp.fillna(0,inplace=True)
bcols=bp.columns[1:]
for i in range(20):
  bp[bcols[i]]=cos_sim(i)

def top_similars(movie,n):
  sims=bp.iloc[m_dic2[movie]].tolist()[1:]
  top_sims=[]
  top_movies=[]
  ids=[sims.index(i) for i in heapq.nlargest(n+1,sims)]
  for i in range(n+1):
    top_sims.append(round(sims[ids[i]],n+1))
    top_movies.append(movie_names[ids[i]])
  return list(zip(top_movies,top_sims))[1:]
  
print(movie_names[0])
print(top_similars(movie_names[0],5))
"""
Output:
1: Toy Story (1995)
[('260: Star Wars: Episode IV - A New Hope (1977)', 0.747409), ('780: Independence Day (ID4) (1996)', 0.690665), ('296: Pulp Fiction (1994)', 0.667846), ('318: Shawshank Redemption, The (1994)', 0.667424), ('1265: Groundhog Day (1993)', 0.661016)]
"""
def calc_rating(user,num):
  v0=df.iloc[u_dic2[user]].tolist()
  s0=bp.iloc[num].tolist()[1:]
  s=[]
  for i in range(20):
     if v0[i]==0:
        s.append(0)
     else:
        s.append(s0[i])
  v=[]
  for i in range(20):
     if v0[i]==0:
        v.append(0)
     else:
        v.append(v0[i]-means[u_dic2[user]])
  dp=np.dot(s,v)
  return round(dp/(sum(s))+means[u_dic2[user]],6)

def top_ratings(user,n):
   r_u=[]
   for i in range(20):
     r_u.append(calc_rating(user,i))
   ids=[r_u.index(i) for i in heapq.nlargest(n,r_u)]
   top_movies=[]
   top_ratings=[]
   for i in range(n):
      top_ratings.append(r_u[ids[i]])
      top_movies.append(movie_names[ids[i]])
   res=list(zip(top_movies,top_ratings))
   return res

print(top_ratings(5277,5))
"""
Top 5 Ratings for User 5277:
[("527: Schindler's List (1993)", 2.973883), ('1259: Stand by Me (1986)', 2.928801), ('260: Star Wars: Episode IV - A New Hope (1977)', 2.92224), ('593: Silence of the Lambs, The (1991)', 2.883304), ('2396: Shakespeare in Love (1998)', 2.852131)]
"""

#2 Normalized Ratings
df_n0=pd.read_excel("Assignment 5.xls",sheet_name=1)
l2_n=df_n0.iloc[20].tolist()[1:]
df_n0.drop(20,inplace=True)
cols_n0=df_n0.columns
df_n=df_n0[cols_n0[1:]]
cols_n=df_n.columns

def cos_sim_n(c):
  clst=[]
  for i in range(20):
    clst.append(df_n[cols_n[i]].tolist())
  rlst=[]
  for i in range(20):
    rlst.append(max(np.dot(clst[i],clst[c])/(l2_n[i]*l2_n[c]),0))
  return rlst

bp_n=pd.read_excel("Assignment 5.xls",sheet_name=2)

for i in range(20):
  bp_n[bcols[i]]=cos_sim_n(i)

def top_similars_n(movie,n):
  sims=bp_n.iloc[m_dic2[movie]].tolist()[1:]
  top_sims=[]
  top_movies=[]
  ids=[sims.index(i) for i in heapq.nlargest(n+1,sims)]
  for i in range(n+1):
    top_sims.append(round(sims[ids[i]],n+1))
    top_movies.append(movie_names[ids[i]])
  return list(zip(top_movies,top_sims))[1:]
print(movie_names[0])
print(top_similars_n(movie_names[0],5))
"""
Output:
1: Toy Story (1995)
[('34: Babe (1995)', 0.554448), ('356: Forrest Gump (1994)', 0.35578), ('296: Pulp Fiction (1994)', 0.295013), ('318: Shawshank Redemption, The (1994)', 0.215975), ('2028: Saving Private Ryan (1998)', 0.192799)]
"""
def calc_rating_n(user,num):
  v0=df.iloc[u_dic2[user]].tolist()
  s0=bp_n.iloc[num].tolist()[1:]
  s=[]
  for i in range(20):
     if v0[i]==0:
        s.append(0)
     else:
        s.append(s0[i])
  v=[]
  for i in range(20):
     if v0[i]==0:
        v.append(0)
     else:
        v.append(v0[i]-means[u_dic2[user]])
  dp=np.dot(s,v)
  return round(dp/(sum(s))+means[u_dic2[user]],6)

def top_ratings_n(user,n):
   r_u=[]
   for i in range(20):
     r_u.append(calc_rating_n(user,i))
   ids=[r_u.index(i) for i in heapq.nlargest(n,r_u)]
   top_movies=[]
   top_ratings=[]
   for i in range(n):
      top_ratings.append(r_u[ids[i]])
      top_movies.append(movie_names[ids[i]])
   res=list(zip(top_movies,top_ratings))
   return res

print(top_ratings_n(5277,5))
"""
Top 5 Ratings for User 5277:
[('260: Star Wars: Episode IV - A New Hope (1977)', 4.565822), ("527: Schindler's List (1993)", 4.562483), ('1259: Stand by Me (1986)', 3.602141), ('2396: Shakespeare in Love (1998)', 3.297938), ('593: Silence of the Lambs, The (1991)', 3.22089)]
"""
