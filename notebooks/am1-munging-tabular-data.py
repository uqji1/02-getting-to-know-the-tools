
# coding: utf-8

# # Munging tabular data
# 
# We're going to go through how to munge tabular data in more detail (and _slowly_). The aim is for you to get comfortable with the tools we're using:
# 
# - [pandas](pandas.pydata.org) for data handling (our dataframe library)
# - [seaborn](seaborn.pydata.org) for _nice_ data visualization
# - [scipy](scipy.org) for scientific libraries (particularly `scipy.stats` which we'll use for fitting some more unusual probability distributions), and 
# - [statsmodels](statsmodels.org) which gives us some more expressive curve fitting approaches
# 
# The other aim is to get familiar with code-sharing workflows - so we will be doing pair programming for the duration of the day! _You will probably want to take a moment to look at the documentation of the libraries above - especially pandas_
# 
# The other useful resource is Stack Overflow - if you have a question that sounds like 'how do I do {x}' then someone will probably have answered it on SO. Questions are also tagged by library so if you have a particular pandas question you can do something like going to https://stackoverflow.com/questions/tagged/pandas (just replace the 'pandas' in the URL with whatever library you're trying to use.
# 
# Generally answers on SO are probably a lot closer to getting you up and running than the documentation. Once you get used to the library then the documentation is generally a quicker reference. We will cover strategies for getting help in class.
# 
# ## Git links
# 
# We will be working through using GitHub and GitKraken to share code between pairs. We will go through all the workflow in detail in class but here are some useful links for reference:
# 
# - GitKraken interface basics: https://support.gitkraken.com/start-here/interface
# - Staging and committing (save current state -> local history): https://support.gitkraken.com/working-with-commits/commits
# - Pushing and pulling (sync local history <-> GitHub history): https://support.gitkraken.com/working-with-repositories/pushing-and-pulling
# - Forking and pull requests (request to sync your GitHub history <-> someone else's history - requires a _review_):
#   - https://help.github.com/articles/about-forks/
#   - https://help.github.com/articles/creating-a-pull-request-from-a-fork/
# 
# ## Step 1: Reading my data
# 
# In pairs work out how to read your data into a pandas dataframe.
# 
# If you have your own tabular data please start using it here. If not, use the ATCO dataset from last week.

# In[5]:


import pandas as pd
import os
from os import path

# your code goes here
os.getcwd()


# In[6]:


data_folder = path.join(
    path.abspath('..'),  # '..' means the directory above this one
    'data')
data_folder


# In[7]:


os.listdir(data_folder)


# Once you've worked this out in the Jupyter notebook, transfer your code to a Python script (say a function called `load_data` in a file called `munging.py` in the same directory as the notebooks - you can create a text file in the Jupyter notebook home screen). Then try importing your load function with 
# 
# ```python 
# from munging import load_data
# 
# df = load_data('path/to/datafile')
# ```

# In[8]:


# This points to the location of the fault data file on my computer
fault_file = path.join(data_folder, 'Mains Faults Data_SAP_2010-2016.xlsx')

# First we need to see what sheets we have available in the book
faults_xl = pd.ExcelFile(fault_file)
faults_xl.sheet_names


# In[9]:


df = faults_xl.parse('All Notifications_2010-2016')

df.set_index('Notification')

df.head()


# Next work out how to access a column within your dataframe. 
# 
# - How can you list all the column names? 
# - There are two ways to access columns by name - try to find out what both of these are. 
# - There's also methods to access columns by number - try to do this as well
# 
# Next look at how to access rows - both using labels and numbers.

# In[14]:


df.columns[0]


# In[59]:


(df.set_index('Notification'))['Code group'].iloc[4:25]


# To access records efficiently pandas can construct an index for your data. Find out how you set the index on your dataframe and pick a useful column (i.e. one that has a unique value for each record and can be sorted) and set this as the index.
# 
# Try selecting data using your index (especially if you have a timeseries index)

# In[39]:


df.set_index('Notification')


# In[52]:


df.loc[0:5]


# If you get through this quickly, take a look at the [other data formats that pandas is able to read](http://pandas.pydata.org/pandas-docs/stable/api.html#input-output) and find out about these online - we can have a discussion about when you might like to use them. Pay particular attention to [`pandas.read_sql`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql.html#pandas.read_sql) as that's pretty useful for ripping data from databases.
# 
# Go to [data.gov.au](https://data.gov.au) and find some other data in different formats to read and try reading it.
# 
# ## Step 2: What's in my data?
# 
# First find the documentation in pandas on datatypes!
# 
# Work through the columns in your dataset and assign them to the correct datatype.

# How will you find incorrect values in your data? Can you write a small function to test these? For more details on Python functions you can work through [this little tutorial on DataCamp](https://www.datacamp.com/community/tutorials/functions-python-tutorial)
# 
# Also take a look at the [`apply`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) method for more tricky data munging that has to be carried out record-by-record
# 
# Try writing a small function to apply to one of the columns in your dataframe - here's a toy example to get you started: your function could look something like:
# 
# ```python
# import random
# import pandas
# 
# # Make some bogus data - see random_data.py for defns
# from random_data import random_dataframe
# 
# df = random_dataframe(10)
# 
# # Define our bogus function
# def random_replacement(record):
#     "Some of column 'a', some of column 'b'"
#     return random.sample([record.a, record.b], 1)[0]
# 
# # Apply function once per record
# df.apply(random_replacement, axis='columns')
# ```
# 
# Work out how to apply a function once per column as well.

# ### Step 3: Tidy my data
# 
# Work through the 'tidy data checklist' and make sure your data has been tidied!
# 
# 1. Each variable you measure should be in one column.
# 2. Each different observation of that variable should be in a different row.
# 3. There should be one table for each "kind" of variable.
# 4. If you have multiple tables, they should include a column in the table that allows them to be linked.
# 
# This is a good overview: http://www.jeannicholashould.com/tidy-data-in-python.html
# 
# If your data is already tidy, try downloading the data from that tutorial and working through it instead.

# Once you're done with this, copy your code from steps 2 and 3 over to a Python script for easier sharing. This is an example of an extract-transform-load workflow that you could share with your IT department to run automatically when your org collects more data that is similar to this.
