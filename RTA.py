#Import neccesary libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Title 
st.title("Analysis of Road Traffic Accidents")
#introduction
st.write("The RTA is to show the accidents that occur, major causes, build models that predict injury severity , the road conditions monitoring and by data visualization ,creating dashboards and reports to present accident data in a visually accessible maner to help in informed decisions,it is also used in predicting the impact of drivers age on accidents and accident forecast by weather conditions.")
#displaying image
st.write("Displaying an image:")
st.image("road accident image.jpg", caption="Road traffic accidents remains a pervasive and critical issue worldwide.This accidents leads to significant loss of life, injuries, and economic coast affecting individuals and the nation.This project enhancing road saftety seeks to address this pressing concern by conducting a comprehensive analysis of road traffic accidents", use_column_width=True)

#Load the dataset and preprocess it

def load_data():
    data = pd.read_csv("RTA Dataset.csv")
    data['Type_of_vehicle'].fillna(method='ffill', inplace=True)
    data.dropna(subset=['Age_band_of_driver'], inplace=True)
    data.to_csv('cleaned_dataset.csv', index=False)
    data['Time_of_day'] = pd.to_datetime(data['Time']).dt.strftime('%H:%M')
    data['Day_part'] = pd.to_datetime(data['Time_of_day']).dt.hour.apply(
        lambda x: 'Morning' if 5 <= x < 12
        else ('Afternoon' if 12 <= x < 17
            else ('Evening' if 17 <= x < 21
                else 'Night')))
    data['Age_group'] = data['Age_band_of_driver'].apply(
        lambda x: 'Young' if '18-30' in x
        else ('Middle-aged' if '31-50' in x
            else 'Senior'))

    data.drop(columns=['Educational_level', 'Service_year_of_vehicle'], inplace=True)
    
    return data

data = load_data()  

#displaying the data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)
    #creating the visualizations
# Pie chart for Accident Severity
accident_severity_counts = data['Accident_severity'].value_counts().reset_index()
accident_severity_counts.columns = ['Accident_severity', 'Count']

fig = px.pie(accident_severity_counts, names='Accident_severity', title='Distribution of Accident Severity')
st.plotly_chart(fig)

# Create a scatter plot
fig = px.scatter(data, x='Age_band_of_driver', y='Number_of_casualties', color='Accident_severity',
                 title='Age of Driver vs. Number of Casualties by Accident Severity')
fig.update_xaxes(title='Age of Driver')
fig.update_yaxes(title='Number of Casualties')
st.plotly_chart(fig)
# Box plot for Age Distribution by Accident Severity
fig = px.box(data, x='Accident_severity', y='Age_band_of_driver', color='Accident_severity',
             title='Age Distribution by Accident Severity')
fig.update_xaxes(title='Accident Severity')
fig.update_yaxes(title='Age of Driver')
st.plotly_chart(fig)
# Violin plot for Age Distribution by Accident Severity
fig = px.violin(data, x='Accident_severity', y='Age_band_of_driver', color='Accident_severity',
               title='Age Distribution by Accident Severity (Violin Plot)')
fig.update_xaxes(title='Accident Severity')
fig.update_yaxes(title='Age of Driver')
st.plotly_chart(fig)
# Scatter plot for Light Conditions vs. Weather Conditions
fig = px.scatter(data, x='Light_conditions', y='Weather_conditions', color='Accident_severity',
                 title='Light Conditions vs. Weather Conditions by Accident Severity')
fig.update_xaxes(title='Light Conditions')
fig.update_yaxes(title='Weather Conditions')
st.plotly_chart(fig)

# Title 
st.title('Impact of Driver Age on Accidents')

# Sidebar for user input
st.sidebar.subheader('Select Age Band of Driver')
age_band = st.sidebar.selectbox('Select Age Band', data['Age_band_of_driver'].unique())

# Filter data based on user-selected age band
filtered_data = data[data['Age_band_of_driver'] == age_band]

# Display insights or predictions based on the selected age band
st.subheader('Insights for the Selected Age Band')
if filtered_data.empty:
    st.write(f'No data available for the selected age band: {age_band}')
else:
    # Create visualizations or perform data analysis
    #  create a bar plot of accident severity for the selected age band.
    accident_severity_counts = filtered_data['Accident_severity'].value_counts().reset_index()
    accident_severity_counts.columns = ['Accident_severity', 'Count']
    fig = px.bar(accident_severity_counts, x='Accident_severity', y='Count', title=f'Accident Severity for {age_band}')
    st.plotly_chart(fig)
# Title 
st.title('Accidents Forecast by Weather Condition')

# Sidebar for user input
st.sidebar.subheader('Select Weather Condition')
selected_weather_condition = st.sidebar.selectbox('Select Weather Condition', data['Weather_conditions'].unique())

# Filter data based on user-selected weather condition
filtered_data = data[data['Weather_conditions'] == selected_weather_condition]

# Display insights or predictions based on the selected weather condition
st.subheader(f'Insights for {selected_weather_condition} Weather Condition')
if filtered_data.empty:
    st.write(f'No data available for the selected weather condition: {selected_weather_condition}')
else:
    # Perform data analysis or provide insights
    # calculate statistics or trends related to accident severity for the selected weather condition.
    accident_severity_counts = filtered_data['Accident_severity'].value_counts().reset_index()
    accident_severity_counts.columns = ['Accident_severity', 'Count']
    st.write('Accident Severity by Weather Condition:')
    st.write(accident_severity_counts)
    
# Create a bar plot for road conditions using Plotly
road_condition_counts = data['Road_surface_conditions'].value_counts().reset_index()
road_condition_counts.columns = ['Road_surface_conditions', 'Count']

st.subheader('Road Conditions Distribution')
fig = px.bar(road_condition_counts, x='Road_surface_conditions', y='Count', title='Distribution of Road Conditions')
st.plotly_chart(fig)



































