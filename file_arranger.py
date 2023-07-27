import os
import shutil
import time

download_folder = 'C:/Users/Michael Zatey/Downloads'
videos_folder = 'C:/Users/Michael Zatey/Downloads/videos_folder'
images_folder = 'C:/Users/Michael Zatey/Downloads/images_folder'


def move_videos(file_path):
    destination = os.path.join(videos_folder, os.path.basename(file_path))
    shutil.move(file_path, destination)
    print(f"Moved video file: {file_path} -> {destination}")

def move_images(file_path):
    destination = os.path.join(images_folder, os.path.basename(file_path))
    shutil.move(file_path, destination)
    print(f"Moved image file: {file_path} -> {destination}")

def monitor_download_folder():
    while True:
        for filename in os.listdir(download_folder):
            file_path = os.path.join(download_folder, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()
                if file_extension in ('.mp4', '.avi', '.mov', '.mkv', '.flv'):
                    move_videos(file_path)
                elif file_extension in ('.jpg', '.jpeg', '.png', '.gif'):
                    move_images(file_path)
                else:
                    print(f"Unsupported file format: {filename}")

        time.sleep(10)

if __name__ == "__main__":
    monitor_download_folder()
