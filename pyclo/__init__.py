def dissoc(dict_, *keys):
    return {k: v for k, v in dict_.items() if k not in keys}


def select_keys(dict_, *keys):
    return {k: dict_[k] for k in keys if k in dict_}


def get_in(dict_, keys, default=None):
    if not keys:
        return dict_

    if not isinstance(dict_, dict):
        return default

    if len(keys) == 1:
        return dict_.get(keys[0], default)

    return get_in(dict_.get(keys[0], {}), keys[1:], default)
