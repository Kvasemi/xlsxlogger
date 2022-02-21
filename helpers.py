import logging
import re
import files
import constants


def conv_cell_date(string):
    # converts cell date into tuple in (mm, yy) format for comparison

    try:
        date_tpl = tuple(string.strftime("%-m/%-y").split("/"))
    except:
        logging.exception("Converting cell to tuple failed.")
    else:
        return date_tpl


def conv_file_date(string, path):
    # converts filename into tuple in (mm, yy) format for comparison

    try:
        date_list = re.split("[_.]", string)[-3:-1]
        date_tpl = tuple([constants.MONTHS[date_list[0]], date_list[1][2:]])
        result = (date_list[0], date_tpl)
    except KeyError as e:
        files.error_move_log(path, string, "There was an error in the filename.", e)
    else:
        return result


def filter_files(files):
    # filter files in folder that meets criteria

    filtered_files = tuple(
        filter(
            lambda file: not file.startswith((".", "~")) and file.endswith("xlsx"),
            files,
        )
    )
    try:
        filtered_files[0]
    except:
        logging.error("No excel files were found that meet the criteria.")

    return filtered_files


def score_calculator(label, data):
    if label.startswith("Promoters"):
        if data > 200:
            return "good"
        elif data < 200:
            return "bad"
    elif label.startswith("Passives"):
        if data > 100:
            return "good"
        elif data < 100:
            return "bad"
    elif label.startswith("Dectrators"):
        if data > 100:
            return "good"
        elif data < 100:
            return "bad"
    else:
        return None
