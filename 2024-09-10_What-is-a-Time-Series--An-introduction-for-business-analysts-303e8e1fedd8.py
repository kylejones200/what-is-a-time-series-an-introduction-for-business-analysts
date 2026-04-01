# Description: Short example for What is a Time Series An introduction for business analysts.


# Sample data

import matplotlib.pyplot as plt
import pandas as pd

dates = pd.date_range(start='2025–01–01', end='2025–12–31', freq='D')
values = [10, 12, 15, 14, 11, 13, 16, 14, 12, 15, 17, 19, 18, 16, 14, 12, 14, 17, 15, 13, 11, 14, 16, 18]
# Convert to a pandas Series
ts = pd.Series(values, index=dates)

plt.figure(figsize=(12, 6))
plt.plot(ts)
plt.title('Time Series of Daily Values')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
