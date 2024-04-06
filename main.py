# How to create a python venv?
# python3 -m venv myenv
# windows: myenv\Scripts\activate
# mac: source myenv/bin/activate
# pip install streamlit streamlit-lottie pandas
# To run the app: streamlit run main.py

import streamlit as st # Cheat sheet here: https://docs.streamlit.io/develop/quick-reference/cheat-sheet
import pandas as pd   # for data manipulation
import plost    # for plots/charts
from streamlit_lottie import st_lottie # for animations

def create_csv():
    # Count the occurrences of each type of weather
    weather_counts = seattle_weather['weather'].value_counts()

    # Create a new DataFrame to store the counts
    weather_counts_df = pd.DataFrame(weather_counts)

    # Rename the columns for clarity
    weather_counts_df.columns = ['count']

    # Reset index to make 'weather' a column instead of an index
    weather_counts_df.reset_index(inplace=True)

    # Rename the columns
    weather_counts_df.columns = ['weather', 'count']

    # Write the DataFrame to a new CSV file
    weather_counts_df.to_csv('weather_counts.csv', index=False)

    print("Weather counts saved to weather_counts.csv file.")

# Icons/emojis in streamlit: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
st.set_page_config(page_title="Weather Dashboard", page_icon=":rain_cloud:", layout="wide", initial_sidebar_state="expanded")

st.title(" :rain_cloud: Weather Dashboard")
# st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True) # to make the heading go up to the top of the window
# 1 rem = 16 pixels in most browsers
# 1 rem = 1 unit of the font-size of the root element (html)

# SIDEBAR
st.sidebar.title('Settings')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])

create_csv();

weather_counts_csv = pd.read_csv("weather_counts.csv")
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

print(stocks.head(10))

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=weather_counts_csv,
        theta='count',
        color='weather',
        legend='bottom', 
        use_container_width=True)
    
# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)


### EXTRA


value = st.toggle("<-- toggle button") # Question: How do you move this button the sidebar?
# print("Value:", value)
fl = st.file_uploader("Upload a file", type=["csv", "txt"])


#Choose a animation here: https://lottiefiles.com/featured
lottie_url = "https://lottie.host/4a8322b4-981b-4d72-8309-0adbb6305351/a4zyCyhizk.json"
st_lottie(lottie_url, width=200, height=200)


