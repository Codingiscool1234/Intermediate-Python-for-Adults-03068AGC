def avg_age(contact_dict):
    total = 0
    count = 0
    if len(contact_dict.values()) != 0:
        for val in contact_dict.values():
            total += int(val["age"])
            count += 1
    else:
        return 0
    avg = total / count
    return avg

