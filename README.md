# HarPar | A Pythonic Har File Parser written Python3


## Install
```
pip install harpar
```

## Example Usage

```py
from harpar import harpar_factory
import json

# NOTE: this assumes results.json is a valid HAR file
with open("results.json") as fp:
    data = json.load(fp)
    hp = harpar_factory(data)

for entry in hp.log.entries:
    print(entry.request.method)
```
