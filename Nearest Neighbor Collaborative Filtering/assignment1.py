import numpy as np
import pandas as pd
import warnings
import heapq
warnings.filterwarnings("ignore")
df0=pd.read_excel("UUCF Assignment Spreadsheet.xls",sheet_name=0)
cols0=df0.columns
df=df0[cols0[1:]]
cols=df.columns
corr=df.corr()

d1={}
for i in range(25):
  d1[i]=cols[i]
d2={}
for k,v in d1.items():
  d2[v]=k

def top_5_neighbors(user_id):
  top_neighbors=[]
  top_corrs=[]
  lst=corr[user_id].tolist()
  res=[lst.index(i) for i in heapq.nlargest(6,lst)]
  for i in range(6):
    top_neighbors.append(d1[res[i]])
    top_corrs.append(lst[res[i]])
  return (top_neighbors[1:],top_corrs[1:])
movies=df0[cols0[0]].tolist()

# Part 1 - Without Normalization
def pred_rating(user_id,row):
  tops=top_5_neighbors(user_id)
  weights=0
  ratings=0
  for i in range(5):
    if not np.isnan(df0[tops[0][i]][row]):
      weights+=tops[1][i]
      ratings+=tops[1][i]*df0[tops[0][i]][row]
  if weights!=0:
    return round(ratings/weights,4)
  else:
    return 0

def top_movies(user_id,n):
  all_ratings=[]
  top_ratings=[]
  movie_names=[]
  for i in range(100):
    all_ratings.append(pred_rating(user_id,i))
  ids=[all_ratings.index(i) for i in heapq.nlargest(n,all_ratings)]
  for i in range(n):
    top_ratings.append(all_ratings[ids[i]])
    movie_names.append(movies[ids[i]])
  zipped=zip(movie_names,top_ratings)
  return list(zipped)
  
print(top_movies(3867,3))
"""
Output:
[('1891: Star Wars: Episode V - The Empire Strikes Back (1980)', 4.7603), ('155: The Dark Knight (2008)', 4.5515), ('122: The Lord of the Rings: The Return of the King (2003)', 4.5076)]
"""
print(top_movies(89,3))
"""
Output:
[('238: The Godfather (1972)', 4.8941), ('278: The Shawshank Redemption (1994)', 4.8822), ('807: Seven (a.k.a. Se7en) (1995)', 4.7741)]
"""

# Part 2 - With Normalization
def avg_rating(user_id):
  return round(df[user_id].mean(),4)

def pred_rating_nm(user_id,row):
  tops=top_5_neighbors(user_id)
  weights=0
  ratings=0
  for i in range(5):
    if not np.isnan(df0[tops[0][i]][row]):
      weights+=tops[1][i]
      ratings+=tops[1][i]*(df0[tops[0][i]][row]-avg_rating(tops[0][i]))
  if weights!=0:
    return round(ratings/weights,4)+avg_rating(user_id)
  else:
    return avg_rating(user_id)

def top_movies_nm(user_id,n):
  all_ratings=[]
  top_ratings=[]
  movie_names=[]
  for i in range(100):
    all_ratings.append(pred_rating_nm(user_id,i))
  ids=[all_ratings.index(i) for i in heapq.nlargest(n,all_ratings)]
  for i in range(n):
    top_ratings.append(all_ratings[ids[i]])
    movie_names.append(movies[ids[i]])
  zipped=zip(movie_names,top_ratings)
  return list(zipped)

print(top_movies_nm(3867,3))
"""
Output:
[('1891: Star Wars: Episode V - The Empire Strikes Back (1980)', 5.2455), ('155: The Dark Knight (2008)', 4.8567), ('77: Memento (2000)', 4.7778)]
"""

print(top_movies_nm(89,3))
"""
Output:
[('238: The Godfather (1972)', 5.322), ('278: The Shawshank Redemption (1994)', 5.2614), ('275: Fargo (1996)', 5.2411)]
"""

