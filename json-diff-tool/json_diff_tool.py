def getJSONDiff(json1, json2):
    res = []
    hashmap = {}
    key = ''
    val = ''
    switch = False
    print(json1)
    for char in json1:
        if char == ',':
            hashmap[key] = val
            key = ''
            val = ''
            switch = False
        elif char.isalpha() and not switch:
            key += char
        elif char.isalpha() and switch:
            val += char
        elif char == ':':
            switch = True
        elif char == '"':
            continue

    hashmap[key] = val

    key2 = ''
    val2 = ''
    switch2 = False
    for char in json2:
        if char == ',':
            if hashmap[key2] != val2:
                res.append(key2)
            key2 = ''
            val2 = ''
            switch2 = False
        elif char.isalpha() and not switch2:
            key2 += char
        elif char.isalpha() and switch2:
            val2 += char
        elif char == ':':
            switch2 = True

    if hashmap[key2] != val2:
        res.append(key2)

    res.sort()
    return res
