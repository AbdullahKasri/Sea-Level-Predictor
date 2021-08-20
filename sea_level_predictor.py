import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import seaborn as sns

df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Read data from file
    plot = plt.plot(df)
    plt.savefig("plot.png")
    return plot

def draw_sctter_plot():

    # Create scatter plot
    scatterplot = plt.scatter(df)
    plt.savefig("scatterplot.png")
    return scatterplot

def first_line():
    # Create first line of best fit
    firstline = sns.lineplot(0)
    plt.savefig("firstline.png")
    return firstline

def second_line():
    # Create second line of best fit
    secondline = sns.lineplot(1)
    plt.savefig("firstline.png")
    return secondline


def get_xlabel():
    plt.xlabel = 'test_plot_xlabel'

def get_ylabel():
    plt.ylabel = 'test_plot_ylabel'

def get_xticks():
    plt.xticks = 'test_plot_xticks'

def add_labels_titles():
    # Add labels and title
    height = 'test_plot_xlabel'
    bars = 'test_plot_ylabel'
    x_pos = np.arange(len(bars))
    plt.title("sea level")
    plt.xlabel("year")
    plt.ylabel("sea level")
    plt.xticks(x_pos, height)
    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()