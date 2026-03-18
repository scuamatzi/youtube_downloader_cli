import glob
import os
import subprocess


def convert_to_mp3(file_path, extension):
    """
    Convert a file to mp3 format.
    Args:
        file_path(str): folder path with file to convert
        extension(str): extension of the file to be converted (mp4,mov,mpeg,etc)

    Returns:
        True if successfull
        False in case of exception
    """
    mp3_file_name = file_path.replace(f"{extension}", "mp3")
    command = [
        "ffmpeg",
        "-i",
        file_path,
        "-acodec",
        "libmp3lame",
        "-b:a",
        "128k",
        mp3_file_name,
    ]

    try:
        subprocess.run(command)
        return True
    except Exception as e:
        print(f"\nError in convertion to mp3: {e}")
        return False


def convert_last_mp4_to_mp3(path_to_work):
    """
    Find and converts latest mp4 file in 'path_to_work' to mp3 format.

    Args:
        path_to_work(str): folder to look for latest mp4 file to convert to mp3.

    Returns:
        None: if there are not mp4 files in path_to_work
        True: if mp4 file is converted to mp3
        False: in case of exception
    """
    folder = path_to_work

    # Get list of mp4 files
    mp4_files = glob.glob(os.path.join(folder, "*.mp4"))

    if not mp4_files:
        return None

    # Get latest mp4 file
    latest_mp4_file = max(mp4_files, key=os.path.getmtime)

    return convert_to_mp3(latest_mp4_file, "mp4")


if __name__ == "__main__":
    folder = input("Path to mp4 files: ")

    if not convert_last_mp4_to_mp3(folder):
        print("\nNo mp4 files in folder.")
    else:
        print("\nmp4 file converted to mp3.")
