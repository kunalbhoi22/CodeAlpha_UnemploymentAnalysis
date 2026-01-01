import pandas as pd
import matplotlib.pyplot as plt

# loading the data
df = pd.read_csv("data/Unemployment in India.csv")

# fixing column names
df.columns = df.columns.str.strip()

# removing missing values
df = df.dropna()

# converting date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# -------------------------------
# overall unemployment trend
# -------------------------------
monthly_avg = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure()
plt.plot(monthly_avg.index, monthly_avg.values)
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.title("Unemployment Rate in India (2019–2020)")
plt.show()

# -------------------------------
# covid impact
# -------------------------------
pre_covid = monthly_avg[monthly_avg.index < "2020-03-01"]
covid_time = monthly_avg[(monthly_avg.index >= "2020-03-01") & (monthly_avg.index <= "2020-05-31")]
post_covid = monthly_avg[monthly_avg.index > "2020-05-31"]

print("Average unemployment before covid:", round(pre_covid.mean(), 2))
print("Average unemployment during covid:", round(covid_time.mean(), 2))
print("Average unemployment after covid:", round(post_covid.mean(), 2))