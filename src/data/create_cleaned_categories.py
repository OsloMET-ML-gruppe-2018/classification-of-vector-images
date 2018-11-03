from pathlib import Path
import shutil

class CleanCategoriesCreator:
    """ Cleans categories passed, creates new folders containing cleaned data
    """

    def __init__(self, categories_path: Path, images_path: Path):

        self.categories_path = categories_path
        self._categories = {}
        self._create_categories_data_store()
        self._cleaned_categories = {}
        self._images_path = images_path

    def create(self, path_to_create_folder: Path):
        self.remove_classification_data_overlap()

        try:
            category_folder = path_to_create_folder.joinpath("cleaned_categories/")
            category_folder.mkdir()
        except IsADirectoryError as err:
            print("Cleaned Category directory has already been created. No action is taken")
        else:
            label_folder_paths = {}
            for label in self._cleaned_categories:
                category_folder.joinpath(label).mkdir()
                label_folder_paths[label] = category_folder.joinpath(label + "/")
            for label in label_folder_paths:
                self.copy_files_into_folder(self._images_path, label_folder_paths.get(label), self._cleaned_categories.get(label))

    def _create_categories_data_store(self):
        self._categories = gen_dict_of_label_lists(self.categories_path)

    def remove_classification_data_overlap(self):

        cleaned_data_dict = {}

        for label in self._categories:
            cleaned_data_dict[label] = []
            for id in self._categories.get(label):

                id_is_clean = True # assumes every id is not duplicated until otherwise proven
                for other_label in self._categories:
                    if other_label != label:
                        if id in self._categories.get(other_label):
                            id_is_clean = False
                            break
                if id_is_clean:
                    cleaned_data_dict[label].append(id)
        self._cleaned_categories = make_dict_of_list_into_set(cleaned_data_dict)

    def get_difference_between_clean_and_unclean_category_data(self):
        diff_dict = {}

        for label in self._cleaned_categories:
            overlap = 0
            for id in self._cleaned_categories.get(label):
                if id in self._categories.get(label):
                    overlap += 1
            diff_dict[label] = (len(self._categories.get(label)) - overlap, overlap)
        return diff_dict

    def print_if_categories_are__equal(self):
        for label in self._cleaned_categories:
            print(label + "dirty and clean datasets is equal :" + str(self._cleaned_categories.get(label) == self._categories.get(label)))

    def copy_files_into_folder(self, files_location: Path, folder_location: Path, id_list):
        count_files_not_found = 0
        for id in id_list:
            file_path = files_location.joinpath(id + "_128.png")
            try:
                shutil.copyfile(str(file_path.absolute()), str(folder_location.joinpath(str(id + "_128.png")).absolute()))
            except FileNotFoundError as err:
                count_files_not_found += 1
        print("files not found: " + str(count_files_not_found))


def make_dict_of_list_into_set(dictonary: dict):
    for list in dictonary:
        dictonary[list] = set(dictonary.get(list))
    return dictonary

def gen_dict_of_label_lists(path: Path) -> dict:
    dict_of_label_lists = {}

    for file in path.iterdir():
        label_name = remove_file_ending(file.name)
        with file.open("r") as f:
            read_data = f.read()
            dict_of_label_lists[label_name] = string_to_list(read_data)
    return dict_of_label_lists


def string_to_list(string: str) -> iter:
    data =  string.split("\n")
    for value in data:
        if value == "" or " ":
            data.remove(value)
    return set(data)

def remove_file_ending(filename: str):
    return filename.split(".")[0]


def get_category_name(catergory_path: Path) -> str:
    return str(catergory_path)[-1]


if __name__ == "__main__":

    # NB change paths
    testObj = CleanCategoriesCreator(
        Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/Categories/categories"),
        Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/data_png/data_png_128"))
    testObj.create(Path("/home/sondre/PycharmProjects/classification-of-vector-images"))


