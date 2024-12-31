def sort_rgb(arr):
    return sorted(arr, key=lambda x: {"B": 0, "G": 1, "R": 2}[x])

balls = ["R", "G", "B", "G", "G", "R", "B", "B", "G"]
print(sort_rgb(balls))
