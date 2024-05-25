import streamlit as st
from pytube import YouTube
import os

# Title of the application
st.title('YouTube Video Downloader')

# Taking the URL of the YouTube video from the user
url = st.text_input('Enter the URL of the YouTube video you wish to download:', '')

if url:
    yt = YouTube(url)
    st.write(f"*Video Title:* {yt.title}")
    st.write(f"*Video Length:* {yt.length // 60} minutes {yt.length % 60} seconds")
    st.write(f"*Number of Views:* {yt.views}")
    st.image(yt.thumbnail_url)

    # Let the user choose the stream
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    options = [(i.itag, i.resolution) for i in stream]
    itag = st.selectbox('Choose the quality/resolution of the video to download:', options, format_func=lambda x: x[1])

    # Specify the download path
    download_path = st.text_input('Enter the download path:', '')

    if st.button('Download Video'):
        selected_stream = stream.get_by_itag(itag[0])
        with st.spinner('Downloading...'):
            # Download the video to the specified path
            selected_stream.download(output_path=download_path)
        st.success('Downloaded Successfully!')
        st.balloons()
