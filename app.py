import streamlit as st
from pytube import YouTube
import os
from pytube.exceptions import VideoUnavailable
from time import sleep

# Get the user's Downloads folder path
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Apply custom styles with Streamlit's `unsafe_allow_html` feature
st.markdown(
    """
    <style>
    /* Default gradient background */
    .stApp {
        background: linear-gradient(90deg, red, blue, purple);
        background-size: 400% 400%;
        animation: Gradient 10s ease infinite; /* Continuous movement */
        color: white; /* Text color */
    }

    /* Keyframes for gradient movement */
    @keyframes Gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* Water wave effect on hover */
    .stApp:hover {
        animation: WaveEffect 2s infinite; /* Wave animation */
    }

    /* Keyframes for water wave animation */
    @keyframes WaveEffect {
        0% {background-position: 0% 50%;}
        50% {background-position: 50% 100%;}
        100% {background-position: 0% 50%;}
    }

    /* Shadow and glow effects for input boxes */
    .stTextInput {
        background-color: lightgray;
        padding: 10px;
        border: 2px solid lightgray;
        border-radius: 5px;
        box-shadow: 3px 3px 5px gray; /* Shadow effect */
        transition: 0.3s; /* Smooth transitions */
    }

    /* Glow effect on hover */
    .stTextInput:hover {
        border-color: red;
        box-shadow: 5px 5px 10px red; /* Glow effect */
    }

    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a YouTube logo and title
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/9/98/YouTube_Logo.svg",
    width=100,
)  # YouTube logo
st.title("YouTube Video Downloader")

# Input field for YouTube video URL
video_url = st.text_input(
    "Enter YouTube video URL", placeholder="Enter a valid YouTube URL"
)

# Format options
format_choice = st.radio("Select Format", ("MP4", "MP3"))

# Resolution options
resolution_choice = st.selectbox("Select Resolution", ["1080p", "720p", "480p"])

# Button to start the download process
if st.button("Download"):
    if video_url:
        try:
            # Display animation during download
            with st.spinner("Downloading, please wait..."):
                for _ in range(3):
                    st.text("🐇")  # Simple animation
                    sleep(1)

            # Initialize YouTube object
            yt = YouTube(video_url)

            # Check if the video is age-restricted
            if yt.age_restricted:
                raise VideoUnavailable("This video is age-restricted and cannot be downloaded.")

            # Set stream according to format and resolution
            if format_choice is "MP4":
                stream = yt.streams.filter(
                    file_extension="mp4", res=resolution_choice
                ).first()
            else:
                stream = yt.streams.filter(only_audio=True).first()

            # Ensure the Downloads folder exists
            os.makedirs(downloads_folder, exist_ok=True)

            # Save the video in the Downloads folder
            filename = f"{yt.title}.{format_choice.lower()}"
            filepath = os.path.join(downloads_folder, filename)

            stream.download(output_path=downloads_folder, filename=yt.title)

            # Display success message
            st.success(f"Downloaded '{yt.title}' in {format_choice} format to your Downloads folder!")

        except VideoUnavailable as e:
            st.warning(f"Error: {e}")

        except Exception as e, you'd rather
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a YouTube video URL.")

# Add a footer with custom text
st.markdown(
    """
    <div class="footer">
        <h5>Made with love by Vignesh Prabhu</h5>
    </div>
    """,
    unsafe_allow_html=True,
)
