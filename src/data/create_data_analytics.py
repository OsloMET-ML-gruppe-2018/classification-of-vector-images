from pathlib import Path
from pprint import pprint as pp
import csv
import json

def get_mtruk_categories():
    path = Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/categories/cats_mturk")
    categories ={}
    for label_file in path.iterdir():
        with label_file.open("r") as reader:
            images = ""
            lines = reader.readlines()
            for line in lines:
                if line[0] != "#":
                    images += line
            categories[label_file.name.split(".")[0]] = images.split()
    return categories

def get_public_categories():
    path = Path("../../data/raw/categories/categories/")
    categories ={}
    for label_file in path.iterdir():
        with label_file.open("r") as reader:
            images = ""
            lines = reader.readlines()
            for line in lines:
                if line[0] != "#":
                    images += line
            categories[label_file.name.split(".")[0]] = images.split()
    return categories

def get_category_sizes(cat_dict):
    result = []
    for label, images in cat_dict.items():
        result.append({"category": label, "image_count": len(images)})
    return result


def calc_category_overlap(category_image_dict):
    category_image_dict = setify(category_image_dict)

    result_list = []
    for label, images in category_image_dict.items():
        images_in_other_categories = set()
        result_data_dict = {"label": label, "label_image_count": len(images), "result": []}
        for comp_label, comp_images in category_image_dict.items():
            if label == comp_label:
                continue

            overlap_count = 0

            for image in images:
                if image in comp_images:
                    overlap_count += 1
                    images_in_other_categories.add(image)
            result_data_dict["result"].append({"label": comp_label, "image_count": len(comp_images),
                                           "overlap": overlap_count,
                                           "overlap_percent": (overlap_count / len(images)) * 100})
        result_data_dict["total_image_overlap"] = len(images_in_other_categories)
        result_list.append(result_data_dict)

    return result_list


def setify(category_image_dict):
    for label, images in category_image_dict.items():
        category_image_dict[label] = set(images)
    return category_image_dict


def get_category_sizes():
    mturk_cat = get_mtruk_categories()
    public_cat = get_public_categories()

    mturk_images = set()
    for cat, images in mturk_cat.items():
        for image in images:
            mturk_images.add(image)

    public_images = set()
    for cat, images in public_cat.items():
        for image in images:
            public_images.add(image)

    print("mkat count: " + str(len(mturk_images)))
    print("public count: " + str(len(public_images)))


def create_mturk_dataset():
    store_file_path = Path("../../data//processed/dataset_analytics/mturk_data.json")
    result =get_mtruk_categories()
    sizes = get_category_sizes(result)
    data = calc_category_overlap(result)
    data = json.dumps(data)
    with store_file_path.open("w+") as writer:
        writer.write(data)

def get_clean_dataset_size():
    dataset_path = Path("../../data/processed/cleaned_categories")
    test_dir = dataset_path.joinpath("test")
    train_dir = dataset_path.joinpath("train")


    image_count = 0
    for dir in test_dir.iterdir():
        for pfile in dir.iterdir():
            if pfile.is_file():
                image_count += 1
    for dir in train_dir.iterdir():
        for pfile in dir.iterdir():
            if pfile.is_file():
                image_count += 1
    return image_count

def get_clean_subcat_size():
    dataset_path = Path("../../data/processed/cleaned_categories")
    test_dir = dataset_path.joinpath("test")
    train_dir = dataset_path.joinpath("train")
    categories = {}


    for dir in test_dir.iterdir():
        image_count = 0
        for pfile in dir.iterdir():
            if pfile.is_file():
                image_count += 1
        categories[dir.name] = image_count
    for dir in train_dir.iterdir():
        image_count = 0
        for pfile in dir.iterdir():
            if pfile.is_file():
                image_count += 1
        categories[dir.name] += image_count
    return categories

if __name__ == "__main__":
    #get_category_sizes()
    print("clean_image caount: " + str(get_clean_dataset_size()))
    pp(get_clean_subcat_size())
    check_count = 0
    for label, value in get_clean_subcat_size().items():
        check_count += value
    print("clean image count: " + str(check_count))
