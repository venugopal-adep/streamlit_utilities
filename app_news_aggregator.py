import streamlit as st
import feedparser

# Define the URLs of the RSS feeds you want to aggregate
rss_feeds = {
    "BBC News": "http://feeds.bbci.co.uk/news/rss.xml",
    "NY Times": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "The Times of India": "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    "The Hindu": "https://www.thehindu.com/news/feeder/default.rss",
    "India Today": "https://www.indiatoday.in/rss/home"
}

def fetch_news(rss_url):
    """ Fetches news from a given RSS feed URL and returns parsed entries """
    feed = feedparser.parse(rss_url)
    return feed.entries

def display_news():
    """ Displays news entries using Streamlit components """
    st.title("News Aggregator")
    
    # Dropdown to select news source
    source = st.sidebar.selectbox("Select News Source", list(rss_feeds.keys()))
    
    # Fetching news entries from the selected source
    entries = fetch_news(rss_feeds[source])
    
    for entry in entries:
        st.subheader(entry.title)
        st.write(entry.summary)
        st.markdown(f"[Read more]({entry.link})")

if __name__ == "__main__":
    display_news()
