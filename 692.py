def top_k_fre(string, k):
    hash_map = {}
    for word in string.split():
        hash_map[word] = hash_map.get(word, 0) + 1

    result = []
    for word in sorted(hash_map):
        if hash_map[word] == k:
            result.append(word)
    return result

print(top_k_fre("jango is powerful and jango is fast", 2))
# ['is', 'jango']