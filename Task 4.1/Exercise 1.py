
# coding: utf-8

# In[253]:


import pandas as pd


# In[254]:


PATH = 'C:/Users/En/Documents/Python/Py/'


# In[255]:


def years_path():
    years_list = []
    year = input('Пожалуйста, введите нужные года через запятую: ')
    year = year.split(', ')
    for y in year:
        way = PATH + 'yob' + y + '.txt'
        years_list.append(way)
    return years_list


# In[256]:


def years_file(years_list):
    years_file_list = []
    for y in years_list:
        year_data = pd.read_csv(y, names=['Name', 'Gender', 'Count'])
        years_file_list.append(year_data)
    return(years_file_list)


# In[257]:


def uni_years(years_list):
    if len(years_list) == 1:
        return years_list[0]
    else:
        for i in years_list[1:]:
            years_list[0] = pd.merge(years_list[0], i, on=['Name', 'Gender'])
            years_list[0]['Count'] = years_list[0]['Count_x'] + years_list[0]['Count_y']
            del years_list[0]['Count_x']
            del years_list[0]['Count_y']
            return years_list[0]


# In[258]:


def top_three(dt):
    dt = dt.sort_values(by=['Count'], ascending=False)
    ndt = dt.head(3)
    for n in ndt['Name']:
        print(n)


# In[259]:


def main():
    pt = years_path()
    fl = years_file(pt)
    ye = uni_years(fl)
    top_three(ye)
    
main()

