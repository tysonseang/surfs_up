# Surfs Up!

## Overview

This project entails writing and executing Python code in Jupyter Notebook, using SQLAlchemy to connect to and query a SQLite database, plotting data in the form of histograms and bar plots using Matplotlib plotting library, and analyzing descriptive statistics that summarize the central tendency, dispersion, and shape of a dataset's distribution. SQLite is a widely used database engine, and SQLAlchemy is a tool designed to query SQLite databases. 

In this hypothetical scenario, I have pitched a new business idea for a surf & ice cream shop on the Hawaiian island of O‘ahu. After presenting my business plan, a potential investor expressed concerns about the potential impact of local weather on customer foot traffic and sales. In order to secure investor backing, I first needed to run some analytics on a weather dataset to analyze temperature and precipitation from a variety of local weather stations. 

## Results
Temperature at the proposed store location is close to perfect year-round. 
- For the month of June, the low (minimum) temperature is 64 degrees, the high (maximum) temperature is 85 degrees, and the average temperature is 75 degrees.

![June_Temp_Summary_Statistics.png](https://github.com/tysonseang/surfs_up/blob/main/June_Temp_Summary_Statistics.png)

- For the month of December, the low (minimum) temperature is 56 degrees, the high (maximum) temperature is 83 degrees, and the average temperature is 71 degrees.

![December_Temp_Summary_Statistics.png](https://github.com/tysonseang/surfs_up/blob/main/December_Temp_Summary_Statistics.png)

- The standard deviations for temperatures during the months of June and December are both low, indicating a minimal dispersion of the data relative to the mean values.

## Summary

As seen in the below histogram, temperature is perfect for surfing and milkshakes throughout the entirety of the year! 

![All_Temperature_Observations.png](https://github.com/tysonseang/surfs_up/blob/main/All_Temperature_Observations.png)

To further analyze the data for the impact of weather on foot traffic, I would look into precipitation data, as rain is the weather type for this region that is most likely to impact sales.

```
#Perform a query to retrieve the data and precipitation scores
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

#Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)

#Sort the dataframe by date
df = df.sort_index()

```

I would then visualize the data in order to better understand rainfall seasonality.

```
#Use Pandas Plotting with Matplotlib to plot the data
df.plot()
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)
```
![Precipitation.png](https://github.com/tysonseang/surfs_up/blob/main/Precipitation.png)

Overall, O‘ahu's beautiful weather makes it a great fit for a business focusing on outdoor activities and ice cream!