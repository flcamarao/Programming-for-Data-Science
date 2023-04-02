
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def largest_invoice():
    df = pd.read_csv(filepath, dtype={'InvoiceNo': 'str'})
    df = df.InvoiceNo.value_counts().head(10)
    df.index.name = 'InvoiceNo'
    return df

def most_daily_tagged_artists():
    df = pd.read_csv(filepath, sep='\t', engine='python')
    df['date'] = pd.to_datetime(df[['year','month','day']])
    df = df.groupby(['date','userID']).artistID.nunique().nlargest(10)
    return df.reset_index().userID.to_list()

def bin_names():
    df = pd.read_csv(filepath)
    df['bin'] = pd.cut(df.product_name_lenght, 10)
    return df.groupby('bin').product_description_lenght.median()

def charge_per_state():
    df = (pd.read_csv(filepath, 
                      sep='\t', 
                      engine='python',  
                      nrows=1000000, 
                      usecols = ['NPPES_PROVIDER_STATE', 'AVERAGE_SUBMITTED_CHRG_AMT'])
          .groupby('NPPES_PROVIDER_STATE').AVERAGE_SUBMITTED_CHRG_AMT.mean()
         )
    fig, ax = plt.subplots(figsize=(12,8))
    plt.xticks(rotation=90)
    df.plot(kind='bar', ax=ax, ylabel='Average submitted charge amount ($)')
    ax.yaxis.set_ticks(np.arange(0,900,100))
    ax.yaxis.set_ticklabels(['0', '100', '200', '300','400','500','600','700','800'])
    return ax

def voters_profile():
    df = pd.read_csv(filepath).select_dtypes(include=['int64']).sort_index(axis=1)
    fig, ax = plt.subplots(5, 4, figsize=(10, 12), dpi=300)
    df.hist(ax=ax, bins=10)
    plt.subplots_adjust(hspace=0.5, wspace=.4)
    plt.show()
    return fig

def standardize_ratings():
    df = pd.read_csv(filepath, nrows=1000000)
    df.rating = (df.rating - df.rating.mean())/df.rating.std()
    return df

def user_songcount():
    df = pd.read_table(filepath, names=["userID", "songID", "count"], nrows=1000000)
    df.userID = df.userID.str[:5]
    return df.groupby('userID').songID.nunique()

def at_least_10():
    df = pd.read_csv(filepath, nrows=1000)
    return df[df.groupby('user_id').track_id.transform('nunique') >= 10]

def source_dest():
    df = pd.read_csv(filepath,
                     nrows=1000,
                     delimiter='\t', 
                     header=None, 
                    compression='gzip')
    return df.groupby(0)[1].apply(list)

def mean_std_votes():
    df = pd.read_csv(filepath)
    return df.groupby('province_or_city').agg({'votes_obtained':['mean', 'std']})


