import pandas as pd
data = pd.read_csv(r"C:\Users\hp\Downloads\archive\weather.csv")
#print(data.info())
print(data)
print(data['WindSpeed3pm'].nunique())#print(data['WindSpeed3pm'].unique())

#to analyse how many times RainTommorow is true
print(data.RainTomorrow.value_counts())
print(data.groupby('RainTomorrow').get_group('Yes'))


#Now cheking that how many time the windspeed is a particular entity say 4km/h
print(data['WindSpeed3pm'].unique())
print(data.groupby('WindSpeed3pm').get_group(4))

# to anaylyse how many null values in the data
print(data.isnull().sum())

#to calculate mean pressure at 9 am
print(data.Pressure9am.mean())

#to calculate standard deviation of pressure at 9 am
print(data.Pressure9am.std())

#to calculate the variance of humidity at 9am
print(data.Humidity9am.var())

#to find the instance that how many times rain today is recorded
print(data[data.RainToday=='Yes'])

#to find the instance where temperature at 9 am is more than 20 degree and rain is predicted today
print(data[(data.Temp9am>20)&(data.RainToday=='Yes')])

#to calculate mean against every possiblity of Rain Tomorrow
print(data.groupby('RainTomorrow').mean())

#to calculate max against every possiblity of Rain Tomorrow
#print(data.groupby('RainTomorrow').max())

#to find instances where the temp at 3 pm is higher than 35 or rain today is no
print(data[(data.Temp3pm>35) | (data.RainToday == 'No')])

