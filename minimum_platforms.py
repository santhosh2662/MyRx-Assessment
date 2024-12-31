def find_minimum_platforms(arr, dep):
    arr = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in arr]
    dep = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in dep]


    arr.sort()
    dep.sort()

    platform_needed = 1
    max_platforms = 1
    i, j = 1, 0

    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:  
            platform_needed += 1
            i += 1
        else:  
            platform_needed -= 1
            j += 1

        max_platforms = max(max_platforms, platform_needed)

    return max_platforms

arrival = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(find_minimum_platforms(arrival, departure))  

arrival = ["9:00", "9:40"]
departure = ["9:10", "12:00"]
print(find_minimum_platforms(arrival, departure))  
