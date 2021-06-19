import unittest
import yaml_data_loader

class TestYamlDataLoader(unittest.TestCase):

    def test_load(self):
        yaml_loader = yaml_data_loader.YamlDataLoader()
        config = yaml_loader.load_data()
        for item in config["Roles"]:
            print(item)

if __name__ == "__main__":
    unittest.main()

