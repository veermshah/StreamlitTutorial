import streamlit as st
import pandas as pd
import plost

# Function to create and save weather counts to CSV
def create_csv():
    weather_counts = seattle_weather['weather'].value_counts()
    weather_counts_df = pd.DataFrame(weather_counts).reset_index()
    weather_counts_df.columns = ['weather', 'count']
    weather_counts_df.to_csv('weather_counts.csv', index=False)
     
# Set page config
### STEP 0 ###
st.set_page_config(layout="wide")
st.title(":rain_cloud: Weather Dashboard")

# Sidebar settings
st.sidebar.title('Settings')
### STEP 1 ###


# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
### STEP 2 ###

# Load weather data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
create_csv()
weather_counts_csv = pd.read_csv("weather_counts.csv")

# Charts
c1, c2 = st.columns((7,3))
with c1:
    # Line Chart
    ### STEP 3 ###
    pass

with c2:
    # Donut Chart
    ### STEP 4 ###
    pass