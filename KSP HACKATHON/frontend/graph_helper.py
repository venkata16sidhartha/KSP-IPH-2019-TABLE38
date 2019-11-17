import pandas as pd
from collections import Counter
import dict_digger
import numpy as np
import matplotlib.pyplot as plt

def plotter(file, col, name):
    data = pd.read_csv(file, index_col = None)
    der_data=data[col].values
    a=dict(Counter(der_data))
    value=[]
    for i in range(len( data)):
        value.append(dict_digger.dig(a,der_data[i]))
    labels = list(a.keys())
    plt.subplot(2,1,1)
    plt.xlabel("times")
    plt.ylabel(col)
    plt.title("bar graph")
    plt.bar(np.arange(0,len(data),1),value)
    plt.subplot(2,1,2)
    plt.title("pie chart")
    plt.pie(value[:len(labels)], labels=labels, shadow=True, startangle=90)
    img = "static/img/"
    # plt.show()
    plt.savefig(img + name + ".png")
    # print(img+name+".png")
    return (img+name+".png")

if __name__ == "__main__":
    plotter("mem_details.csv", "beat_number", "beat4")
