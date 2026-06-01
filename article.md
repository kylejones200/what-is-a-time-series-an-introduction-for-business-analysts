# What is a Time Series? An introduction for business analysts A time series is a sequence of data points collected over time, usually
at regular intervals. These data points can represent various...

### What is a Time Series? An introduction for business analysts 

#### A time series is a sequence of data points collected over time, usually at regular intervals. These data points can represent various measurements or observations, such as stock prices, weather patterns, or product sales.
Time series analysis deals with the examination of data points collected over time. Unlike cross-sectional data, which captures a snapshot of a phenomenon at a single point in time, time series data consists of a sequence of observations recorded at regular intervals. These data points can represent various measurements or indicators, such as stock prices, weather patterns, retail sales, or macroeconomic indicators like inflation and GDP.

The distinguishing characteristic of time series data is the *temporal order of the observations*. This sequential nature allows analysts to study the evolution of a variable over time, identify trends and patterns, and potentially make forecasts about future values. Time series data is used across many fields, from business and economics to science and social research. Understanding how to properly analyze and model time series data is a critical skill for data scientists, analysts, and decision-makers.

#### Qualitative and quantitative forecasting
There are two main approaches to forecasting: qualitative and quantitative. Qualitative forecasting involves gathering experts together and relying on their subjective opinions and experiences. For example, they might say that whenever there's a Super Bowl and the average temperature is high, and crickets are chirping 10 times a minute, they normally think a certain outcome will occur. This type of qualitative forecasting can be accurate over time as experts develop their intuition, but it is difficult to replicate.

In contrast, quantitative forecasting uses mathematical formulas and models applied to data to predict future values. This is the focus of the discussion, rather than the more subjective qualitative methods.

#### Components of Time Series
When examining a time series, it is useful to break down the data into its core components.

1.  [Trend: The overall direction of the data, whether it is increasing, decreasing, or staying relatively flat over time. A time series may exhibit an upward trend, a downward trend, or no clear trend at all (a flat or stationary series).]
2.  [Seasonality: Periodic fluctuations in the data that occur at regular intervals, such as daily, weekly, or yearly patterns. Seasonality is often driven by external factors like weather, holidays, or systematic human behaviors.]
3.  [Stationarity: The statistical properties of the time series, such as the mean and variance, remaining constant over time. These cycles may be caused by economic, political, or other macroeconomic factors.]
4.  [Noise: Random variations in the data that cannot be explained by the trend or seasonality components.]

These components help us analyze and model time series data.

#### A simple example
Let's consider a example to illustrate these concepts. Suppose we are analyzing monthly sales data for a retail company over the past 5 years. We might observe the following:

- Trend: The overall sales figures have been steadily increasing over the 5-year period, indicating an upward trend in the business.
- Seasonality: There are clear seasonal patterns in the data, with higher sales occurring during the holiday months of November and December, and lower sales during the summer months.
- Stationarity: Beyond the annual seasonal cycles, there may also be broader economic cycles that influence the company's sales, such as a recession or expansion in the broader retail sector.
- Irregularity/Error/Noise: Even after accounting for the trend and seasonal components, there will likely be some unexplained month-to-month variations in the sales figures, which can be attributed to random, unpredictable factors.

Decomposing the time series in this way provides valuable insights into the underlying dynamics driving the data, which can then inform forecasting models, strategic planning, and other business decisions.


<h1 id="an-error-occurred." class="message">An error occurred.</h1>

Unable to execute JavaScript.

#### Converting Data to a Time Series
To effectively analyze time series data, it is first necessary to convert the raw data into a format that preserves the temporal ordering and structure of the observations. In Python, the primary data structure used for time series analysis is the \`pandas.Series\` object, which is a one-dimensional labeled array that can handle the date/time indexing inherent to time series data.

Here's a simple example of how to create a \`pandas.Series\` object from a list of values with corresponding dates:


In this example, we first create a \`DatetimeIndex\` object using the \`pd.date_range()\` function, which generates a sequence of daily dates from January 1, 2025 to December 31, 2025. We then assign a list of corresponding data values to this index, and pass both the values and the index to the \`pd.Series()\` constructor to create a time series object.

The resulting \`ts\` variable is a \`pandas.Series\` object, which has the following properties:

Index: The dates representing the temporal ordering of the observations. Values: The actual data points, which can be numeric, categorical, or a mix of data types.

Once the data is in this time series format, we can begin to analyze the components and characteristics of the data, such as trend, seasonality, and stationarity.

#### Visualizing Time Series Data
One of the most effective ways to gain initial insights into a time series is through visualization. By plotting the data points over time, we can quickly identify patterns, trends, and anomalies that may not be immediately apparent from the raw numbers alone.

The \`matplotlib\` and \`seaborn\` libraries in Python provide powerful tools for visualizing time series data. Here's an example of how to create a basic line plot of the time series we created earlier:


This will generate a line plot that displays the values of the time series over the course of the year. From this visualization, we can start to observe potential trend and seasonal patterns in the data.

More advanced time series visualizations can include:

- Scatter plots: Plotting the values against the time index to identify patterns and outliers.
- Bar charts: Showing the values aggregated by time period (e.g., monthly or yearly).
- Heatmaps: Representing the values in a grid format, often used for visualizing seasonality.
- Autocorrelation plots: Depicting the correlation between the series and its own lagged values, useful for identifying cyclical patterns.

Visualization really helps in time series analysis. We are visual creatures and graphs can give us an intuitive understanding of the data and guide our subsequent modeling and forecasting efforts.


<figcaption>An example from another project I did where you can see the demand for energy over time.</figcaption>


#### Stationarity and Transformations
One important concept in time series analysis is the idea of stationarity. A stationary time series is one whose statistical properties, such as the mean and variance, do not change over time. In other words, the underlying process generating the data has a constant behavior.

Non-stationary time series, on the other hand, exhibit changes in these statistical properties over time. This can be problematic for many standard time series modeling techniques, as they often assume the data is stationary.

There are several ways to test for stationarity, such as the Augmented Dickey-Fuller (ADF) test. If a time series is found to be non-stationary, there are various transformations that can be applied to make it stationary, such as:

- Differencing: Taking the difference between consecutive observations to remove trends and make the series stationary.
- Logarithmic transformation: Applying a log transform to stabilize the variance of the series.
- Seasonal differencing: Taking the difference between an observation and the corresponding observation from the previous season (e.g., year-over-year differences).

These transformations can help ensure that the time series meets the assumptions required for many modeling techniques, improving the accuracy and reliability of the analysis. Some python tools will do this work for you.

#### Modeling and Forecasting
Once we have a solid understanding of the components and characteristics of a time series, we can begin to develop models to describe the data and make forecasts about future values. There are numerous time series modeling approaches, ranging from simple moving averages to more sophisticated techniques like autoregressive integrated moving average (ARIMA) models.

The specific modeling approach chosen will depend on the characteristics of the time series, the purpose of the analysis, and the desired level of accuracy and complexity. Regardless of the modeling technique, the general process for time series modeling and forecasting typically involves the following steps:

1.  [Data Preparation: Ensuring the time series is in the appropriate format, handling missing values, and transforming the data as needed to achieve stationarity.]
2.  [Exploratory Data Analysis: Visualizing the data, identifying trend and seasonal patterns, and assessing the stationarity of the series.]
3.  [Model Selection: Choosing an appropriate time series model based on the characteristics of the data and the forecasting objectives.]
4.  [Model Estimation: Fitting the selected model to the historical data and estimating the model parameters.]
5.  [Model Evaluation: Assessing the accuracy and reliability of the model through techniques like cross-validation and residual analysis.]
6.  [Forecasting: Using the fitted model to generate predictions of future values.]
7.  [Monitoring and Updating: Continuously monitoring the accuracy of the forecasts and updating the model as new data becomes available.]

Time series modeling and forecasting is fun and has many applications. Here is an example project I've done with forecasting.

[Time Series forecasting of natural gas prices with Python *A common task in finance is forecasting values. There are several methods for creating forecasts such as ARIMA...*medium.com](https://medium.com/@kylejones_47003/time-series-forecasting-of-natural-gas-prices-with-python-b21c0d11019d "https://medium.com/@kylejones_47003/time-series-forecasting-of-natural-gas-prices-with-python-b21c0d11019d")[](https://medium.com/@kylejones_47003/time-series-forecasting-of-natural-gas-prices-with-python-b21c0d11019d)
#### Reflection Questions
1.  [How can you define the changes happening in a given time series? By identifying the trend, seasonality, and stationarity of the data, you can describe the overall changes and patterns occurring in the time series.]
2.  [What are the implications of trend and seasonality in time series data? Trend and seasonality have important implications for forecasting, decision-making, and understanding the underlying factors driving the data. Trend can indicate long-term growth or decline, while seasonality can help identify recurring patterns that may influence business operations, planning, and strategy.]

### Related Stories
- [[ARIMA Models and Time Series Forecasting for Business Analytics](https://medium.com/@kylejones_47003/arima-models-and-time-series-forecasting-for-business-analytics-97c5c870e9c6)]
- [[Time Series Forecast Evaluation for Business Analytics](https://medium.com/@kylejones_47003/time-series-forecast-evaluation-for-business-analytics-3f5b6a634717)]
- [[Using Trends in Time Series for Business Analysis](https://medium.com/@kylejones_47003/using-trends-in-time-series-for-business-analysis-0d79f4b93ca9)]
