import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to plot monthly bicycle usage
def barplot_monthly_bicycle_usage(data):
    
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    monthly_total_users = data.groupby('mnth')['cnt'].sum() 

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=monthly_total_users.index, y=monthly_total_users.values, estimator=sum, errorbar=None, alpha=0.7, ax=ax)

    for index, value in enumerate(monthly_total_users.values):
        ax.text(index, value, '{:,.0f}'.format(value), ha='center', va='bottom')

    ax.set_title('Distribution of Bike Sharing Users by Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Users')
    ax.set_xticklabels(month_names, rotation=45)
    st.pyplot(fig)
    
# Function to plot trends bicycle in 2011
def lineplot_trends_bicycle_2011(data):
    fig, ax = plt.subplots(figsize=(15, 6))

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Visualization of bicycle usage trends by month for 2011
    sns.lineplot(x='mnth', y='cnt', data=data[data['yr'] == 0], estimator=sum, label='Total Users')
    sns.lineplot(x='mnth', y='registered', data=data[data['yr'] == 0], estimator=sum, label='Registered Users')
    sns.lineplot(x='mnth', y='casual', data=data[data['yr'] == 0], estimator=sum, label='Casual Users')
    ax.set_title('Trends in Bicycle Use in 2011')
    ax.set_xlabel('Month')
    ax.set_ylabel('Users')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(month_names, rotation=45)

    # Add text labels with the values of each line
    for line in ax.lines:
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        for x, y in zip(x_data, y_data):
            ax.text(x, y, '{:,.0f}'.format(y), ha='center', va='bottom')

    st.pyplot(fig)
    
# Function to plot trends bicycle in 2012
def lineplot_trends_bicycle_2012(data):
    fig, ax = plt.subplots(figsize=(15, 6))

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Visualization of bicycle usage trends by month for 2012
    sns.lineplot(x='mnth', y='cnt', data=data[data['yr'] == 1], estimator=sum, label='Total Users')
    sns.lineplot(x='mnth', y='registered', data=data[data['yr'] == 1], estimator=sum, label='Registered Users')
    sns.lineplot(x='mnth', y='casual', data=data[data['yr'] == 1], estimator=sum, label='Casual Users')
    ax.set_title('Trends in Bicycle Use in 2012')
    ax.set_xlabel('Month')
    ax.set_ylabel('Users')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(month_names, rotation=45)

    # Add text labels with the values of each line
    for line in ax.lines:
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        for x, y in zip(x_data, y_data):
            ax.text(x, y, '{:,.0f}'.format(y), ha='center', va='bottom')
            
    st.pyplot(fig)
    
# Function to plot The Influence of Seasons on Bicycle Use
def plot_season_barplot(data):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='season', y='cnt', data=data, estimator=sum, errorbar=None, alpha=0.7, ax=ax)

    for index, value in enumerate(data.groupby('season')['cnt'].sum()):
        ax.text(index, value, '{:,.0f}'.format(value), ha='center', va='bottom')

    ax.set_xticks(ticks=[0, 1, 2, 3])
    ax.set_xticklabels(labels=['Spring', 'Summer', 'Fall', 'Winter'])
    ax.set_title('The Influence of Seasons on Bicycle Use')
    ax.set_ylabel('Total Users')
    st.pyplot(fig)
    
# Function to plot The Influence of Seasons on Bicycle Use (comparison 2011 and 2012)
def plot_season_comparison_barplot(data_2011, data_2012):
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    
    # Calculate the total users for each season in each year
    seasonal_total_users_2011 = data_2011.groupby('season')['cnt'].sum()
    seasonal_total_users_2012 = data_2012.groupby('season')['cnt'].sum()

    # Set the width for each bar
    bar_width = 0.35

    # Set the position for each bar
    r1 = np.arange(len(seasons))
    r2 = [x + bar_width for x in r1]


    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(r1, seasonal_total_users_2011, color='skyblue', width=bar_width, label='2011', alpha=0.7)
    ax.bar(r2, seasonal_total_users_2012, color='salmon', width=bar_width, label='2012', alpha=0.7)

    # Add text labels with the values of each bar
    for i, value in enumerate(seasonal_total_users_2011):
        ax.text(i, value, '{:,.0f}'.format(value), ha='center', va='bottom', color='black')
    for i, value in enumerate(seasonal_total_users_2012):
        ax.text(i + bar_width, value, '{:,.0f}'.format(value), ha='center', va='bottom', color='black')

    ax.set_xticks([r + bar_width/2 for r in range(len(seasons))])
    ax.set_xticklabels(seasons)
    ax.set_title('The Influence of Seasons on Bicycle Use (2011 vs 2012)')
    ax.set_ylabel('Total Users')
    st.pyplot(fig)

# Function to plot The Effect of Weather on Bicycle Use
def plot_weathersit_barplot(data):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='weathersit', y='cnt', data=data, estimator=sum, errorbar=None, alpha=0.7, ax=ax)

    for index, value in enumerate(data.groupby('weathersit')['cnt'].sum()):
        ax.text(index, value, '{:,.0f}'.format(value), ha='center', va='bottom')

    ax.set_xticks(ticks=[0, 1, 2])
    ax.set_xticklabels(labels=['Clear with Few Clouds', 'Foggy and Overcast', 'Light Rain or Snow'])
    ax.set_title('The Effect of Weather on Bicycle Use')
    ax.set_ylabel('Total Users')
    st.pyplot(fig)
    
# Function to plot The Effect of Weather on Bicycle Use (comparison 2011 and 2012)
def plot_weathersit_comparison_barplot(data_2011, data_2012):
    weathersit = ['Clear with Few Clouds', 'Foggy and Overcast', 'Light Rain or Snow']
    
    # Calculate the total users for each season in each year
    weathersit_total_users_2011 = data_2011.groupby('weathersit')['cnt'].sum()
    weathersit_total_users_2012 = data_2012.groupby('weathersit')['cnt'].sum()

    # Set the width for each bar
    bar_width = 0.35

    # Set the position for each bar
    r1 = np.arange(len(weathersit))
    r2 = [x + bar_width for x in r1]

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot barplots for each year
    ax.bar(r1, weathersit_total_users_2011, color='skyblue', width=bar_width, label='2011', alpha=0.7)
    ax.bar(r2, weathersit_total_users_2012, color='salmon', width=bar_width, label='2012', alpha=0.7)

    # Add text labels with the values of each bar
    for i, value in enumerate(weathersit_total_users_2011):
        ax.text(i, value, '{:,.0f}'.format(value), ha='center', va='bottom', color='black')
    for i, value in enumerate(weathersit_total_users_2012):
        ax.text(i + bar_width, value, '{:,.0f}'.format(value), ha='center', va='bottom', color='black') 

    ax.set_xticks([r + bar_width/2 for r in range(len(weathersit))])
    ax.set_xticklabels(weathersit) 
    ax.set_title('The Effect of Weather on Bicycle Use (2011 vs 2012)')
    ax.set_ylabel('Total Users')
    st.pyplot(fig)


def main():
    st.title('Bike Sharing Users')

    # Load data
    file_path = './dashboard/day.csv'
    data = load_data(file_path)

    data_2011 = data[data['yr'] == 0]
    data_2012 = data[data['yr'] == 1]
    
    datetime_columns = ["dteday"]
    data.sort_values(by="dteday", inplace=True)
    data.reset_index(inplace=True)

    for column in datetime_columns:
        data[column] = pd.to_datetime(data[column])

    # Filter data
    min_date = data["dteday"].min()
    max_date = data["dteday"].max()

    with st.sidebar:
        # st.subheader('Nama: Ridhan Al Aufar')
        # st.subheader('Email: ridhan783@gmail.com')
        # st.subheader('ID Dicoding: ridhann_4')
    
        # Mengambil start_date & end_date dari date_input
        start_date, end_date = st.date_input(
            label='Rentang Waktu', min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )

    main_df = data[(data["dteday"] >= str(start_date)) & 
                    (data["dteday"] <= str(end_date))]

    st.subheader('Data Preview')
    st.write(main_df.head())
    
    col1, col2 = st.columns(2)

    with col1:
        working_days = data[data['workingday'] == 1]['workingday'].count()
        st.metric("Total Working Days", value=working_days)

    with col2:
        total_users = data['cnt'].sum()
        formatted_total_users = '{:,.0f}'.format(total_users)
        st.metric("Total Users", value=formatted_total_users)

    st.subheader('Distribution of Bike Sharing Users by Month')
    barplot_monthly_bicycle_usage(main_df)
    
    st.subheader('Trends in Bicycle Use in 2011')
    lineplot_trends_bicycle_2011(main_df)
    
    st.subheader('Trends in Bicycle Use in 2012')
    lineplot_trends_bicycle_2012(main_df)
    
    st.subheader('The Influence of Seasons on Bicycle Use')
    plot_season_barplot(main_df)

    st.subheader('The Influence of Seasons on Bicycle Use (2011 vs 2012)')
    plot_season_comparison_barplot(data_2011, data_2012)

    st.subheader('The Effect of Weather on Bicycle Use')
    plot_weathersit_barplot(main_df)

    st.subheader('The Effect of Weather on Bicycle Use (2011 vs 2012)')
    plot_weathersit_comparison_barplot(data_2011, data_2012)

if __name__ == "__main__":
    main()


st.caption('Copyright © Ridhan Al Aufar 2024')
