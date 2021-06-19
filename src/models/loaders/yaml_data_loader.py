import i_data_loader
import typing
import yaml

class YamlDataLoader(i_data_loader.IDataLoader):

    def load_data(self) -> typing.Dict:
        with open("data/GloryToRomeCards.yaml") as card_file:
            return yaml.safe_load(card_file)