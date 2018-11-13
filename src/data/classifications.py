from pathlib import Path
import math
import csv


def classification_overlap(class_label:str):
    path_str = "../../data/raw/categories/categories/{}.txt".format(class_label)
    path = Path(path_str)
    if not path.exists():
        raise FileExistsError("File does not exist")

    with open(path.absolute()) as f:
        read_data = f.read()
        class_label_list = string_to_list(read_data)

    lablel_dict = gen_dict_of_label_lists(class_label)
    perc_dict = dict.fromkeys(lablel_dict.keys(), 0)
    unique_ids = set(class_label_list)

    for label_list in lablel_dict:
        unique_ids = unique_ids.union(lablel_dict.get(label_list))
        count = 0
        for id in class_label_list:
            if id in lablel_dict.get(label_list):
                count += 1
        perc_dict[label_list] = (count / len(lablel_dict.get(label_list))) * 100
    print("For label: " + class_label + " - size: " + str(len(class_label_list)))
    for label in perc_dict:
        print(str(label) + " % overlap : " + str(perc_dict.get(str(label))) + "<br>")
    print("\nSum of unique images in categories: " + str(len(unique_ids)))



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
    for el in labels:
        print("\n")
        classification_overlap(el)

if __name__ == '__main__':
    main()