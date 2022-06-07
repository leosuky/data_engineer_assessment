import json
import unittest
from main import main


f = open('test.json')
file = json.load(f)

class TestJsonData(unittest.TestCase):


    def test_result(self):
        result = main(file)
        self.assertTrue(isinstance(result, dict))

    def test_string_type(self):
        result = main(file)
        self.assertEqual(result["nationality"]["type"], "string")

    def test_integer_type(self):
        result = main(file)
        self.assertEqual(result["age"]["type"], "integer")

    def test_enum_type(self):
        result = main(file)
        self.assertEqual(result["favouriteFood"]["type"], "enum")

    def test_array_type(self):
        result = main(file)
        self.assertEqual(result["status"]["type"], "array")

    def test_nested_object(self):
        result = main(file)
        self.assertTrue(isinstance(result["name"], dict))

    def test_padded_values(self):
        result = main(file)
        self.assertIsNotNone(result["status"]["tag"])
        self.assertIsNotNone(result["status"]["description"])
        self.assertFalse(result["status"]["required"])



if __name__ == '__main__':
    unittest.main()