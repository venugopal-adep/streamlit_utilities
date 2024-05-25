import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go
import plotly.express as px

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return sentiment, subjectivity

def main():
    st.set_page_config(page_title="Sentiment Analyzer", page_icon=":smiley:", layout="wide")
    st.title("Text Sentiment Analyzer")
    st.sidebar.markdown("Enter your text below to analyze its sentiment and subjectivity.")

    text_input = st.sidebar.text_area("Enter your text here", height=5)

    if st.sidebar.button("Analyze Sentiment"):
        sentiment_score, subjectivity_score = analyze_sentiment(text_input)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Sentiment Analysis")
            sentiment_fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=sentiment_score,
                title={'text': "Sentiment"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [-1, 1]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [-1, -0.5], 'color': "red"},
                        {'range': [-0.5, 0.5], 'color': "yellow"},
                        {'range': [0.5, 1], 'color': "green"}
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 4},
                        'thickness': 0.75,
                        'value': sentiment_score
                    }
                },
                delta={'reference': 0}
            ))
            st.plotly_chart(sentiment_fig)

        with col2:
            st.subheader("Subjectivity Analysis")
            subjectivity_fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=subjectivity_score,
                title={'text': "Subjectivity"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [0, 1]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 0.5], 'color': "lightblue"},
                        {'range': [0.5, 1], 'color': "darkblue"}
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 4},
                        'thickness': 0.75,
                        'value': subjectivity_score
                    }
                },
                delta={'reference': 0.5}
            ))
            st.plotly_chart(subjectivity_fig)


if __name__ == "__main__":
    main()