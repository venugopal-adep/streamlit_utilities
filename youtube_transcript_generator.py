import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if "youtu.be" in url:
        return url.split("/")[-1]
    if "youtube" in url and "v=" in url:
        return url.split('v=')[1].split('&')[0]
    return None

def fetch_transcript(video_id):
    """Fetch the transcript of a video using its ID"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        return formatted_transcript
    except Exception as e:
        return str(e)

def main():
    """Run the main Streamlit application"""
    st.title('YouTube Video Transcript Extractor')
    
    video_url = st.text_input("Enter YouTube video URL:", "")
    if st.button("Get Transcript"):
        if video_url:
            video_id = get_video_id(video_url)
            if video_id:
                transcript = fetch_transcript(video_id)
                if transcript:
                    st.text_area("Transcript:", value=transcript, height=300)
                else:
                    st.error("Failed to fetch transcript. Make sure the video has captions enabled.")
            else:
                st.error("Invalid YouTube URL")
        else:
            st.error("Please enter a URL")

if __name__ == "__main__":
    main()
