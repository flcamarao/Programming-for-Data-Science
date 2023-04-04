import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.testing.compare import compare_images

get_ipython().run_line_magic('matplotlib', 'inline')

def peel(df):
    if df.shape[0] != df.shape[1]:
        return None
    else:
        return df.iloc[1:-1, 1:-1]

def patch(df, upper_left, lst):
    sl = df.loc[upper_left[0]:, upper_left[1]:]
    sl.iloc[:len(lst), :len(lst[0])] = lst

def pop_stats(province, municipality=None, census_year=2015):
    years = {'Feb-60': '1960',
             'May-70': '1970',
             'May-75': '1975',
             'May-80': '1980',
             'May-90': '1990',
             'Sep-95': '1995',
             'May-00': '2000',
             'Aug-07': '2007',
             'May-10': '2010',
             'Aug-15': '2015'}
    if municipality is None:
        df = pd.read_csv('Municipality Data - PSA.csv')
        df.rename(columns=years, inplace=True)
        df['is_total'].astype('string')
        df['province'] = df['province'].apply(str.lower)
        df['municipality'] = df['municipality'].apply(str.lower)
        df.drop(df[(df['is_total'] == 1)].index, inplace=True)
        x = df.groupby(['province'])[str(census_year)].agg(['sum', 'mean', 'std'])
        y = x[(x.index == province)]
        if (y.empty):
            return None
        return y.squeeze()
    else:
        df = pd.read_csv('Municipality Data - PSA.csv')
        df.rename(columns=years, inplace=True)
        df = df.fillna(0)
        df['1960'].astype(float)
        df['province'] = df['province'].apply(str.lower)
        df['municipality'] = df['municipality'].apply(str.lower)
        df = df[(df['province'] == province) & (df['is_total'] == 1)]
        df = df.groupby(['province', 'municipality']).sum()
        df2 = df[str(census_year)]
        if (df2.empty):
            return None
        return df2

def plot_pop(municipalities):
    df = pd.read_csv('Municipality Data - PSA.csv')
    mun = [m.lower() for m in municipalities]
    df = df.drop(columns=['province', 'is_total']).melt(id_vars=['municipality'],
                                                        var_name='date',
                                                        value_name='pop')
    fig, ax = plt.subplots(1, 1, figsize=(8, 10))
    for i in mun:
        df[df['municipality'].str.lower() == i].plot.line(x='date', y='pop', ax=ax)
    ax.legend(municipalities)
    return ax

def find_max(province):
    df = pd.read_csv('Municipality Data - PSA.csv')
    if (province.lower() not in df.province.str.lower().tolist()):
        raise ValueError
    else:
        df = df[df['is_total'] != 1]
        df.drop(columns=['is_total'], inplace=True)
        nums = df.select_dtypes(include=np.number).columns.tolist()
        df[nums] = (df.select_dtypes(include=np.number)
                    .diff(axis=1)
                    .apply(abs))
        end = df[df.province.str.lower() == province.lower()].select_dtypes(include=np.number).max().idxmax()
        range_mapper = {}
        for i, x in enumerate(df.select_dtypes(include=np.number).columns.tolist()[1:]):
            range_mapper[x] = df.select_dtypes(include=np.number).columns.tolist()[i]
        municipality = df.loc[df[df.province.str.lower() == province.lower()][end].idxmax()]['municipality']
        return municipality, range_mapper[end], end

def most_populous():
    df = pd.read_csv('Municipality Data - PSA.csv')
    df = df[df['is_total'] != 1]
    result = df.groupby('province')['Aug-15'].mean().sort_values(ascending=False).head(10)
    return result

def hourly_hashtag():
    df = pd.read_csv(filepath,
                     nrows=1_000_000,
                     parse_dates=['created_at'])
    df['created_at'] = (df['created_at'].dt.tz_localize('UTC')
                        .dt.tz_convert(tz='Asia/Manila'))
    result = (df.groupby(['hashtag', pd.Grouper(key='created_at', freq='H')])
              .size().reset_index()
              .rename(columns={0: 'count'}))
    return result.sort_values(['hashtag', 'created_at'])

def aisle_counts():
    df1 = pd.read_csv(filepath,
                      nrows=1_000_000)
    df2 = pd.read_csv(filepath,
                      nrows=1_000_000)
    merged_data = df1.merge(df2, on=['product_id', 'product_id'])
    df3 = pd.read_csv(filepath,
                      nrows=1_000_000)
    df4 = pd.read_csv(filepath,
                      nrows=1_000_000)
    df5 = pd.read_csv(filepath,
                      nrows=1_000_000)
    merged_data2 = merged_data.merge(df3, on=['aisle_id', 'aisle_id'], how='left')
    merged_data3 = merged_data2.merge(df4, on=['order_id', 'order_id'], how='left')
    merged_data3 = merged_data3.groupby('aisle')['order_id'].count().sort_values(ascending=False)
    return merged_data3

def from_to():
    df = pd.read_csv(filepath,
                     nrows=1000,
                     compression='gzip',
                     sep='\t',
                     engine='python',
                     header=None)
    return df.pivot_table(values=[3], index=[0], columns=[1], fill_value=0).droplevel(0, axis=1)

get_ipython().system('jupyter nbconvert "Assignment 4.ipynb" --stdout --to python --PythonExporter.exclude_markdown=True | pycodestyle - --show-source --ignore=W391,W503,E402,E501')

