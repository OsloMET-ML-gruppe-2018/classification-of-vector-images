import unittest
from ..create_cleaned_categories import CleanCategoriesCreator
from pathlib import Path
from pprint import pprint as pp

class TestCleanCategoriesCreator(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_initialization__normal_case(self):
        testObj = CleanCategoriesCreator(Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/Categories/categories"))
        testObj.remove_classification_data_overlap()
        pp(testObj.get_difference_between_clean_and_unclean_category_data())

    def test_equality(self):
        testObj = CleanCategoriesCreator(Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/Categories/categories"))
        testObj.remove_classification_data_overlap()
        testObj.print_if_categories_are__equal()

    def test_create(self):
        testObj = CleanCategoriesCreator(Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/Categories/categories"),
                                         Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/data_png/data_png_128"))
        testObj.create(Path("/home/sondre/PycharmProjects/classification-of-vector-images"))

    def test_split_dataset(self):
        testObj = CleanCategoriesCreator(
            Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/Categories/categories"),
            Path("/home/sondre/PycharmProjects/classification-of-vector-images/data/raw/data_png/data_png_128"))
        train, test = testObj.split_datasett(testObj._categories["car"])
        print(len(train))
        print(len(test))
