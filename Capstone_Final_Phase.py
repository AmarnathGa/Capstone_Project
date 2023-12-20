#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


# Reading CSV files into separate DataFrames


# In[2]:


df1 = pd.read_csv("Table_1.csv")
df2 = pd.read_csv("Table_2.csv")
df3 = pd.read_csv("Table_3.csv")


# In[3]:


result_df = pd.merge(df1, df2,)


# In[5]:


result_df


# In[8]:


Final_df = pd.merge(result_df,df3)


# In[7]:


df3


# In[9]:


Final_df


# In[10]:


Final_df.to_csv('Table_Final.csv')
Final_df=pd.read_csv('Table_Final.csv')


# In[11]:


df = pd.read_csv("Table_Final.csv")


# In[12]:


df


# In[257]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[99]:


df.shape


# In[100]:


df.head(20)


# In[101]:


df.info()


# In[ ]:





# In[ ]:


#Removing null colums


# In[ ]:





# In[102]:


df.drop(["Unnamed: 0"], axis=1, inplace=True)


# In[103]:


df.info()


# In[104]:


pd.isnull(df).sum()


# In[105]:


df.shape


# In[106]:


df.head(5)


# In[ ]:





# In[ ]:


#Changing datatype for Shoe_Price from Float to int


# In[24]:


df["Shoe_Price"] = df["Shoe_Price"].astype('int')


# In[107]:


df.info()


# In[ ]:


#combined check for the data


# In[108]:


df.describe()


# In[109]:


df.head(10)


# In[ ]:





# # Bar Plot for the Shoe Price and the star ratings shared

# In[ ]:





# In[112]:


sns.barplot(x='Star_Rate', y='Shoe_Price', data=df)
sns.set(rc={'figure.figsize':(70,70)})


# In[ ]:





# The analysis reveals a positive correlation between star ratings and shoe prices, indicating that higher-rated shoes tend to command higher prices, reflecting consumer value perception and quality satisfaction.

# In[ ]:





# In[ ]:





# # Pie Chart for the reviews shared by customers

# In[ ]:





# 

# In[ ]:





# In[119]:


Star_Rate_counts = df['Star_Rate'].value_counts()
plt.pie(Star_Rate_counts, labels=Star_Rate_counts.index)
plt.axis('equal')
plt.title('Distribution of star_ratings')
plt.figure(figsize=(40,40))
plt.show()


# #PieChart for the star rating for shoes where it seems that most of the shoes fall between range of 4-5 on star rating
# #Approximately 25% of Shoes do not have any reviews from customers

# # Pie Chart for the Comfort levels that has been shown

# In[81]:





# In[ ]:





# In[120]:


Comfort_counts = df['Comfort'].value_counts()
plt.pie(Comfort_counts, labels=Comfort_counts.index)
plt.axis('equal')
plt.title('Distribution of Comfort')
plt.figure(figsize=(50,50))
plt.show()


# #After conducting a comprehensive analysis of the comfort ratings for various shoe models
# #it is evident that a majority of the surveyed customers highly favor and praise the exceptional comfort levels.

# In[ ]:





# # Bar plot for the Shoe Price and Comfort levels

# In[ ]:





# In[ ]:





# In[79]:


sns.barplot(x='Comfort', y='Shoe_Price', data=df)
sns.set(rc={'figure.figsize':(70,70)})


# #After the analysis that we made, it is clear that as the price of the shoe increases the comfort level also increases and demonstrates a positive relationship.

# In[ ]:





# In[ ]:





# # Top 10 shoes with highest Price

# In[ ]:





# In[ ]:





# In[122]:


top_shoes = df.groupby(['Shoe_Name'], as_index=False)['Shoe_Price'].sum().sort_values(by='Shoe_Price', ascending=False).head(10)
sns.barplot(data=top_shoes, x='Shoe_Price',y='Shoe_Name')
sns.set(rc={'figure.figsize':(50,85)})


# #The top 10 shoes with the highest prices showcase premium quality, exquisite designs, and exclusive features, appealing to a luxury-seeking consumer base.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Phase 4         Machine Learning Price Prediction

# In[143]:


data.info()


# In[152]:


data.head()


# In[239]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error


# In[241]:


data


# In[242]:


model = LinearRegression()


# In[243]:


X = data.drop('Shoe_Price', axis=1)
y = data['Shoe_Price']


# In[255]:


preprocessor = ColumnTransformer(
    transformers=[
        ('stylecode', ['Style_code']),
        ('imputer', SimpleImputer(strategy='mean'), ['Colour1', 'Colour2'])
    ],
    remainder='passthrough'
)


# In[251]:


model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])


# In[252]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[254]:


model.fit(X_train, y_train)


# In[253]:


y_pred = model.predict(X_test)


# In[261]:


data


# In[263]:


x= data["Shoe_Price"]

plt.figure(figsize=(9,7))

plt.scatter(x,y,color="red", label='Data Points')
plt.xlabel('Shoe_Price')

plt.legend()
plt.grid(True)
plt.show()


# In[264]:


x= data["Star_Rate"]

plt.figure(figsize=(9,7))

plt.scatter(x,y,color="blue", label='Data Points')
plt.xlabel('Star_Rate')

plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




