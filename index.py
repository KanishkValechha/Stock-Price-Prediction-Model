import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the web app
st.title('Stock Price Prediction')

# Load data from a CSV file
data = pd.read_csv('C:/Users/kanis/Downloads/predicted_stock_prices_with_weekly_data.csv', index_col=0)

# Create a sidebar for navigation
sidebar = st.sidebar
sidebar.title('Select a company')

# Get unique company names from the DataFrame
company_names = data.columns[1:]  # Assuming the first column is 'Date'

# Create a selectbox in the sidebar with company names
selected_company = sidebar.selectbox('', company_names)

# Display the predicted price and graph for the selected company
if selected_company:
    # Display the predicted price
    predicted_price = data.loc[selected_company, 'Predicted Closing Price']
    if pd.notnull(predicted_price):
        st.write(f"The predicted closing price for {selected_company} is: **${predicted_price:.2f}**")

        # Plot the weekly graph
        fig, ax = plt.subplots()
        # Generate a range of days for the x-axis
        days = list(range(13, len(data[selected_company][1:]) + 14))  # +2 to include the predicted price day
        # Plot the actual prices
        actual_prices = data[selected_company][1:]  # Skip the first row which is the predicted price
        ax.plot(days[:-1], actual_prices, marker='o', linestyle='-', label='Actual Price')  # Exclude the last day for actual prices
        # Highlight the predicted price on the graph
        ax.scatter(days[-1], predicted_price, color='red', label='Predicted Price', zorder=5)
        ax.set_xlabel("Days")
        ax.set_ylabel("Adjusted Closing Price")
        ax.set_title(f"Weekly Stock Price History for {selected_company}")
        ax.legend()
        st.pyplot(fig)
