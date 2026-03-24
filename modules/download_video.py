import os
from rich.console import Console
import yt_dlp
import sys

console = Console()


def download_video(url, download_path="yt_downloads"):
    """
    Download a youtube video to the specified folder

    Args:
        url(str): URL youtube video
        download_path(str): Folder to save video - default -> "yt_downloads"

    Returns: None
    """

    # Create download directory if it doesn't exist
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

    console.print(f"\nDownloading video to: {download_path}", style="turquoise4")
    print("This may take a while depending on video size...\n")

    try:
        with console.status(""):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            console.print("\nDownload completed successfully!", style="dodger_blue2")
    except yt_dlp.utils.DownloadError as e:
        console.print(f"\nDownload error: {e}", style="dark_orange")
        sys.exit(1)
    except Exception as e:
        console.print(f"\nAn unexpected error occurred: {e}", style="dark_orange")
        sys.exit(1)


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
