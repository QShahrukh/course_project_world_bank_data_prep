#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd


# In[34]:


women_data = pd.read_csv('API_SE.PRM.CMPT.FE.ZS_DS2_en_csv_v2_5359531.csv', skiprows=3)


# In[35]:


women_data.head(3)


# In[36]:


women_data = women_data.drop(['Indicator Name', 'Indicator Code', 'Unnamed: 66'], axis=1)


# In[37]:


women_data = women_data.melt(id_vars=['Country Name', 'Country Code'])
women_data.columns = ['Country Name', 'Country Code', 'year', 'percentage']


# In[38]:


women_data


# In[39]:


len(women_data)


# In[40]:


women_data_metadata = pd.read_csv('Metadata_Country_API_SE.PRM.CMPT.FE.ZS_DS2_en_csv_v2_5359531.csv')


# In[41]:


women_data_metadata


# In[42]:


women_data = women_data.merge(women_data_metadata, on=['Country Code'], how='left')


# In[43]:


women_data


# In[29]:


# Drop rows where percentage is missing for country.  


# In[46]:


women_data = women_data.dropna(subset=['percentage'])


# In[49]:


women_data['IncomeGroup'] = women_data['IncomeGroup'].fillna('OTHER')


# In[51]:


women_data['Region'] = women_data['Region'].fillna('OTHER')


# In[72]:


# Save women Primary completion rate date. 
women_data.to_csv('women_clean_data.csv')


# In[54]:


# Preparing child mortality data.


# In[56]:


child_data = pd.read_csv('API_SH.DYN.MORT_DS2_en_csv_v2_5358988.csv', skiprows=3)


# In[59]:


child_data = child_data.drop(['Indicator Name', 'Indicator Code', 'Unnamed: 66'], axis=1)


# In[61]:


child_data = child_data.melt(id_vars=['Country Name', 'Country Code'])
child_data.columns = ['Country Name', 'Country Code', 'year', 'percentage']
child_data


# In[63]:


child_data_metadata = pd.read_csv('Metadata_Country_API_SH.DYN.MORT_DS2_en_csv_v2_5358988.csv')


# In[64]:


child_data_metadata


# In[65]:


child_data = child_data.merge(child_data_metadata, on=['Country Code'], how='left')


# In[66]:


child_data


# In[67]:


child_data = child_data.dropna(subset=['percentage'])


# In[68]:


child_data


# In[69]:


child_data['IncomeGroup'] = child_data['IncomeGroup'].fillna('OTHER')
child_data['Region'] = child_data['Region'].fillna('OTHER')


# In[70]:


child_data


# In[71]:


child_data.to_csv('child_clean_data.csv')


# In[ ]:




