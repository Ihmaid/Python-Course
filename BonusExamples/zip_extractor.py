import zipfile
import pathlib


def extract_archive(filepath, destination_dir):
    destination_path = pathlib.Path(destination_dir, "extract")
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(destination_path)


if __name__ == "__main__":
    extract_archive(filepath="compressed.zip", destination_dir="dest")