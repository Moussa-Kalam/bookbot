def count_words(text):
    return len(text.split())

def count_chars(text):
    chars_stats = {}
    for character in text:
        char = character.lower()
        if char in chars_stats:
            chars_stats[char] += 1
        else:
            chars_stats[char] = 1
    return chars_stats
