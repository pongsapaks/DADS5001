# %%
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print( f"Python {sys.version}\nPandas {pd.__version__}\nNumPy {np.__version__}" ) 
# Load the pokemon dataset
df = pd.read_csv('movie_metadata.csv')  
df.shape

# %%
#1. ปัจจัยที่ส่งผลต่อ ค่าrating IMDB (runtime, actor, director, etc. )
df = df.dropna()
df = df.reset_index(drop=True)
df.shape


# %%
df

# %%
df['actor_2_name'].unique()

# %%
df_select = df.drop(['num_critic_for_reviews','director_facebook_likes','actor_3_facebook_likes','actor_1_facebook_likes','cast_total_facebook_likes','facenumber_in_poster','movie_imdb_link','num_user_for_reviews','actor_2_facebook_likes','aspect_ratio','movie_facebook_likes'], axis=1)

# %%
df_select.sort_values('imdb_score', ascending=False )['imdb_score'].unique()

# %%
dfsort = df.sort_values( 'title_year', ascending=False )['title_year'].unique()

# %%
dfsort

# %%
df1 = df[df['movie_facebook_likes'] != 0]


# %%
df2 = df[df['imdb_score'] == 0]


# %%
df.columns

# %%
# Plot Normal distribution : duration
plt.figure(figsize=(10,5))
sns.distplot(df['duration'],kde=False, color=['red'])
plt.title('Distplot with Normal distribution for run time',fontweight="bold")
plt.show()

# %%
plt.figure(figsize=(10,5))
sns.set(style="darkgrid")
px = sns.countplot(x="imdb_score", data=df,palette="Set1",  order=df['imdb_score'].value_counts().index[0:])
plt.title("COUNT OF RATINGS")
px.set_xticks(range(0,10,0.5))

#ต้อง group by rating ก่อนหรอ?

# %%
#2. หนังประเภทไหน มีbudget ในการทำสูง
df2_split = df['genres'].str.split('|', expand=True)
df2_split


# %%
c=["duration","title_year","language", "budget"]
#plt.figure(figsize=(15,7))
for a in c:
    sns.scatterplot(y="gross",x=a,data=df)
   
    
    plt.show()

# %%
g = sns.regplot(x = 'budget', y='gross' , data = df)
# remove the top and right line in graph
sns.despine()
# Set the size of the graph from here
g.figure.set_size_inches(7,5)

# %%
column_data = df2_split.iloc[:, 7]
column_data

# %%
print('Hello')

# %%
column_data.unique()

# %%
#3. หนังที่มี budget สูง จะมี gross profit สูงตามหรือไม่ มี margin เท่าไหร่
df['gross'].plot()   

# %%
plt.figure(figsize=(10,5))
sns.set(style="darkgrid")
px = sns.countplot(x="Rating", data=df,palette="Set1",  order=df['Rating'].value_counts().index[0:])
plt.title("COUNT OF RATINGS")
plt.show()

# %%
plt.figure(figsize=(20,10))
sns.countplot(x='imdb_score',palette =['#f5c518', '#121212','#8b8b8b'], data = df)

#จัด grouping ยังไง?

# %%
#4.หนังของประเทศไหน ได้รับความนิยมสูง

# %%
#5. เทรนด์หนัง ในแต่ละปี



