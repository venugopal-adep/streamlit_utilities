import streamlit as st
from googleapiclient.discovery import build
import os

# Initialize YouTube API
youtube = build('youtube', 'v3', developerKey='AIzaSyB_7A_vvP_33qO-FyJa9OfvBoWcRPXYt2I')

def get_videos(query):
    # Search for videos on YouTube
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=10,
        type='video',
        videoDuration='medium',  # Filters videos that are 4-20 mins long
        videoLicense='youtube',
        order='rating'  # Sort by rating
    ).execute()

    videos = []
    for item in search_response.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        description = item['snippet']['description']
        videos.append((title, video_id, description))

    return videos

def main():
    st.title('YouTube video search')
    
    # Text input for user query
    query = st.text_input('Enter the topic for search', '')
    if query:
        st.write('Links to YouTube videos you are looking for:', query)
        # Fetch videos
        videos = get_videos(f"{query}")
        
        if videos:
            st.write('Top tutorials:')
            # Display video links
            for title, video_id, description in videos:
                link = f"https://www.youtube.com/watch?v={video_id}"
                st.markdown(f"[{title}]({link})")
                st.text(description)
        else:
            st.write("No videos found. Try refining your search.")

if __name__ == '__main__':
    main()
