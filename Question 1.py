def min_subsequences(source, target):
    source_len = len(source)
    target_len = len(target)

    # This dictionary maps characters to their indices in the source string
    char_index_map = {}
    for i, char in enumerate(source):
        if char not in char_index_map:
            char_index_map[char] = []
        char_index_map[char].append(i)

    # Initializing the count of subsequences
    count = 0
    i = 0

    while i < target_len:
        count += 1
        pos = 0  # Position in source

        while i < target_len:
            if target[i] not in char_index_map:
                return -1  # Character not found in source

            # Binary search to find the smallest index in source which is >= pos
            j = binary_search(char_index_map[target[i]], pos)
            if j == len(char_index_map[target[i]]):
                break  # No valid position found, need a new subsequence
            pos = char_index_map[target[i]][j] + 1
            i += 1

    return count


def binary_search(lst, x):
    """Binary search to find the smallest index which is >= x"""
    lo, hi = 0, len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    source = input("Enter the source string: ")
    target = input("Enter the target string: ")
    result = min_subsequences(source, target)
    print(result)
