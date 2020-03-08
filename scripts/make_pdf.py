from modules.utils import *
import pickle
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np


with open('dict_data/corr.dict', 'rb') as f:
    corr_dict = pickle.load(f)
f.close()

with open('dict_data/time_series.dict', 'rb') as f:
    time_series_dict = pickle.load(f)
f.close()



dates = [i for i in corr_dict]
dates.sort()
figsize = (20, 10)

plots_corr = []
plots_time = []

# filling lists

for key in dates:
    if len(corr_dict[key].dropna()) > 2:
        plots_corr.append(make_corr_plot(corr_dict[key], fig_size=figsize))
        plots_time.append(make_timeseries_plot(time_series_dict[key], fig_size=figsize))



pdf = PdfPages("output.pdf")

print('making pdf')
for i in range(len(plots_time)):
    pdf.savefig(plots_time[i])
    pdf.savefig(plots_corr[i])
pdf.close()

plt.close('all')
