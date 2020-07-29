from . import dissoc, select_keys, get_in


def test_dissoc():
    assert(dissoc({}) == {})
    assert(dissoc({'foo': 42}) == {'foo': 42})

    assert(dissoc({}, 'foo') == {})
    assert(dissoc({'foo': 42}, 'foo') == {})
    assert(dissoc({'foo': 42}, 'foo', 'foo') == {})
    assert(dissoc({'foo': 42, 'bar': 23}, 'foo') == {'bar': 23})


def test_select_keys():
    assert(select_keys({}) == {})
    assert(select_keys({'foo': 42}) == {})

    assert(select_keys({}, 'foo') == {})
    assert(select_keys({'bar': 42}, 'foo') == {})
    assert(select_keys({'bar': 42, 'foo': 23}, 'foo') == {'foo': 23})
    assert(select_keys({'bar': 42, 'foo': 23}, 'foo', 'foo') == {'foo': 23})


def test_get_in():
    assert(get_in({}, []) == {})
    assert(get_in({}, [], 1) == {})
    assert(get_in({}, ['foo', 'bar']) is None)
    assert(get_in({}, ['foo', 'bar'], 1) == 1)

    assert(get_in(0, []) == 0)
    assert(get_in(1, []) == 1)
    assert(get_in(0, ['foo']) is None)
    assert(get_in(1, ['foo']) is None)
    assert(get_in(0, ['foo'], 10) == 10)
    assert(get_in(1, ['foo'], 11) == 11)

    assert(get_in({'foo': 42}, ['foo']) == 42)

    assert(get_in({'foo': 42}, ['foo', 'bar']) is None)
    assert(get_in({'foo': 42}, ['foo', 'bar'], 23) == 23)

    assert(get_in({'foo': {}}, ['foo']) == {})
