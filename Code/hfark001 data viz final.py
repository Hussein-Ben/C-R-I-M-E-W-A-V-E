#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

plt.tight_layout()

# import the data
source_url_crime_rate = "https://data.london.gov.uk/download/recorded_crime_summary/d2e9ccfc-a054-41e3-89fb-53c2bc3ed87a/MPS%20Borough%20Level%20Crime%20(most%20recent%2024%20months).csv"

crime_source = requests.get(source_url_crime_rate).content
crime_rate = pd.read_csv(io.StringIO(crime_source.decode('utf-8')))

#print(crime_rate.columns)

# for every borough
murder_rate = crime_rate.loc[crime_rate['Minor Category'] == 'Murder']

# murder rate for the entire london covered by the Metropolitan Police Force in the last 24 months
murder_rate = murder_rate.groupby(['Minor Category']).agg('sum')

# plot murder rate
murder_rate_graph = murder_rate.iloc[0].plot.line(grid=True)
murder_rate_graph.set_xlabel("Time period over the last 24 months")
murder_rate_graph.set_ylabel("Murder count")

months = murder_rate.columns

murder_rate_graph.set_xticks(range(24)) # each tick for each month
murder_rate_graph.set_xticklabels(months[:], rotation=90)
#murder_rate_graph


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

plt.tight_layout()

source_url_police_pop = "https://data.london.gov.uk/download/police-force-strength/e442f07c-bc39-4c61-a62b-0e5957ea474f/Police%20Force%20Strength.csv"

police_pop_source = requests.get(source_url_police_pop).content
police_pop = pd.read_csv(io.StringIO(police_pop_source.decode('utf-8')))

# total police force population combine all three columns togther to create total police population
police_pop['Total Police Strength'] = police_pop['Police Officer Strength'] + police_pop['Police Staff Strength'] + police_pop['PCSO Strength']
police_pop = police_pop.drop(columns=['Police Officer Strength', 'Police Staff Strength','PCSO Strength'])


#police_pop_graph
pre_201611 = range(41)
police_pop = police_pop.drop(pre_201611)
fig, ax = plt.subplots()
police_pop_graph = ax.plot(police_pop['Date'], police_pop['Total Police Strength'])
fig.autofmt_xdate()
ax.grid(True)
plt.xticks(rotation=90, fontsize = 15)
plt.tick_params(axis='x', which='major', labelsize=9)
plt.xlabel('Time period over the last 21 months')
plt.ylabel('Total Police Strength')
plt.tight_layout()

#police_pop


# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

plt.tight_layout()

# import the data
source_url_crime_rate = "https://data.london.gov.uk/download/recorded_crime_summary/d2e9ccfc-a054-41e3-89fb-53c2bc3ed87a/MPS%20Borough%20Level%20Crime%20(most%20recent%2024%20months).csv"

crime_source = requests.get(source_url_crime_rate).content
crime_rate = pd.read_csv(io.StringIO(crime_source.decode('utf-8')))

#print(crime_rate.columns)

# for every borough
GBH_rate = crime_rate.loc[crime_rate['Minor Category'] == 'Wounding/GBH']

# GBH rate for the entire london covered by the Metropolitan Police Force in the last 24 months
GBH_rate = GBH_rate.groupby(['Minor Category']).agg('sum')

# plot GBH rate
GBH_rate_graph = GBH_rate.iloc[0].plot.line(grid=True)
GBH_rate_graph.set_xlabel("Time period over the last 24 months")
GBH_rate_graph.set_ylabel("Wounding/GBH count")

months = GBH_rate.columns

GBH_rate_graph.set_xticks(range(24)) # each tick for each month
GBH_rate_graph.set_xticklabels(months[:], rotation=90)


# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

plt.tight_layout()

# import the data
source_url_crime_rate = "https://data.london.gov.uk/download/recorded_crime_summary/d2e9ccfc-a054-41e3-89fb-53c2bc3ed87a/MPS%20Borough%20Level%20Crime%20(most%20recent%2024%20months).csv"

crime_source = requests.get(source_url_crime_rate).content
crime_rate = pd.read_csv(io.StringIO(crime_source.decode('utf-8')))

#print(crime_rate.columns)

# for every borough
weapon_rate = crime_rate.loc[crime_rate['Minor Category'] == 'Offensive Weapon']

# offensive weapon rate for the entire london covered by the Metropolitan Police Force in the last 24 months
weapon_rate = weapon_rate.groupby(['Minor Category']).agg('sum')

# plot offensive weapon rate
weapon_rate_graph = weapon_rate.iloc[0].plot.line(grid=True)
weapon_rate_graph.set_xlabel("Time period over the last 24 months")
weapon_rate_graph.set_ylabel("Offensive Weapon count")

months = weapon_rate.columns

weapon_rate_graph.set_xticks(range(24)) # each tick for each month
weapon_rate_graph.set_xticklabels(months[:], rotation=90)


# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

plt.tight_layout()

# import the data
source_url_crime_rate = "https://data.london.gov.uk/download/recorded_crime_summary/d2e9ccfc-a054-41e3-89fb-53c2bc3ed87a/MPS%20Borough%20Level%20Crime%20(most%20recent%2024%20months).csv"

crime_source = requests.get(source_url_crime_rate).content
crime_rate = pd.read_csv(io.StringIO(crime_source.decode('utf-8')))

#print(crime_rate.columns)

# for every borough
pp_rate = crime_rate.loc[crime_rate['Minor Category'] == 'Personal Property']

# personal property rate for the entire london covered by the Metropolitan Police Force in the last 24 months
pp_rate = pp_rate.groupby(['Minor Category']).agg('sum')

# plot personal property rate
pp_rate_graph = pp_rate.iloc[0].plot.line(grid=True)
pp_rate_graph.set_xlabel("Time period over the last 24 months")
pp_rate_graph.set_ylabel("Personal Property theft count")

months = pp_rate.columns

pp_rate_graph.set_xticks(range(24)) # each tick for each month
pp_rate_graph.set_xticklabels(months[:], rotation=90)

#crime_rate


# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

plt.tight_layout()

# import the data
source_url_crime_rate = "https://data.london.gov.uk/download/recorded_crime_summary/d2e9ccfc-a054-41e3-89fb-53c2bc3ed87a/MPS%20Borough%20Level%20Crime%20(most%20recent%2024%20months).csv"

crime_source = requests.get(source_url_crime_rate).content
crime_rate = pd.read_csv(io.StringIO(crime_source.decode('utf-8')))

#print(crime_rate.columns)

# for every borough
bp_rate = crime_rate.loc[crime_rate['Minor Category'] == 'Business Property']

# business property rate for the entire london covered by the Metropolitan Police Force in the last 24 months
bp_rate = bp_rate.groupby(['Minor Category']).agg('sum')

# plot business property rate
bp_rate_graph = bp_rate.iloc[0].plot.line(grid=True)
bp_rate_graph.set_xlabel("Time period over the last 24 months")
bp_rate_graph.set_ylabel("Business Property theft count")

months = bp_rate.columns

bp_rate_graph.set_xticks(range(24)) # each tick for each month
bp_rate_graph.set_xticklabels(months[:], rotation=90)


# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

source_url_police_pop = "https://data.london.gov.uk/download/police-force-strength/e442f07c-bc39-4c61-a62b-0e5957ea474f/Police%20Force%20Strength.csv"

police_pop_source = requests.get(source_url_police_pop).content
police_pop = pd.read_csv(io.StringIO(police_pop_source.decode('utf-8')))

# Police composition Oct 2016

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Police Officer Strength', 'Police Staff Strength', 'PCSO Strength'

officer_start = police_pop.loc[police_pop['Date'] == 'Oct-16', 'Police Officer Strength']
staff_start = police_pop.loc[police_pop['Date'] == 'Oct-16', 'Police Staff Strength']
pcso_start = police_pop.loc[police_pop['Date'] == 'Oct-16', 'PCSO Strength']

sizes = [officer_start, staff_start, 1493] ## last value had to be manually entered due to overloading the stack
explode = (0.1, 0.1, 0.1) # space out the slices

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
#police_pop


# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

source_url_police_pop = "https://data.london.gov.uk/download/police-force-strength/e442f07c-bc39-4c61-a62b-0e5957ea474f/Police%20Force%20Strength.csv"

police_pop_source = requests.get(source_url_police_pop).content
police_pop = pd.read_csv(io.StringIO(police_pop_source.decode('utf-8')))

# Police composition Jun 2018

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Police Officer Strength', 'Police Staff Strength', 'PCSO Strength'

officer_end = police_pop.loc[police_pop['Date'] == 'Jun-18', 'Police Officer Strength']
staff_end = police_pop.loc[police_pop['Date'] == 'Jun-18', 'Police Staff Strength']
pcso_end = police_pop.loc[police_pop['Date'] == 'Jun-18', 'PCSO Strength']

sizes = [officer_end, staff_end, 1257] ## last value had to be manually entered due to overloading the stack
explode = (0.1, 0.1, 0.1) # space out the slices

fig1, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
#police_pop


# In[ ]:





# In[ ]:




