import os
import yt_dlp


def download_video(url, download_path="yt_downloads"):
    # Create downloads directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Configure yt-dlp options
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "embedthumbnail": True,
        "writethumbnail": True,
        "embedmetadata": True,
        "quiet": False,
        "no_warnings": False,
        "progress_hooks": [progress_hook],
    }

    print(f"\nDownloading video to: {download_path}")
    print("This may take a while depending on the video size...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def progress_hook(d):
    """Callback function to show download progress."""
    if d["status"] == "downloading":
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        if total:
            percent = d["downloaded_bytes"] / total * 100
            speed = d.get("_speed_str", "N/A")
            eta = d.get("_eta_str", "N/A")
            print(f"\rDownloaded: {percent:.1f}% | Speed: {speed} | ETA: {eta}", end="")
        elif d["status"] == "finished":
            print(f"\rDownload complete!!")
