# Library import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path

# Analysis result
df_hour = pd.read_csv("hour.csv")
df_day = pd.read_csv("day.csv")

fig1, ax1 = plt.subplots()
sns.regplot(x = df_day.temp, y = df_day.cnt, line_kws={"color": "tab:orange"}, scatter_kws={"s": 5}, ax=ax1)
plt.ylabel('Bike rental frequency')
plt.xlabel('Normalized Temperature')
plt.title('Correlation between Temperature and Bike Rental Count')

yr_mo = df_hour.groupby(by=['yr','mnth']).agg({'cnt':'sum'})
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fig2, ax2 = plt.subplots(figsize=(10,5))
plt.plot(yr_mo.cnt.tolist()[:12], '-o', label='Year 0')
plt.plot(yr_mo.cnt.tolist()[12:], '-o', label='Year 1')
plt.title('Bike Rent Count Each Month', fontsize=20)
plt.xticks(range(len(month)), month, fontsize=14)
plt.legend()

season = df_day.groupby(by='season').agg({'cnt':'mean'})
fig3, ax3 = plt.subplots()
bars = plt.bar(['Spring', 'Summer', 'Fall', 'Winter'], season.cnt)
bars[0].set_alpha(0.3)
bars[1].set_alpha(0.3)
bars[3].set_alpha(0.3)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Average bike rent', fontsize=12)
plt.title('Average Bike Rent Each Season', fontsize=16)

workingday = df_day.groupby(by='workingday').agg({'cnt':'mean'})
fig4, ax4 = plt.subplots()
bars = plt.bar(['Not Working Day', 'Working Day'], workingday.cnt)
bars[0].set_alpha(0.3)
plt.ylabel('Average bike rent', fontsize=12)
plt.title('Average Bike Rent between Not Working Day vs Working Day', fontsize=16)

weekday = df_day.groupby(by='weekday').agg({'cnt':'sum'})
fig5, ax5 = plt.subplots()
bars = plt.bar(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], weekday.cnt)
plt.xlabel('Days', fontsize=12)
plt.ylabel('Average bike rent', fontsize=12)
plt.title('Average Bike Rent Each Different Day', fontsize=16)

holiday = df_day.groupby(by='holiday').agg({'cnt':'mean'})
fig6, ax6 = plt.subplots()
bars = plt.bar(['Not Holiday', 'Holiday'], holiday.cnt)
bars[1].set_alpha(0.3)
plt.ylabel('Average bike rent', fontsize=12)
plt.title('Average Bike Rent between Holiday vs Not Holiday', fontsize=16)

# Dashboard construction
st.title("Bike Sharing Dashboard")

st.header("Impact of weather situation on bike demand")
st.pyplot(fig1)
st.caption("At high temperatures, there is a tendency for demand for bicycle rental to be higher.")

st.header("Explosion of demand in specific time")
st.pyplot(fig2)
st.pyplot(fig3)
st.pyplot(fig4)
st.pyplot(fig5)
st.pyplot(fig6)
st.caption("There is an increase in demand for bicycle rental during the fall season which occurs from May to September. "
           "Next, the demand for bicycles is higher during weekdays and the increase in demand continues to increase "
           "from Monday to Friday, then decreases on Saturday and Sunday. On national holidays, there is a decrease in "
           "demand for bicycle rental. But on the 4th of July 2012 national holiday, namely the United States' "
           "Independence Day, there was a high demand for bicycle rental.")
