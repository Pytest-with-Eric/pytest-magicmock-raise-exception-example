import pytest
from src.file_handler import (
    create_temp_directory,
    add_file,
    remove_file,
    remove_directory,
)


def test_create_temp_directory(mocker):
    """
    Test that a temporary directory is created.
    """
    # Arrange
    mocker.patch("tempfile.mkdtemp", return_value="/tmp/test")
    # Act
    directory = create_temp_directory()
    # Assert
    assert directory == "/tmp/test"


def test_add_file(mocker):
    """
    Test that a file is added to a directory.
    """
    # Arrange
    mocker.patch("builtins.open")
    # Act
    filepath = add_file("/tmp", "test.txt", "test")
    # Assert
    assert filepath == "/tmp/test.txt"


def test_remove_file_success(mocker):
    """
    Test that a file is removed successfully.
    """
    # Arrange
    mocker.patch("os.remove", return_value=True)
    # Act
    result = remove_file("/tmp/test.txt")
    # Assert
    assert result is True


def test_remove_file_file_not_found_exception(mocker):
    """
    Test that a FileNotFoundError is raised when attempting to remove a file that does not exist.
    """
    # Arrange
    mocker.patch("os.remove", side_effect=FileNotFoundError)

    # Assert
    with pytest.raises(FileNotFoundError):
        remove_file("/tmp/test.txt")


def test_remove_file_file_not_found_exception_no_mocking():
    """
    Test that a FileNotFoundError is raised when attempting to remove a file that does not exist. No mocking.
    """
    # Assert
    with pytest.raises(FileNotFoundError):
        remove_file("/tmp/test.txt")


def test_remove_directory_success(mocker):
    """
    Test that a directory is removed successfully.
    """
    # Arrange
    mocker.patch("shutil.rmtree", return_value=True)
    # Act
    result = remove_directory("/tmp/test")
    # Assert
    assert result is True


def test_remove_directory_directory_not_found_exception(mocker):
    """
    Test that a FileNotFoundError is raised when attempting to remove a directory that does not exist.
    """
    # Arrange
    mocker.patch("shutil.rmtree", side_effect=FileNotFoundError)

    # Assert
    with pytest.raises(FileNotFoundError):
        remove_directory("/tmp/test")
