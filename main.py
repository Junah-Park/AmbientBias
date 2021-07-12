import pandas as pd
import glob

path = r'\\emcore.us\dfs\CACON\ATE_Data\SDG500-00100-100' 

# # Any file dated 20200101 onward
# file_names = glob.glob(path + "/*-100_ZROTC_SDG500_202*.csv")
# short_names = glob.glob(path + "/*-100_ZROTC_SDG500_Short_202*.csv")

# list of dataframes, each dataframe is a unit
units = []

# for file_name in file_names:
#     df = pd.read_csv(file_name, header=12)#, float_precision='high')
#     units.append(df)

# for file_name in short_names:
#     df = pd.read_csv(file_name, header=12), float_precision='high')
#     units.append(df)

file_name = glob.glob(path + "/J7878-100_ZROTC_SDG500_20210601_200721.csv")
df = pd.read_csv(file_name[0], header=12, usecols=['Time','RateV_Y','TempV_Y'],
 float_precision='high')

# with pd.option_context('display.precision',10):
#     print(df.head())

Tmax = 85
Tmin = -40

# Time starts from 0
df['Time'] = df['Time'] - df['Time'][0]

# Temps in V, max and min temps
tempsV = df['TempV_Y']
max_tempV = tempsV.max()
min_tempV = tempsV.min()

tmpsf = (Tmax - Tmin) / (max_tempV - min_tempV)
tmpbias = Tmax - (tmpsf * max_tempV)

tempsC = tmpbias + tmpsf * tempsV

df['TempC'] = tempsC

df[df.loc((df['TempC']>=22.5) & (df['TempC']<=25))]

print(df.head())


# # Slope of line of best fit
# temp_slope = (max_tempV-min_tempV)/(40+85)

# # Ambient bias:   0 ± 12 mV at +25°C
# # Oven at 25°C at ~50 rows into the test (500 seconds)
# amb_bias = df['RateV_Y'][50]

# Temps = tempsV/temp_slope + (85 - (max_tempV/temp_slope))

# print(Temps.head())
# print(amb_bias)

# Assumption: mx+b => temp_slope * tempsV + amb_bias

# Min Deviation



