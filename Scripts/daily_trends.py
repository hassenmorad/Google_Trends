# Daily Google Search Trends (source: https://github.com/qztseng/google-trends-daily/blob/master/google%20Trend%20daily%20data%20for%20Brexit.ipynb)
from pytrends.request import TrendReq
import gtrends
import pandas as pd
import numpy as np
from datetime import date
import os

# Keywords to extract trends data for
kw_dict = {
    'Amazon': ['amazon', 'amazon stock', 'amzn', 'amzn stock', 'amzn earnings'],
    'Apple': ['apple', 'apple stock', 'aapl', 'aapl stock', 'aapl earnings'],
    'Fitbit': ['fitbit', 'fitbit stock', 'fit stock', 'fit earnings'],
    'Google': ['google', 'google stock', 'googl', 'googl stock', 'googl earnings', 'alphabet stock', 'alphabet earnings'],
    'Netflix': ['netflix', 'netflix stock', 'nflx', 'nflx stock', 'nflx earnings'],
    'Peloton': ['peloton', 'peloton stock', 'pton', 'pton stock', 'pton earnings'],
    'Tesla': ['tesla', 'tesla stock', 'tsla', 'tsla stock', 'tsla earnings'],
    'Bitcoin': ['bitcoin', 'bitcoin', 'bitcoin price', 'btc', 'btc price'],
    'Gold': ['gold', 'gold price'],
}

# 
pytrend = TrendReq(hl='en-US', tz=480)
start = '2019-01-01'
end = str(date.today())
geo=''
cat=0
gprop=''

os.mkdir('stock_trends')
os.chdir('stock_trends')
for key in kw_dict:
    print(key)
    kw_list = kw_dict[key]
    key_df = pd.DataFrame()
    for keyword in kw_list:
        df = gtrends.get_daily_trend(pytrend, keyword, start, end, geo=geo, cat=cat, gprop=gprop, verbose=False)
        df['Search Term'] = np.full(len(df), keyword)
        df = df[[keyword, 'Search Term']].reset_index()
        df = df.rename({keyword:'Trend Score', 'index':'Date'}, axis=1)
        key_df = pd.concat([key_df, df])
        #data = pytrend.get_historical_interest(kw_list, year_start=2020, month_start=1, day_start=1, hour_start=0, year_end=2020, month_end=1, day_end=9, hour_end=23, cat=0, geo='', gprop='', sleep=15)
    key_df.to_csv(key.lower() + '_search_trends_' + start[2:4] + '_' + end[2:4] + '.csv', index=False)