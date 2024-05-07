import os
import shutil
import tempfile


def create_temp_directory():
    """
    Creates and returns the path to a temporary directory.
    """
    return tempfile.mkdtemp()


def add_file(directory, filename, content):
    """
    Adds a file with the specified filename and content to the provided directory.
    Args:
    - directory (str): The path to the directory.
    - filename (str): The name of the file to be created.
    - content (str): The content to be written to the file.

    Returns:
    - str: The path to the created file.
    """
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as f:
        f.write(content)
    return file_path


def remove_file(filepath):
    """
    Removes the specified file.
    Args:
    - filepath (str): The path to the file to be removed.

    Returns:
    - bool: True if the file was removed successfully, False otherwise.
    """
    try:
        os.remove(filepath)
        return True
    except FileNotFoundError as e:
        raise e


def remove_directory(directory):
    """
    Removes the specified directory and all its contents.
    Args:
    - directory (str): The path to the directory to be removed.

    Returns:
    - bool: True if the directory was removed successfully, False otherwise.
    """
    try:
        shutil.rmtree(directory)
        return True
    except FileNotFoundError as e:
        raise e
