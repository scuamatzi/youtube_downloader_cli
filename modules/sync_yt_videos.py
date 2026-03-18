from datetime import datetime
import os
import shutil
import sys


def verify_source_folder_exists(source_folder):
    if not os.path.exists(source_folder):
        print(f"Folder {source_folder} with youtube videos doesn't exist. Exiting...")
        sys.exit(1)


def create_local_dest_folder(dest_folder):
    if not os.path.exists(dest_folder):
        try:
            os.makedirs(dest_folder, exist_ok=True)
        except Exception as e:
            print(f"Error creating local path for final videos: {e}")
            sys.exit(1)


def copy_to_cloud(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        try:
            os.makedirs(dst_folder, exist_ok=True)
        except Exception as e:
            print(f"Error creating local path for final videos: {e}")
            sys.exit(1)

    print(f"\nCopying to {dst_folder}")
    try:
        shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)
    except Exception as e:
        print(f"Error copying videos to cloud:  {e}")
        sys.exit(1)


def move_videos_to_local_folder(src_folder, dst_folder):
    try:
        shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)
    except Exception as e:
        print(f"Error copying videos to {dst_folder}:  {e}")
        sys.exit(1)

    # Delete videos download
    try:
        shutil.rmtree(src_folder)
        os.makedirs(src_folder)
    except Exception as e:
        print(f"Error deleting youtube videos after doing backup: {e}")
        sys.exit(1)


def sync_videos(original_path):
    """
    Copy files from 'original_path' to cloud then move them to local folder.
    Use current date to organize files.

    Args:
        original_path(str): folder to sync

    Returns:
        None if everything is ok
        Exit if exception raises
    """

    # Create paths
    current_date = datetime.now().strftime("%Y%m%d")
    DOWNLOAD_FOLDER = "youtube_downloads"
    local_dest_path = f"/mnt/common/{DOWNLOAD_FOLDER}/{current_date}"
    cloud_dest_path = os.path.join(
        os.getenv("HOME"), f"pCloudDrive/myFiles/{DOWNLOAD_FOLDER}/{current_date}"
    )

    verify_source_folder_exists(original_path)

    create_local_dest_folder(local_dest_path)

    # Ask if it should be copied to pCloudDrive
    answer = input("\nDo you want to copy video to pcloud? ").strip()
    if answer in ["y", "yes"]:
        copy_to_cloud(original_path, cloud_dest_path)

    # Move videos to final local folder
    print(f"\nMoving to {local_dest_path}")
    move_videos_to_local_folder(original_path, local_dest_path)


if __name__ == "__main__":
    sync_videos(
        "/mnt/common/pythonprojects/smallprojects/29_yt_download_and_sync/yt_downloads"
    )
