from datetime import datetime
import os
import shutil
import sys


def sync_videos(original_path):
    # """Create paths"""
    current_date = datetime.now().strftime("%Y%m%d")
    download_folder = "youtube_downloads"
    local_path = f"/mnt/common/{download_folder}/{current_date}"
    cloud_path = os.path.join(
        os.getenv("HOME"), f"pCloudDrive/myFiles/{download_folder}/{current_date}"
    )

    if not os.path.exists(original_path):
        print(f"Folder {original_path} with youtube videos doesn't exist. Exiting...")
        sys.exit(1)

    if not os.path.exists(local_path):
        try:
            os.makedirs(local_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating local path for final videos: {e}")
            sys.exit(1)

    #    if not os.path.exists(cloud_path):
    #        try:
    #            os.makedirs(cloud_path, exist_ok=True)
    #        except Exception as e:
    #            print(f"Error creating local path for final videos: {e}")
    #            sys.exit(1)

    # """ Copy videos to cloud """
    # Ask if it should be copied to pCloudDrive
    answer = input("\nDo you want to copy video to pcloud? ").strip()

    if answer in ["y", "yes"]:
        if not os.path.exists(cloud_path):
            try:
                os.makedirs(cloud_path, exist_ok=True)
            except Exception as e:
                print(f"Error creating local path for final videos: {e}")
                sys.exit(1)

        print(f"\nCopying to {cloud_path}")
        try:
            shutil.copytree(original_path, cloud_path, dirs_exist_ok=True)
        except Exception as e:
            print(f"Error copying videos to cloud:  {e}")
            sys.exit(1)

    # """ Move videos to local """
    print(f"\nMoving to {local_path}")
    try:
        shutil.copytree(original_path, local_path, dirs_exist_ok=True)
    except Exception as e:
        print(f"Error copying videos to cloud:  {e}")
        sys.exit(1)

    # """ Delete videos download """
    try:
        shutil.rmtree(original_path)
        os.makedirs(original_path)
    except Exception as e:
        print(f"Error deleting youtube videos after doing backed up: {e}")
        sys.exit(1)


if __name__ == "__main__":
    sync_videos(
        "/mnt/common/pythonprojects/smallprojects/29_yt_download_and_sync/yt_downloads"
    )
