import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df0=pd.read_csv("HW1-data.csv")
df=df0.copy()
cols=df.columns

#1 Top Movies by Mean Rating
del df[cols[0]]
del df[cols[1]]
means=df.apply(lambda x: x.mean(),axis=0).sort_values(ascending=False).iloc[0:3]
print(means)
"""
Output:
318: Shawshank Redemption, The (1994)             3.600000
260: Star Wars: Episode IV - A New Hope (1977)    3.266667
541: Blade Runner (1982)                          3.222222
dtype: float64
"""

#2 Top Movies by Count of Ratings
cnts=df.apply(lambda x:20- x.isna().sum()).sort_values(ascending=False).iloc[0:3]
print(cnts)
"""
Output:
1: Toy Story (1995)                               17
593: Silence of the Lambs, The (1991)             16
260: Star Wars: Episode IV - A New Hope (1977)    15
dtype: int64
""" 

#3 Top Movies by Percent Liking
# ('Liking' means a rating of at least 4 points)
def hlmpf(lst):
  goods=0
  valued=0
  for i in range(len(lst)):
    if lst[i]>3:
      goods+=1
    elif lst[i]>0:
      valued+=1
  return goods/(valued+goods)

pos_perc=df.apply(hlmpf,axis=0).sort_values(ascending=False).iloc[0:3]
print(pos_perc)
"""
Output:
318: Shawshank Redemption, The (1994)             0.700000
260: Star Wars: Episode IV - A New Hope (1977)    0.533333
3578: Gladiator (2000)                            0.500000
dtype: float64
"""

#4 Association Score
df2=df.fillna(0)
toy_st=df2[cols[8]]

def ass_score(lst):
  cvar=0
  for i in range(len(lst)):
    cvar+=min(lst[i]*toy_st[i],1)
  return cvar/17

assoc=df2.apply(ass_score,axis=0).sort_values(ascending=False).iloc[[1,2,4]]
print(assoc)
"""
Output:
260: Star Wars: Episode IV - A New Hope (1977)    0.823529
593: Silence of the Lambs, The (1991)             0.764706
780: Independence Day (ID4) (1996)                0.764706
dtype: float64
"""

#5 Correlation with 'Toy Story'
def corrs(col):
  pt=df[[cols[8],col]].corr()
  return pt.iloc[0,1]

corr_vec=[]
for i in range(2,22):
  corr_vec.append(corrs(cols[i]))

corr_ser=pd.DataFrame(corr_vec)
titles=pd.DataFrame(cols[2:22])
corr_df=pd.merge(titles,corr_ser,left_index=True,right_index=True)
corr_df.columns=["title","corr"]
sorted=corr_df.sort_values(by="corr",ascending=False)
print(sorted.iloc[1:4])
"""
Output:
title      corr
3   318: Shawshank Redemption, The (1994)  0.888523
19                        34: Babe (1995)  0.811107
8                296: Pulp Fiction (1994)  0.709842
"""

#6 Male-female differences in average rating
df_gen=df0.copy()
del df_gen[cols[0]]
f=df_gen[df_gen[cols[1]]==1]
m=df_gen[df_gen[cols[1]]==0]
del f[cols[1]]
del m[cols[1]]
means_f=pd.DataFrame(f.apply(lambda x: x.mean()))
means_m=pd.DataFrame(m.apply(lambda x: x.mean()))
means_df=pd.merge(means_f,means_m,left_index=True,right_index=True)
means_df.columns=["f","m"]
means_df["diff(f-m)"]=means_df["f"]-means_df["m"]
# Which movie rate female raters the highest above male raters?
print(means_df.sort_values(by="diff(f-m)",ascending=False).iloc[0])
"""
Output:
f            4.250000
m            2.142857
diff(f-m)    2.107143
Name: 2396: Shakespeare in Love (1998), dtype: float64
"""

means_df["diff(m-f)"]=means_df["m"]-means_df["f"]
del means_df["diff(f-m)"]
# Which movie rate male raters the highest above female raters?
print(means_df.sort_values(by="diff(m-f)",ascending=False).iloc[0])
"""
Output:
f            2.000000
m            3.666667
diff(m-f)    1.666667
Name: 1198: Raiders of the Lost Ark (1981), dtype: float64
"""
f_ratings=f[cols[2]].tolist()
for i in range(3,22):
  f_ratings+=f[cols[i]].tolist()
t1=pd.DataFrame(f_ratings)

m_ratings=m[cols[2]].tolist()
for i in range(3,22):
  m_ratings+=m[cols[i]].tolist()
t2=pd.DataFrame(m_ratings)
# What is the difference of the average female rating overall and the average male rating overall?
print(t1[0].mean()-t2[0].mean())
"""
Output:
0.0418566100290092
"""
#7 Male-female difference by percent liking
f.reset_index(inplace=True)
m.reset_index(inplace=True)
perc_f=pd.DataFrame(f.apply(hlmpf,axis=0))
perc_m=pd.DataFrame(m.apply(hlmpf,axis=0))
perc_df=pd.merge(perc_f,perc_m,left_index=True,right_index=True)
perc_df.columns=["f","m"]
perc_df["perc(f-m)"]=perc_df["f"]-perc_df["m"]
# What movie has the biggest difference conc. the liking percentage between female and male raters?
print(perc_df.sort_values(by="perc(f-m)",ascending=False).iloc[0])
"""
Output:
f            0.75
m            0.00
perc(f-m)    0.75
Name: 2396: Shakespeare in Love (1998), dtype: float64
"""
perc_df["perc(m-f)"]=perc_df["m"]-perc_df["f"]
del perc_df["perc(f-m)"]
# What movie has the biggest difference conc. the liking percentage between male and female raters?
print(perc_df.sort_values(by="perc(m-f)",ascending=False).iloc[0])
"""
Output:
f            0.0
m            0.5
perc(m-f)    0.5
Name: 1198: Raiders of the Lost Ark (1981), dtype: float64
"""

# What is the difference of the  female rating overall and male rating overall conc. liking percentage?
print(hlmpf(t1[0])-hlmpf(t2[0]))
"""
Output:
0.082469954413593
m[cols[20]].to_csv("m20.csv")
"""
