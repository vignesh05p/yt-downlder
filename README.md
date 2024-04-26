
### README.md for YouTube Video Downloader

# YouTube Video Downloader

![Home Page](https://github.com/vignesh05p/yt-downlder/blob/master/images/homee.PNG)

Welcome to the YouTube Video Downloader project! This application allows users to download YouTube videos in various formats and resolutions. It's built using Streamlit, a framework for creating interactive web applications in Python.

## Features
- **Video Downloading**: Download YouTube videos in MP4 or MP3 format.
- **Resolution Selection**: Choose from multiple video resolutions (1080p, 720p, 480p).
- **Responsive Design**: Works on desktops and mobile devices.
- **User-Friendly Interface**: Intuitive design with a clear layout.

## Setup Instructions
To run this project locally, follow these steps:

1. **Clone the Repository**: Clone the GitHub repository to your local machine.
   ```bash
   git clone https://github.com/vignesh05p/yt-downlder.git
   ```

2. **Navigate to the Project Directory**: Move into the project folder.
   ```bash
   cd yt-downlder
   ```

3. **Install Dependencies**: Install the necessary Python packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**: Start the Streamlit server to run the application.
   ```bash
   streamlit run app.py
   ```

5. **Access the App**: Open the provided URL in your web browser to interact with the app.

## Phone Interface
Here's how the app looks on a mobile device:

![Phone Interface](https://github.com/vignesh05p/yt-downlder/blob/master/images/phone.PNG)

## Notes
- The app relies on `pytube` to download YouTube videos. Ensure you're using a version that supports the latest YouTube features.
- The download location is determined by your browser's settings. On mobile devices, files typically go to the "Downloads" folder or equivalent.
- If you encounter issues, ensure your Streamlit version is up to date and check your internet connection.

## Contributing
Contributions to this project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Make sure your code follows the project's style and includes necessary documentation.
