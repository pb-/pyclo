def dissoc(dict_, *keys):
    return {k: v for k, v in dict_.items() if k not in keys}


def select_keys(dict_, *keys):
    return {k: dict_[k] for k in keys if k in dict_}
