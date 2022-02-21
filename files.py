import logging
import shutil
import os.path


def check_and_make_dir(path, dirname):
    # takes path and directory name and if does not exist, will create one

    if not os.path.isdir(f"{path}{dirname}"):
        new_path = os.path.join(path, dirname)
        os.mkdir(new_path)


def error_move_log(path, filename, message, e=""):
    # try except that checks for Error folder and moves files and logs error.
    try:
        check_and_make_dir(path, "Error")  # TEMP COMMENT
        shutil.move(f"{path}{filename}", f"{path}Error/")  # TEMP COMMENT
        logging.error(f"{message} {e}")
    except OSError as e:
        logging.error(e)


def search_list(path, files):
    # checks textfile to see if file already processed

    unprocessed = []

    if os.path.isfile(f"{path}file.txt"):
        with open(f"{path}file.txt", "r") as f:
            content = f.read().split("\n")
        for file in files:
            if file in content:
                error_move_log(path, file, "File has already been processed.")
            else:
                unprocessed.append(file)
        return unprocessed
    else:
        return files


def write_list(path, file):
    # takes path and files and adds filenames that have been successfully processed to textfile

    with open(f"{path}file.txt", "a+") as f:
        f.write(f"{file}\n")
