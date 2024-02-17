def merge_dicts(dicts, reverse_priority=False):
    res = {}
    if reverse_priority:
        dicts = dicts[::-1]

    for d in dicts:
        res.update(d)

    return res