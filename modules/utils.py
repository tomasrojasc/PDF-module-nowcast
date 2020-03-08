import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set_context('talk')


def make_corr_plot(corr_df, fig_size):
    """
    this functions makes a plot for a given df
    :param corr_df: dataframe containing the corr data
    :param fig_size: tuple figsize
    :return: matplotlib figure
    """
    x = corr_df['lag_in_minutes']
    y = corr_df['cross_corr']
    err = corr_df['cross_corr_err']
    date = corr_df['date_key'].unique()[0]

    fig = plt.figure(figsize=fig_size)
    plt.errorbar(x, y, yerr=err)
    plt.title('corr for date '+ date)
    plt.xlabel('lag in minutes')
    plt.ylabel('cross_corr')
    plt.grid()

    return fig


def make_timeseries_plot(time_series_df, fig_size):
    """
    function for time series plot
    :param time_series_df: dataframe with the time series
    :param fig_size: tuple figsize
    :return: matplotlib figure
    """

    x = time_series_df.index
    file1 = time_series_df.file1
    file2 = time_series_df.file2
    date = time_series_df.index.date[0].strftime('%Y-%m-%d')

    df_interpolated = time_series_df.interpolate('slinear')
    file1_inter = df_interpolated.file1
    file2_inter = df_interpolated.file2

    fig = plt.figure(figsize=fig_size)
    plt.plot(x, file1_inter, color='blue')
    plt.plot(x, file1, '.', color='blue')
    plt.plot(x, file2_inter, color='red')

    plt.plot(x, file2, '.', color='red')
    plt.grid()
    plt.title('time series for date '+ date)
    plt.xlabel('UT time')
    plt.ylabel('seeing DIMM')

    return fig
