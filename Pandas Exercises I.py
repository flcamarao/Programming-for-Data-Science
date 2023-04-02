def init_series():                                                                             
    s1 = pd.Series(range(1,101,11), index= list('abcdefghij'), name='foo', dtype=float )           
    s2 = pd.Series(range(0,10),  index= list('fghijklmno'), dtype=int)
    s3 = pd.Series(5, index= list('xyz'), dtype=int)                                                                              
    return s1, s2, s3

def init_df(s1, s2):
    df1 = pd.DataFrame(s1)
    df2 = pd.DataFrame({ 'series2': s2, 'series1': s1 })
    return df1, df2

def top_plus_bottom():
    df = pd.read_csv(filepath, usecols = ['Quantity', 'UnitPrice'])
    return df.head(5).to_numpy() + df.tail(5).to_numpy()

def count_alone():
    df = pd.read_csv(filepath)
    df['alone'] = df['single'] + df['widow'] + df['legally_seperated']
    df.sort_values(by='alone', ascending=False)
    return df

def scores_stats():
    df = pd.read_csv(filepath)
    df = df['relevance'].describe()
    return df

def top_cat():
    df = pd.read_csv(filepath, encoding='latin1', skipinitialspace=True)
    categories = df['Category'].value_counts().head(10)
    return categories

def listing_info():
    df = pd.read_csv(filepath, usecols=['id','name', 'summary' , 'space' , 'description'], index_col='id')
    df = df.sort_index()
    df = df.query('id >= 11076 and id <= 15400')
    return df

def aisle_dep():
    df = pd.read_csv(filepath, index_col='product_id')
    df.loc[df['aisle_id'] == 5, 'product_name'] = (df['product_name'] + " (" + 
    df['aisle_id'].astype(str) + "-" + df['department_id'].astype(str)) + ")"
    return df

def camsur_reps():
    df = pd.read_csv(filepath)
    df = df[(df['province_or_city'] == 'Camarines Sur')]
    df['surname'] = df['name'].str.split(',', expand=True)[0]
    df = df[['surname', 'votes_obtained']]
    return df

def no_pop():
    df = pd.read_csv(filepath, sep='<SEP>', engine ='python', header=None )
    df.columns = ['year', 'track_id', 'artist', 'title']
    options = ['Britney Spears' ,'Backstreet Boys'] 
    df = df[(df['year'] < 2000) & (~df['artist'].isin(options))]
    return df 

def read_trips():
    df = pd.read_csv(filepath, nrows=100)
    df['rate_code'] = df['rate_code'].astype(str)
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])
    return df
    
def write_trips(df_trips):
    df_trips[["pickup_longitude", "pickup_latitude", "dropoff_longitude", "dropoff_latitude"]].to_csv("trip_coords.csv")

