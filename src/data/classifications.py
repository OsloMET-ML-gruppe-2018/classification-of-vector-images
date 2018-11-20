from pathlib import Path
import math
import csv
from pprint import pprint as pp
import json

def classification_overlap(class_label:str):
    path_str = "../../data/raw/categories/categories/{}.txt".format(class_label)
    path = Path(path_str)
    if not path.exists():
        raise FileExistsError("File does not exist")

    with open(path.absolute()) as f:
        read_data = f.read()
        class_label_list = string_to_list(read_data)

    result_data_dict = {"label": class_label, "label_image_count": len(class_label_list), "result": []}
    lablel_dict = gen_dict_of_label_lists(class_label)
    unique_ids = set(class_label_list)
    class_label_id_in_other_lists = set()

    for label_list in lablel_dict:
        unique_ids = unique_ids.union(lablel_dict.get(label_list))
        count = 0
        for id in class_label_list:
            if id in lablel_dict.get(label_list):
                class_label_id_in_other_lists.add(id)
                count += 1
        result_data_dict["result"].append({"label": label_list, "image_count": len(lablel_dict.get(label_list)),
                                           "overlap": count, "overlap_percent": (count / len(class_label_list)) * 100})
        result_data_dict["total_image_overlap"] = len(class_label_id_in_other_lists)
    return result_data_dict


def gen_dict_of_label_lists(not_include_label:str) -> dict:
    path_str = "../../data/raw/categories/categories/"
    path = Path(path_str)
    dict_of_label_lists = {}

    for file in path.iterdir():
        label_name = remove_file_ending(file.name)
        if label_name != not_include_label:
            with open(file.absolute()) as f:
                read_data = f.read()
                dict_of_label_lists[label_name] = string_to_list(read_data)
    return dict_of_label_lists


def string_to_list(string:str) -> iter:
    return set(string.split("\n"))


def remove_file_ending(filename:str):
    return filename.split(".")[0]


def write_to_csv(class_label_list, label_dict, perc_dict):
    file_path = Path("../../data/processed/overlap.csv")
    with file_path.open("w+") as file:
        csv_writer = csv.DictWriter(file, ["label", "label_image_count", "compared_label",
                                           "image_overlap_amount", "overlap_percent"])


def main():
    labels = gen_dict_of_label_lists("")

    result = []
    count = 1
    for el in labels:
        print("\n")
        result.append(classification_overlap(el))
        count += 1
    pp(result)
    json_object = json.dumps(result)
    json_file_path = Path("../../data/processed/dataset_analytics/dataset_report.json")

    with json_file_path.open("w+") as writer:
        writer.write(json_object)


if __name__ == '__main__':
    main()
