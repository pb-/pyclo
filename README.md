# pyclo

Pyclo is a collection of functions for Python named after the Clojure standard library to perform the equivalent operation of the respective Clojure function.

Install with
```
pip install pyclo
```


## Rationale

While immutability is neither idiomatic nor common in Python, it is still beneficial to implement the concept through engineering discipline. However, soon one will find oneself writing the same constructs over and over again, and even though these expressions are fairly succinct, it is much nicer to refer to them by name. The goal of this library is to provide a collection of functions that promote immutable manipulation of standard Python data structures as a concept without strictly enforcing it.

They say that there are only two hard problems in software engineering, one of them being naming. Clojure is chosen as a source of inspiration for these functions because the author of this library considers Clojure's naming the gold standard.


## Reference

```
from pyclo import *
```

 - `dissoc(dict, *keys)` - return a copy of `dict` without specified `keys`.
 - `select_keys(dict, *keys)` - return a copy of `dict` only containing `keys`.
 - `get_in(dict, keys, default=None)` - look up a sequence of keys in a nested dict.


## Development

```
make test
make lint
make upload  # upload to Pypi
```
