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


def sort_on(stats):
    return stats['num']


def get_char_stats_sorted(chars_stats):
    report = []
    for char in chars_stats:
        if char.isalpha():
            report.append({"char": char, "num": chars_stats[char]})
    report.sort(reverse=True, key=sort_on)
    return report
