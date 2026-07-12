def special(s):
    low = []
    upp = []
    count = 0

    for ch in s:
        if ch.isupper() and ch not in upp:
            upp.append(ch)
        elif ch.islower() and ch not in low:  # ✅ added islower() check
            low.append(ch)

    for ch in upp:                  # ✅ loop only uppercase
        if ch.lower() in low:       # ✅ check lowercase version exists
            count += 1

    return count

print(special("aaAAbbBcCC"))  # Output: 3