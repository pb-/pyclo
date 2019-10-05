from . import dissoc, select_keys


def test_dissoc():
    assert(dissoc({}, 'foo') == {})
    assert(dissoc({'foo': 42}, 'foo') == {})
    assert(dissoc({'foo': 42}, 'foo', 'foo') == {})
    assert(dissoc({'foo': 42, 'bar': 23}, 'foo') == {'bar': 23})


def test_select_keys():
    assert(select_keys({}, 'foo') == {})
    assert(select_keys({'bar': 42}, 'foo') == {})
    assert(select_keys({'bar': 42, 'foo': 23}, 'foo') == {'foo': 23})
    assert(select_keys({'bar': 42, 'foo': 23}, 'foo', 'foo') == {'foo': 23})
