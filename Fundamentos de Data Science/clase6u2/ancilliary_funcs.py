import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

def perdidas(dataframe, var, print_list = False):
    
    cantidad_perdidos = dataframe[var].isnull().value_counts().get(True)
    porcentaje_perdidos = dataframe[var].isnull().value_counts('%').get(True) 
    df_trabajo = dataframe[var]
    if cantidad_perdidos == None:
        cantidad_perdidos =0
    if porcentaje_perdidos == None:
        cantidad_perdidos =0
    
    print('la cantidad de casos perdidos es de :',cantidad_perdidos)
    print('su porcentaje es de: ',porcentaje_perdidos)
    
    df_temporal= dataframe[df_trabajo.isnull()]['cname']
    
    if print_list is True:
        print(df_temporal) 
     
    
def grafico_histograma (dataframe, var, sample_min =False, true_min= False):
    plt.hist(dataframe[var].dropna())
    
    if sample_min == True:
        plt.axvline(dataframe[var].mean(), lw=3, color= 'tomato', linestyle='--')
    if true_min== True:
        plt.axvline(df[var].mean(), lw=3, color= 'dodgerblue', linestyle='--')
        
def dotplot(dataframe, plot_var, plot_by, global_stat=False, statistic= 'mean'):
    data_frame_mean= round(dataframe.groupby(plot_by)[plot_var].mean(),2)
    data_frame_median= round(dataframe.groupby(plot_by)[plot_var].median(),2)
    data_frame_media_global= dataframe[plot_var].mean()
    
    if global_stat==True:
        plt.axvline(dataframe[plot_var].mean(), lw=3, color= 'tomato', linestyle='--')
        
    if statistic == 'mean':
        plt.plot(data_frame_mean.values, data_frame_mean.index, 'o', color = 'red')
    elif statistic =='median':
        plt.plot(data_frame_median.values, data_frame_median.index, 'o', color = 'red')

def clasifica_variables(x):   
    for i,v in x.iteritems():
        if v.dtype== 'int64':
            print(v.describe().round(2))
        elif v.dtype== 'float64':
            print(v.describe().round(2))
        elif v.dtype== 'object':
            print(v.value_counts())
            
def missing_value(df1, caracter):
    nombres = df1.columns
    for nombre in nombres:
        df1[nombre] = librerias.np.where(df1[nombre]=='?',librerias.np.nan, df1[nombre])
        return df1
    
def missing_value_caracter(df1, caracter):
    nombres = df1.columns
    for nombre in nombres:
        df1[nombre] = librerias.np.where(df1[nombre]==caracter,librerias.np.nan, df1[nombre])
        return df1