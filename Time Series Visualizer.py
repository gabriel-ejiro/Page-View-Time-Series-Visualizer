#!/usr/bin/env python
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


df = r"C:\Users\ejiro\Downloads\fcc-forum-pageviews.csv"
df = pd.read_csv(df)


# In[29]:


df.head()


# In[30]:


# Convert 'date' column to datetime and set it as inde
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


# In[31]:


# Calculate lower and upper bounds for filtering
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)


# In[34]:


# filter the dataframe
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


# In[36]:


print(df)


# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title 
# should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the 
# y axis should be Page Views.

# In[49]:


# Plotting the data
plt.plot(df.index, df['value'], marker='o', linewidth=1, label='Page Views')
sns.set_style('darkgrid')
# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

# Display the plot
plt.show()


# Create a draw_bar_plot function that draws a bar chart, It should show average daily page 
# views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label 
# on the x axis should be Years and the label on the y axis should be Average Page Views.

# In[76]:


# Grouping by Month and Year
bar_df = df.groupby([df.index.year, df.index.month])['value'].mean().unstack()

# Plotting
sns.set_style('darkgrid')
bar_df.plot(kind='bar', figsize=(12, 6))
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.title('Average Daily Page Views by Month and Year')
plt.xticks(rotation=45)
plt.show()


# Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots that shows how the values are distributed 
# within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend)
# and the title of the second chart should be Month-wise Box Plot (Seasonality). 
# Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. 
# The boilerplate includes commands to prepare the data.

# In[88]:


def draw_box_plot():
    # Preparing the data
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.set_style('darkgrid')

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette='pastel', linewidth=2.5)
    axes[0].set_title('Year-wise Box Plot (Trend)', fontsize=16)
    axes[0].set_xlabel('Year', fontsize=14)
    axes[0].set_ylabel('Page Views', fontsize=14)
    axes[0].tick_params(axis='both', labelsize=12)

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                palette='Set2', linewidth=2.5)
    axes[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=16)
    axes[1].set_xlabel('Month', fontsize=14)
    axes[1].set_ylabel('Page Views', fontsize=14)
    axes[1].tick_params(axis='both', labelsize=12)

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

# Call the function
draw_box_plot()


# In[ ]:




