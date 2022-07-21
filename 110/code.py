import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df=pd.read_csv('medium_data.csv') 
data=df['reading_time'].to_list()

population_mean=statistics.mean(data)
print('The population mean is ',population_mean) 

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(100):
        set_of_means=random_set_of_means(30)
        mean_list.append(set_of_means)
    sample_mean=statistics.mean(mean_list)    
    print('The sample mean is ',sample_mean)
    show_fig(mean_list)

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],['temprature'],show_hist=False)
    fig.show() 

setup()

