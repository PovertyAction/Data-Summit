
# coding: utf-8

# # Imports

# In[2]:


import pandas as pd
import numpy as np
from tqdm import tqdm


# # Data management, organization, manipulation, and basic functionality

# In[3]:


df = pd.read_stata("/Users/JJ/Dropbox/Work-Personal Sync/Misc/Data Summit/cares_deposit_final.dta")


# In[4]:


# df.shape gives you the number of rows and columns of a DataFrame
# range(value) gives you an iterable of every number from 0 to the value
range(df.shape[0])


# In[5]:


# This loops through all the rows and columns in a Dataframe. If a value is of type np.float32 it has 1 added to its value. If it's a string it is capitalized.
for r in tqdm(range(df.shape[0])):
    for c in range(df.shape[1]):
        if type(df.iloc[r,c]) is np.float32:
            df.iloc[r,c] = df.iloc[r,c] + 1
        elif type(df.iloc[r,c]) is str:
            df.iloc[r,c] = df.iloc[r,c].upper()


# In[6]:


# Now we make a function that performs loop above, with an optional custom value, and returns the new DataFrame
def add_val_and_upper(df, x_val = 1): #x_val has a default value of 1
    for r in tqdm(range(df.shape[0])):
        for c in range(df.shape[1]):
            if type(df.iloc[r,c]) is np.float32:
                df.iloc[r,c] = df.iloc[r,c] + x_val
            elif type(df.iloc[r,c]) is str:
                df.iloc[r,c] = df.iloc[r,c].upper()
    return df


# In[7]:


# Here we run our function as a test and see it works.
add_val_and_upper(df, 5)


# In[8]:


# This creates a copy of a DataFrame
data = df.copy()


# In[9]:


# This function was written to add one value to another and return the sum
def add_value(x, x_val):
    y = x+x_val
    return y


# In[10]:


# Here we run our function
add_value(2,3)


# In[11]:


# Here we can create a new column with values 1 greater than another
df['new_col'] = df['cid'] + 1


# In[12]:


# Here we change a value to NaN
df.iloc[0,0] = np.nan


# In[13]:


# This gives us the last five rows of a DataFrame, and assigns it as a new object
last_5 = df[-5:]


# In[14]:


# Here we reset the index of our created DataFrame, and we drop the previous index
last_5.reset_index(drop=True)


# # Data Cleaning

# In[15]:


# This is the equivalent to tab in Stata
df['deposit'].value_counts()


# In[16]:


# Outlier detection, this filters the dataset by removing rows with outliers
df[((df.cid - df.cid.mean()) / df.cid.std()).abs() < 2] # df[(np.abs(stats.zscore(df)) < 3).all(axis=1)] if scipy imported


# In[17]:


# This is a way to drop rows with missing values
df.dropna() # An alternative is to use FancyImpute to impute values; don't use scikit learn's!


# In[18]:


# This is how to replace values or codes
df.replace(21.0, 'Hello') #df.replace('.d', np.nan)


# In[19]:


# Seaborn is a visualization package that extends the matplotlib's package
import seaborn as sns
get_ipython().magic(u'matplotlib inline')

# Scatterplot
sns.lmplot(x='cid', y='deposit', data=df, fit_reg=False, hue='week')


# - Look at this graph!

# In[20]:


sns.set(style="ticks")

# Boxplot
sns.boxplot(x="week", y="deposit", data=df, palette="PRGn")
sns.despine(offset=10, trim=True)


# # Summary statistics / OLS

# In[21]:


# Summary statistics from a dataset
df.describe()


# In[22]:


# Value counts of a field
df['deposit'].value_counts()


# In[23]:


# Ordinary least squares regression
import statsmodels.formula.api as sm
result = sm.ols('week~cid', df).fit()
print(result.summary())

