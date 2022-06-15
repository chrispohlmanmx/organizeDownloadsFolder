import os
import shutil


def is_video_file(filename: str) -> bool:
    filename = filename.lower()
    return filename.endswith('.mp4') or filename.endswith('.mov') or \
           filename.endswith('.wmv') or filename.endswith('.avi') or \
           filename.endswith('.flv') or filename.endswith('.mkv')


def is_image_file(filename: str) -> bool:
    filename = filename.lower()
    return filename.endswith('.jpeg') or filename.endswith('.jpg') or \
           filename.endswith('.png') or filename.endswith('.gif') or \
           filename.endswith('.tiff') or filename.endswith('.psd')


def is_text_file(filename: str) -> bool:
    filename = filename.lower()
    return filename.endswith('.txt') or filename.endswith('.docx') or \
           filename.endswith('.doc') or filename.endswith('.rtf')


def is_executable_file(filename: str) -> bool:
    filename = filename.lower()
    return filename.endswith('.exe')


def is_zipped_file(filename: str) -> bool:
    filename = filename.lower()
    return filename.endswith('.zip') or filename.endswith('.rar') or \
           filename.endswith('.7z') or filename.endswith('.tar')


def move_file(source: str, dest: str):
    shutil.move(source, dest)


def organize_downloads_folder():
    SOURCE = "C:/Users/chris/Downloads"

    with os.scandir(SOURCE) as files:
        for file in files:
            name = file.name
            src = f'{SOURCE}/{name}'
            if is_image_file(name):
                dest = f'{SOURCE}/Images/{name}'
                move_file(src, dest)

            elif is_video_file(name):
                dest = f'{SOURCE}/Videos/{name}'
                move_file(src, dest)

            elif is_text_file(name):
                dest = f'{SOURCE}/Text/{name}'
                move_file(src, dest)

            elif is_zipped_file(name):
                dest = f'{SOURCE}/Zips/{name}'
                move_file(src, dest)

            elif is_executable_file(name):
                dest = f'{SOURCE}/Installers/{name}'
                move_file(src, dest)


if __name__ == "__main__":
    organize_downloads_folder()
