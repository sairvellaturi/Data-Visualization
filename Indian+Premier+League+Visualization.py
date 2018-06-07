
# coding: utf-8

# In[223]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[224]:


df = pd.read_csv(r"C:\Users\Ravi Teja\Desktop\Datasets\ipldata\matches.csv")
df.head()


# Winning team data frame is taken from original dataframe

# In[225]:


win_df = df[['team1','team2','winner']]
win_df.head()


# ### List of Teams:

# In[226]:


teams = df.team1.unique()
print(teams)


# ### Calculating win percentage

# In[227]:


winPercent = []
      
for each_team in teams:
    played_matches = np.count_nonzero(df['team1'].astype(str).str.contains(each_team)) + np.count_nonzero(df['team2'].astype(str).str.contains(each_team))
    matches_won = np.count_nonzero(df['winner'].astype(str).str.contains(each_team))   
    winPercent.append(100 * (matches_won / played_matches))


# ### Win percantage for every team in tabular form

# In[228]:


win = pd.DataFrame({'Team': teams, 'Win Percantge': winPercent})
print (win)


# ### Plot to show all the in percentages:

# In[229]:


plt.style.use('Solarize_Light2')
plt.figure(figsize=(12,6))
plt.barh(range(len(winPercent)), winPercent, align='center')
plt.yticks(range(len(winPercent)), teams)
plt.title("IPL Teams: Winning Percentage")
plt.show()


# ### Sorting and plotting according to Win percentage

# In[230]:


winPercent, teams = zip(*sorted(zip(winPercent, teams)))


# In[231]:


plt.style.use('Solarize_Light2')
plt.figure(figsize=(12,6))
plt.barh(range(len(winPercent)), winPercent, align='center')
plt.yticks(range(len(winPercent)), teams)
plt.title("IPL Teams: Winning Percentage")
plt.show()


# ### Does toss really matter? 

# In[232]:


toss_df = df[['toss_winner','winner']]
toss_df.head()


# In[233]:


#counting the total matches
toss_df.count()


# In[234]:


#cleaning the data by dropping empty rows
toss_df1 = toss_df.dropna()
toss_df1.count()


# In[235]:


#Count of the matches where toss winner won the match
toss_df1[toss_df1.winner == toss_df1.toss_winner].count()
            


# In[236]:


#Count of the matches where toss loser won the match
toss_df1[toss_df1.winner != toss_df1.toss_winner].count()


# In[250]:


x_list = [357, 336]
label_list = ["Toss won", "Toss lost"]

plt.axis("equal")
plt.pie(x_list,
        labels=label_list, autopct = '%f%%')
plt.title("Toss influence on match")
plt.show()


# #### So from the above data we can conclude that toss does not influence the chance of winning the match

# ### Most matches won
# 
# Here let us look at the visual representation of matches won by each team

# In[283]:


df['winner'].value_counts().plot.bar(figsize=(12, 6),title='Matches won')
plt.style.use('Solarize_Light2')
plt.show()


# ### Most "Player of the Match awards"
# 
# From this dataset, we can understand the performances of individual players and can rate the best of lot

# Make a list with player and append all the players of the matches into it

# In[342]:


# making a list and using list comprehension to get a list of player of the matches
player = []
for i in df.player_of_match:
       player.append(i)


# In[343]:


#importing counter from collections
from collections import Counter


# In[300]:


#using counter to count no. of awards each player got and listing out the highest ones
X = (Counter(player))
X.most_common(10)


# In[348]:


# listing out the best players and a visual representation of no. of awards
labels, values = zip(*X.most_common(10))
indexes = np.arange(len(labels))
width = 0.5

plt.barh(indexes, values, width)
plt.title('Most Player of the matches')
plt.yticks(indexes + width * 0.1, labels)
plt.show()

