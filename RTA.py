#Import neccesary libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Title 
st.title("Road Traffic Accidents")
#introduction
st.write("The RTA is to show the accidedents that occur, major causes, build models that predict injury severity of injured accidents, the road conditions monitoring and by data visualization ,creating dashboards and reports to present accident data in a visually accessible maner to help in informed decisions.")
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
# Specify the format for the 'Time' column
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S')

# Create a new column 'Time_of_day' as a formatted string
data['Time_of_day'] = data['Time'].dt.strftime('%H:%M')

# Streamlit app
st.write("Data loaded successfully!")

#displaying the data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)
    #creating the visualizations
# Bar plot for Day_of_week
day_of_week_counts = data['Day_of_week'].value_counts().reset_index()
day_of_week_counts.columns = ['Day_of_week', 'Count']

fig = px.bar(day_of_week_counts, x='Day_of_week', y='Count', title='Accidents by Day of the Week')
fig.update_xaxes(categoryorder='total ascending')
fig.update_xaxes(tickangle=45)
fig.show()
# Pie chart for Accident Severity
accident_severity_counts = data['Accident_severity'].value_counts().reset_index()
accident_severity_counts.columns = ['Accident_severity', 'Count']

fig = px.pie(accident_severity_counts, names='Accident_severity', title='Distribution of Accident Severity')
fig.show()
# Create a scatter plot
fig = px.scatter(data, x='Age_band_of_driver', y='Number_of_casualties', color='Accident_severity',
                 title='Age of Driver vs. Number of Casualties by Accident Severity')
fig.update_xaxes(title='Age of Driver')
fig.update_yaxes(title='Number of Casualties')
fig.show()
# Box plot for Age Distribution by Accident Severity
fig = px.box(data, x='Accident_severity', y='Age_band_of_driver', color='Accident_severity',
             title='Age Distribution by Accident Severity')
fig.update_xaxes(title='Accident Severity')
fig.update_yaxes(title='Age of Driver')
fig.show()
# Violin plot for Age Distribution by Accident Severity
fig = px.violin(data, x='Accident_severity', y='Age_band_of_driver', color='Accident_severity',
               title='Age Distribution by Accident Severity (Violin Plot)')
fig.update_xaxes(title='Accident Severity')
fig.update_yaxes(title='Age of Driver')
fig.show()
# Scatter plot for Light Conditions vs. Weather Conditions
fig = px.scatter(data, x='Light_conditions', y='Weather_conditions', color='Accident_severity',
                 title='Light Conditions vs. Weather Conditions by Accident Severity')
fig.update_xaxes(title='Light Conditions')
fig.update_yaxes(title='Weather Conditions')
fig.show()




































