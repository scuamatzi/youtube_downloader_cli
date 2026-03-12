from modules.download_video import download_video
from modules.mp3_conversion import convert_last_mp4_to_mp3
from modules.sync_yt_videos import sync_videos
import os


def main():
    print("=" * 50)
    print("YouTube Video Downloader")
    print("=" * 50)

    # Get video URL
    url = input("\nEnter the Youtube video URL: ").strip()

    # Get download path
    download_path = input(
        "Enter download directory (press enter for default 'yt_downloads'): "
    ).strip()
    if not download_path:
        download_path = "yt_downloads"

    # Download the video
    download_video(url, download_path)

    # Convert to mp3
    mp3_answer = input("\nConvert it to mp3 file?? (y/n): ")
    if mp3_answer in ["y", "yes"]:
        convert_last_mp4_to_mp3(os.path.join(os.getcwd(), download_path))

    # Copy videos to cloud and move to local folder with current date.
    sync_videos(download_path)


if __name__ == "__main__":
    try:
        import yt_dlp

        main()
    except ImportError:
        print("yt-dlp library not found. Installing...")
        import subprocess
        import sys

        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("yt-dlp installed. Please run the script again.")

    except Exception as e:
        print(f"Error: {e}")

    input("\nPress Enter to exit....")
