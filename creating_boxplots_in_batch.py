import glob
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
##Setting the current directory
os.chdir('/mnt/e/shantanu_new_tanta/tissue/facet_data')
##saving all files (with paths) in the directory as list 
file_list = glob.glob('/mnt/e/shantanu_new_tanta/tissue/facet_data/*csv')
#count=Counter(file_list)
#print(file_list)
#selecting columns to work with. Though it wasn't required but i like it for clarity
cols = [0, 1, 2]
#creating a dataframe
df = pd.DataFrame()
#i = 1
#looping set of commands for all files
for f in file_list:
    var = os.path.basename(f) #saving the file name to create dataframe with that filename
    title = os.path.splitext(var)[0]
    var=pd.read_csv(f, delimiter='\t', header=None, usecols=cols) #reading files
    #df = df.append(df_temp)
    columns = ['Tissuetype', 'E', 'P'] ##assigning columns headers
    var.columns = columns #adding it to dataframe var
    data=pd.melt(var, id_vars=["Tissuetype"], var_name="Region", value_name="G4-Density") ##recasting the data to plot in boxplot format
    fig = plt.figure()
    #++i
    #fig, axes = sns.plt.subplots(2,2)
    #print(i)
    #ax = fig.add_subplot(2, 3, i)
    #plt.subplot(2, 3, i)
    sns.FacetGrid(data, height=4)
    ax = sns.boxplot(x="G4-Density", y="Tissuetype", data=data, hue="Region", width=0.8)
    handles, labels = ax.get_legend_handles_labels()
    l = plt.legend(handles[0:2], labels[0:2], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title(title)
    #axes[0,0].legend(handles[:0], labels[:0])
    plt.savefig("/mnt/e/shantanu_new_tanta/tissue/facet_data/%s.png" % title, bbox_inches='tight')
    plt.show()
