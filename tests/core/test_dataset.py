from hover.core.dataset import SupervisableTextDataset
import pytest


@pytest.mark.core
class TestSupervisableTextDataset:
    TEST_DICTL = [
        {"content": "Aristotle", "mark": "A"},
        {"content": "Bertrand Russell", "mark": "B"},
        {"content": "CRISPR", "mark": "C"},
        {"content": "Doudna", "mark": "D"},
    ]
    DEV_DICTL = [
        {"content": "Doudna", "mark": "D"},
        {"content": "Ernest Hemingway", "mark": "E"},
    ]
    TRAIN_DICTL = [
        {"content": "Ernest Hemingway", "mark": "e"},
        {"content": "Franklin Roosevelt", "mark": "F"},
        {"content": "Geralt of Rivia", "mark": "G"},
    ]
    RAW_DICTL = [{"content": "Geralt of Rivia"}, {"content": "Hailstorm"}]

    EFFECTIVE_SIZE = {"test": 4, "dev": 1, "train": 2, "raw": 1}

    EFFECTIVE_CLASSES = 7

    def test_init(self):
        dataset = SupervisableTextDataset(
            self.__class__.RAW_DICTL[:],
            train_dictl=self.__class__.TRAIN_DICTL[:],
            dev_dictl=self.__class__.DEV_DICTL[:],
            test_dictl=self.__class__.TEST_DICTL[:],
            feature_key="content",
            label_key="mark",
        )

        # check the subset sizes
        for _key, _value in self.__class__.EFFECTIVE_SIZE.items():
            assert dataset.dfs[_key].shape[0] == _value

        # check the number of classes
        assert len(dataset.classes) == self.__class__.EFFECTIVE_CLASSES
