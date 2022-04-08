import json
from dacite import from_dict
from harpar import HarPar

with open("tests/fixtures/results.json") as fp:
    data = json.load(fp)
    hp = from_dict(data_class=HarPar, data=data)

def test_version():
    assert hp.log.version == "1.2"

def test_creator():
    assert hp.log.creator.name == "chrome-har"
    assert hp.log.creator.version == "0.11.12"
    assert hp.log.creator.comment == "https://github.com/sitespeedio/chrome-har"

def test_pages():
    assert hp.log.pages[0].id == "page_1"
    assert hp.log.pages[0].startedDateTime.year == 2022 # NOTE: this is a real datetime object
    assert hp.log.pages[0].title == "https://cnn.com/"

def test_entries():
    assert hp.log.entries[0].startedDateTime.year == 2022
    assert hp.log.entries[0]._requestId == "5BAFD95809A0E99C76F54E57048BF95Fr"
    # TODO: write more asserts to prove the entries are working properly...