import os


def remove_files_except(folder_path, keep_files):
    """
    Removes all files in the specified folder except for those whose filenames are provided in the keep_files array.

    Parameters:
    folder_path (str): The path to the folder where the files are located.
    keep_files (list of str): A list of filenames that should not be deleted.

    Example:
    ----------
    folder_path = "C:/Users/YourUsername/Documents/TargetFolder"
    keep_files = ["important_doc.txt", "keep_this_image.png"]

    remove_files_except(folder_path, keep_files)
    # This will remove all files in the TargetFolder except 'important_doc.txt' and 'keep_this_image.png'.
    """

    # Get the absolute paths of files to keep
    keep_files_full = [os.path.join(folder_path, f) for f in keep_files]

    # List all files in the specified folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is not in the keep_files list and is a file (not a directory)
        if os.path.isfile(file_path) and file_path not in keep_files_full:
            os.remove(file_path)
            print(f"Removed: {file_path}")
        else:
            print(f"Kept: {file_path}")


# Example usage

# Example Usage
# -------------
# Define the folder path where the files are located.
# Replace 'path/to/your/folder' with the actual path to your folder.
folder = "USE_YOUR_FILE_PATH"

# Define the list of filenames you want to keep.
# These files will not be removed from the folder.
keep_files = [
    "CKM09087.JPG",
    "CKM09067.JPG",
    "CKM09061.JPG",
    "CKM09018.JPG",
    "CKM09014.JPG",
    "CKM08989.JPG",
    "CKM08984.JPG",
    "CKM08972.JPG",
    "CKM08955.JPG",
    "CKM08939.JPG",
    "CKM08880.JPG",
    "CKM08871.JPG",
    "CKM08827.JPG",
    "CKM08800.JPG",
    "CKM08775.JPG",
    "CKM08776.JPG",
    "CKM08752.JPG",
    "CKM08689.JPG",
    "CKM08672.JPG",
    "CKM08668.JPG",
    "CKM08660.JPG",
    "CKM08659.JPG",
    "CKM08635.JPG",
    "CKM08622.JPG",
    "CKM08583.JPG",
    "CKM08556.JPG",
    "CKM08544.JPG",
    "CKM08543.JPG",
    "CKM08542.JPG",
    "CKM08516.JPG",
]

# Call the function to remove all files in the specified folder except those listed in 'files_to_keep'.
remove_files_except(folder, keep_files)
