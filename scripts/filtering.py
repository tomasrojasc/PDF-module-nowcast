import pickle
import pandas as pd
from modules.config import year, bin_w

# opening data
with open('./data/dicts_of_utdf.pickle', 'rb') as f:
    UTdf_dict = pickle.load(f)
f.close()

with open('data/final_df.correlations', 'rb') as f:
    correlations = pickle.load(f)
f.close()

correlations['date_key'] = pd.to_datetime(correlations['date_key'])


filter1 = correlations['date_key'].dt.year == year
filter2 = correlations['bin_width'] == bin_w
cols2take = ['lag_in_minutes', 'cross_corr', 'cross_corr_err', 'date_key']
filtered_correlations = correlations[filter1 & filter2][cols2take]

# taking out lags out of +-2hrs

filterlag1 = filtered_correlations['lag_in_minutes'] >= -120
filterlag2 = filtered_correlations['lag_in_minutes'] <= 120

filtered_correlations = filtered_correlations[filterlag1 & filterlag2]


# keeping time series of 2009

date_keys = [i for i in UTdf_dict if i[:4] == str(year)]

filtered_dict_UTdf = {}
for date_key in date_keys:
    filtered_dict_UTdf[date_key] = UTdf_dict[date_key]




# saving data

with open('filtered_data/filtered_correlations.df', 'wb') as f:
    pickle.dump(filtered_correlations, f)
f.close()

with open('filtered_data/filtered_timeseries.dict', 'wb') as f:
    pickle.dump(filtered_dict_UTdf, f)
f.close()




