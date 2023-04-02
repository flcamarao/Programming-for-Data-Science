import numpy as np
import pandas as pd

def double_work(df):
    start = '2021-01-01 09:00'
    end = '2021-01-01 17:00'
    df.loc[start:end, 'a'] = df.loc[start:end, 'b']*2
    return df

def hourly_mem_usage():
    df = pd.read_csv('mem.csv')
    df['Time'] = pd.to_datetime(df.Time, utc=True).dt.tz_convert('Asia/Manila')
    ps = df.groupby(pd.Grouper(key='Time', freq='H', closed='left')).accesslab.mean()
    return ps

def daily_mem_usage():
    df = pd.read_csv('mem.csv')
    df['Time'] = pd.to_datetime(df['Time'])
    ps = df.groupby(pd.Grouper(key='Time',freq='D'))['accesslab'].mean()
    ps.index = ps.index.to_period()
    return ps

def longest_distances():
    df = pd.read_csv(filepath, nrows=1000000)
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime']).dt.hour
    return df.groupby(['pickup_datetime','passenger_count']).trip_distance.max()

def mean_ratings():
    df = pd.read_csv(filepath
                     , compression='gzip'
                     , usecols=['review_scores_rating'
                    ,'host_since'])
    df['host_since'] = pd.to_datetime(df['host_since'])
    grp = pd.Grouper(key='host_since', freq='M')
    return df.groupby(grp)['review_scores_rating'].mean()

def product_aisles():
    df =  (pd.read_csv(filepath)
           .merge(pd.read_csv(filepath)
                  , on='aisle_id'
                  , how='left')
           .set_index('product_id')
          )
    return df

def tracks_with_loc():
    df1 = pd.read_csv(filepath
                      , delimiter='<SEP>'
                      , header=None
                      , engine='python')
    df2 = (pd.read_csv(filepath
                       , delimiter='<SEP>'
                       , header=None, engine='python')
           .drop_duplicates(3, keep='first')
          )
    df1.columns = ['track_id', 'song_id', 'artist', 'title']
    df2.columns = ['artist_id', 'lat', 'lon', 'artist', 'location']
    df = df1.merge(df2, on='artist', how='left').sort_values('track_id', ascending=True)
    return df

def party_votes():
    df = pd.read_csv(filepath)
    return (df.groupby(['province_or_city','party_affiliation'])
            .votes_obtained
            .sum()
            .unstack()
            .fillna(0)
            .astype(np.int64))

def naia_traffic():
    df = (pd.read_csv(filepath)
          .dropna(how='all', axis=1)
          .query('airport == "NAIA"', engine='python')
         )
    df1 = pd.melt(df, id_vars='airline_operator'
                  , value_vars=df.columns[3:-1]
                  , value_name='passengers'
                  , var_name='month')
    df1.month = df1.month.str.capitalize()
    df1.passengers = pd.to_numeric(df1.passengers, errors='coerce').fillna(0).astype(np.int64)
    return df1.groupby(['airline_operator', 'month']).passengers.sum().reset_index()

def pudo():
    df = pd.read_csv(filepath,
                    nrows=1_000_000)
    df = pd.crosstab(df['PULocationID'], df['DOLocationID'])
    return df
