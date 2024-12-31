def sort_hashmap_by_value(map_data):
    return {k: v for k, v in sorted(map_data.items(), key=lambda item: item[1])}

hashmap = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
print(sort_hashmap_by_value(hashmap))
