import os 
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering


#File structure etc
datafolder = os.path.join("..", "00_data")
datafile = "161209_Schenker_Sensordaten.csv"

#Import
df_initial = pd.read_csv(os.path.join(datafolder, datafile))


#Drop all non-numeric columns, so that clustering can work
# 'df_numeric = df_initial.drop(['SXXJ Nummer', 'Container'])
'df_numeric['DatetimeUnix'] = df_numeric.apply




#Create clustering
model_clust = AgglomerativeClustering(distance_threshold=0, n_clusters = None)
model_clust = model_clust.fit(df_initial)