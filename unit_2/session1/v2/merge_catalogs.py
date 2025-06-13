def merge_catalogs(catalog1, catalog2):
    new_catalog = {}
    for key in catalog1:
        if key in catalog2:
            del catalog2[key]

    for key in catalog1:
        new_catalog[key] = catalog1[key]

    for key in catalog2:
        new_catalog[key] = catalog2[key]

    return new_catalog

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}

print(merge_catalogs(catalog1,  catalog2))