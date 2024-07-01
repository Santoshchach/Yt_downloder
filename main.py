import streamlit as st
from pytube import YouTube

# Function to download a YouTube video
def download_youtube_video(url, output_path='.'):
    try:
        # Create YouTube object
        yt = YouTube(url)
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        # Download the video to the specified output path
        stream.download(output_path)
        return f"Downloaded: {yt.title}"
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
def main():
    st.title("YouTube Video Downloader")

    # Input for YouTube video URL
    video_url = st.text_input("Enter the YouTube video URL")

    # Button to trigger download
    if st.button("Download"):
        if video_url:
            message = download_youtube_video(video_url)
            st.success(message)
        else:
            st.error("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    main()
