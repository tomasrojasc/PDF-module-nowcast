import pickle

# opening data
with open('filtered_data/filtered_correlations.df', 'rb') as f:
    correlations = pickle.load(f)
f.close()

with open('filtered_data/filtered_timeseries.dict', 'rb') as f:
    time_series_dict = pickle.load(f)
f.close()

# creating a dictionary of dfs for the correlations

corr_dict = {}
correlations['date_key'] = correlations['date_key'].dt.strftime('%Y-%m-%d')
date_keys = correlations['date_key'].unique().tolist()

for date_key in date_keys:
    corr_dict[date_key] = correlations[correlations['date_key'] == date_key]


with open('dict_data/corr.dict', 'wb') as f:
    pickle.dump(corr_dict, f)
f.close()

with open('dict_data/time_series.dict', 'wb') as f:
    pickle.dump(time_series_dict, f)
f.close()

