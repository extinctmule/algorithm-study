def solution(new_id: str):
    new_id = new_id.lower()

    # idlist = list(id)
    for c in enumerate(new_id):
        if c in "~!@#$%^&*()=+[{]}:?,<>/":
            new_id = new_id.replace(c, "")
    new_id.
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    if not new_id or new_id == ".":
        new_id = "a"
    else:
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

        if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id[-1] == ".":
                new_id = new_id[:-1]

    tmp = len(new_id)
    if tmp <= 2:
        new_id += new_id[-1] * (3 - tmp)

    return new_id
    # "".join(map(str,id))


print(solution("z-+.^."))
