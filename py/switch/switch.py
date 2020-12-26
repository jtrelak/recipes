import pdb

def get_bools(s):
    bools_map = {
        "False-False": [("cold-start", "False"), ("keep-alive", "False")],
        "False-True": [("cold-start", "False"), ("keep-alive", "True")],
        "True-False": [("cold-start", "True"), ("keep-alive", "False")],
        "True-True": [("cold-start", "True"), ("keep-alive", "True")]
    }

    for i in bools_map.keys():
        if i in s:
            return bools_map.get(i, [])
    return []

pdb.set_trace()
