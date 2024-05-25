import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Set page title and layout
st.set_page_config(page_title='Stock Market Trends', layout='wide')

# Function to fetch stock data from Yahoo Finance API
@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Streamlit app
def main():
    # Add a title and subtitle
    st.title('Stock Market Trends')
    st.markdown('Visualize stock market trends using line and bar graphs.')

    # Sidebar for user inputs
    st.sidebar.header('User Inputs')
    ticker = st.sidebar.text_input('Enter Stock Ticker Symbol', 'AAPL')
    start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2020-01-01'))
    end_date = st.sidebar.date_input('End Date', pd.to_datetime('today'))

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    if not stock_data.empty:
        # Display stock data
        st.subheader(f'{ticker} Stock Data')
        st.write(stock_data)

        # Create a line graph for closing prices
        st.subheader(f'{ticker} Closing Prices')
        fig_line = px.line(stock_data, x=stock_data.index, y='Close', title=f'{ticker} Closing Prices')
        fig_line.update_layout(xaxis_title='Date', yaxis_title='Closing Price')
        st.plotly_chart(fig_line)

        # Create a bar graph for trading volume
        st.subheader(f'{ticker} Trading Volume')
        fig_bar = px.bar(stock_data, x=stock_data.index, y='Volume', title=f'{ticker} Trading Volume')
        fig_bar.update_layout(xaxis_title='Date', yaxis_title='Trading Volume')
        st.plotly_chart(fig_bar)
    else:
        st.warning('No data available for the selected stock ticker and date range.')

if __name__ == '__main__':
    main()