from flask import Flask,render_template, request
import pickle
# from sklearn.preprocessing import StandardScaler
# import numpy as np
# import pandas as pd
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
import pandas as pd


app = Flask(__name__)



with open('file.pkl', 'rb') as reliance:
    reliance_forecast = pickle.load(reliance)

with open('TechM.pkl', 'rb') as techm: 
    techm_forecast = pickle.load(techm)
    print(techm_forecast)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/techm')
def predict_techm():
    overall_plot=get_techm_overall()
    overall_plot.savefig(os.path.join('static', 'images', 'techm_overall_plot.png'))
    overall_plot.close()

    monthly_plot=get_techm_month()
    monthly_plot.savefig(os.path.join('static', 'images', 'techm_monthly_plot.png'))
    monthly_plot.close()
  
    return render_template('techm.html')


def get_techm_overall():
  
    plt1=techm_forecast[['Forecast_ARIMA']].plot(figsize=(10,5))
    plt1.get_figure() #converting pandas plot to matplotlib plot. therefore this plot becomes matplotlib plot and therefore stored in plt by default.
    return plt #returning plt becoz matplotlib plot is stored in plt by default.

def get_techm_month():
    # reliance_forecast.iloc[-30:].plot()   # Last 1 month price prediction
    plt1=techm_forecast[['Forecast_ARIMA']].iloc[-30:].plot(figsize = (10,5)) 
    plt1.get_figure()
    return plt

@app.route('/reliance')
def predict_reliance():
    
    overall_plot=get_reliance_overall()
    overall_plot.savefig(os.path.join('static', 'images', 'reliance_overall.png'))
    overall_plot.close()

    monthly_plot=get_reliance_month()
    monthly_plot.savefig(os.path.join('static', 'images', 'reliance_monthly.png'))
    monthly_plot.close()
  
    return render_template('reliance.html')

def get_reliance_overall():
    plt1=reliance_forecast[['Forecast_ARIMA']].plot(figsize=(10,5))
    plt1.get_figure()
    return plt 


def get_reliance_month():
  # Last 1 month price prediction
    plt1=reliance_forecast[['Forecast_ARIMA']].iloc[-30:].plot(figsize=(10,5)) 
    plt1.get_figure()
    return plt

if __name__ == '__main__':
    app.run(debug = True)

