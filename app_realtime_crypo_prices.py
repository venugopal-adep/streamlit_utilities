import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Set page title and layout
st.set_page_config(page_title='Cryptocurrency Price Tracker', layout='wide')

# Function to fetch cryptocurrency data from API
def fetch_crypto_data(coin):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true'
    response = requests.get(url)
    data = response.json()
    return data

# Function to fetch historical price data
def fetch_historical_data(coin, days):
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}'
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit app
def main():
    # Add a title and subtitle
    st.title('Cryptocurrency Price Tracker')
    st.markdown('Track real-time prices and trends of popular cryptocurrencies.')

    # Sidebar for cryptocurrency selection
    coins = ['bitcoin', 'ethereum', 'litecoin', 'ripple', 'cardano']
    selected_coin = st.sidebar.selectbox('Select a cryptocurrency', coins)

    # Fetch cryptocurrency data
    coin_data = fetch_crypto_data(selected_coin)

    # Display cryptocurrency information
    st.subheader(f'{selected_coin.capitalize()}')
    st.write(f'Current Price: ${coin_data[selected_coin]["usd"]:.2f}')
    st.write(f'24h Change: {coin_data[selected_coin]["usd_24h_change"]:.2f}%')
    st.write(f'Market Cap: ${coin_data[selected_coin]["usd_market_cap"]:,.0f}')

    # Fetch historical price data
    days = st.slider('Select the number of days', min_value=1, max_value=365, value=30)
    historical_data = fetch_historical_data(selected_coin, days)

    # Prepare data for plotting
    prices = historical_data['prices']
    df = pd.DataFrame(prices, columns=['Date', 'Price'])
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')

    # Create an interactive line plot using Plotly
    fig = px.line(df, x='Date', y='Price', title=f'{selected_coin.capitalize()} Price Trend')
    fig.update_layout(xaxis_title='Date', yaxis_title='Price (USD)')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()