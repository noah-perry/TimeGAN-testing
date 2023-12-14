# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:02:21 2023

@author: noahj
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


tc_pwr = pd.read_csv("Documents/GitHub/TimeGAN-testing/Tetuan City power consumption.csv", 
                     header = 0, 
                     names = ["datetime", "temp", "humidity", "wind_speed", "gen_diff_flows", "diff_flows", "z1_pwr", "z2_pwr", "z3_pwr"], 
                     parse_dates = [0])


# Aggregate to daily
tc_pwr["date"] = pd.to_datetime(tc_pwr["datetime"]).dt.date

tc_pwr_day = tc_pwr.groupby(['date']).agg(
    temp = ('temp', 'mean'),
    humidity = ('humidity', 'mean'),
    wind_speed = ('wind_speed', 'mean'),
    gen_diff_flows = ('gen_diff_flows', 'sum'),
    diff_flows = ('diff_flows', 'sum'),
    z1_pwr = ('z1_pwr', 'sum'),
    z2_pwr = ('z2_pwr', 'sum'),
    z3_pwr = ('z3_pwr', 'sum')
)

tc_pwr_day = tc_pwr_day.reset_index(drop = False)
tc_pwr_day.to_csv("tc_pwr_day.csv", index = False)


# Add day of week
tc_pwr_day["dayofweek"] = pd.to_datetime(tc_pwr_day["date"]).dt.dayofweek


### Read in synthetic data
tc_pwr_day_synth = pd.read_csv("TC Day Synth.csv", 
                     header = 0, 
                     names = ["temp", "humidity", "wind_speed", "gen_diff_flows", "diff_flows", "z1_pwr", "z2_pwr", "z3_pwr"])



# Temperature Comparison
plt.plot(tc_pwr_day["date"], tc_pwr_day["temp"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["temp"], label = "Synthetic")
plt.title("Temperature (in degrees Celsius)")
plt.xlabel("Date")
plt.legend()

# Humidity Comparison
plt.plot(tc_pwr_day["date"], tc_pwr_day["humidity"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["humidity"], label = "Synthetic")
plt.title("Humidity")
plt.xlabel("Date")
plt.legend(loc = "upper right")
plt.ylim(25, 105)

# Wind Speed Comparison
plt.plot(tc_pwr_day["date"], tc_pwr_day["wind_speed"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["wind_speed"], label = "Synthetic")
plt.title("Wind Speed")
plt.xlabel("Date")
plt.legend(loc = "upper right")
plt.ylim(0, 6.2)

# General Diffuse Flows Comparison
plt.plot(tc_pwr_day["date"], tc_pwr_day["gen_diff_flows"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["gen_diff_flows"], label = "Synthetic")
plt.title("General Diffuse Flows")
plt.xlabel("Date")
plt.legend()

# Diffuse Flows Comparison
plt.plot(tc_pwr_day["date"], tc_pwr_day["diff_flows"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["diff_flows"], label = "Synthetic")
plt.title("Diffuse Flows")
plt.xlabel("Date")
plt.legend()

# Zone 1 Power Consumption
plt.plot(tc_pwr_day["date"], tc_pwr_day["z1_pwr"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["z1_pwr"], label = "Synthetic")
plt.title("Zone 1 Power Consumption")
plt.xlabel("Date")
plt.legend()

# Zone 2 Power Consumption
plt.plot(tc_pwr_day["date"], tc_pwr_day["z2_pwr"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["z2_pwr"], label = "Synthetic")
plt.title("Zone 2 Power Consumption")
plt.xlabel("Date")
plt.legend()

# Zone 3 Power Consumption
plt.plot(tc_pwr_day["date"], tc_pwr_day["z3_pwr"], label = "Real")
plt.plot(tc_pwr_day["date"], tc_pwr_day_synth["z3_pwr"], label = "Synthetic")
plt.title("Zone 3 Power Consumption")
plt.xlabel("Date")
plt.legend()

# Exploring pattern in power consumption plots
plt.plot(tc_pwr_day["date"], tc_pwr_day["z1_pwr"], label = "Zone 1")
plt.plot(tc_pwr_day["date"], tc_pwr_day["z2_pwr"], label = "Zone 2")
plt.plot(tc_pwr_day["date"], tc_pwr_day["z3_pwr"], label = "Zone 3")
plt.title("Daily Power Consumption")
plt.xlabel("Date")
plt.ylim(0,6000000)
plt.legend(loc = "lower left")

# Day of the week pattern exists in zone 1 and zone 2 power consumption
plt.scatter(tc_pwr_day["dayofweek"][0:90], tc_pwr_day["z1_pwr"][0:90], s = 20, alpha = 0.5, label = "Zone 1")
plt.scatter(tc_pwr_day["dayofweek"][0:90], tc_pwr_day["z2_pwr"][0:90], s = 20, label = "Zone 2", color = "orange", )
plt.title("Power Consumption by Day of the Week\n(First 90 Days of 2017)")
plt.xlabel("Day of Week")
plt.legend()

# Day of the week pattern does not appear to be present in zone 3 power consumption
plt.scatter(tc_pwr_day["dayofweek"][0:90], tc_pwr_day["z3_pwr"][0:90], color = "green")
plt.ylim(0,6000000)


# Autocorrelation Comparisons
pd.plotting.autocorrelation_plot(tc_pwr_day["z1_pwr"], label = "Real")
pd.plotting.autocorrelation_plot(tc_pwr_day_synth["z1_pwr"], label = "Synthetic")
plt.title("Autocorrelation: Zone 1 Power Consumption")

pd.plotting.autocorrelation_plot(tc_pwr_day["z2_pwr"], label = "Real")
pd.plotting.autocorrelation_plot(tc_pwr_day_synth["z2_pwr"], label = "Synthetic")
plt.title("Autocorrelation: Zone 2 Power Consumption")

pd.plotting.autocorrelation_plot(tc_pwr_day["z3_pwr"], label = "Real")
pd.plotting.autocorrelation_plot(tc_pwr_day_synth["z3_pwr"], label = "Synthetic")
plt.title("Autocorrelation: Zone 3 Power Consumption")

