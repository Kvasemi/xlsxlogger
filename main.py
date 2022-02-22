import logging
from os import listdir
import os.path
import files
import helpers
import data
import constants


logging.basicConfig(
    level=logging.DEBUG,
    filename="%slog" % __file__[:-2],
    format="%(asctime)s[%(levelname)s  ]: %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S",
    filemode="w",
)


def main(path):
    # takes path and topmost level prog from start to end
    logging.info(f"eval_week2.py started. Searching directory {path}...")

    try:
        next(os.walk(path))
    except StopIteration:
        logging.error("Path provided is invalid.")

    try:
        onlyfiles = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
        filtered_files = helpers.filter_files(onlyfiles)
        remaining_files = files.search_list(constants.PATH, filtered_files)
        if len(remaining_files) != 0:
            for file in remaining_files:
                log_result = data.manage_data(path, file)
                if log_result is not None and len(log_result) != 0:
                    files.write_list(constants.PATH, file)
    except FileNotFoundError as e:
        logging.error(e)


if __name__ == "__main__":
    main(constants.PATH)
