import re
from re import search


def main():
    valid_strings = set()
    # removal_set = set()
    # invalid_strings = ["ab", "cd", "pq", "xy"]

    with open("input.txt") as f:
        for word in f:
            word = word.strip()
            # pattern = re.compile(r'[aeiou]')
            # found = pattern.findall(word)
            # if (len(found) >= 3):
            valid_strings.add(word)

    # for word in valid_strings:
    #     for invalid in invalid_strings:
    #         if invalid in word:
    #             removal_set.add(word)

    # for word in valid_strings:
    #     last_char = ''
    #     word_valid = False
    #     for letter in word:
    #         if (letter == last_char):
    #             word_valid = True
    #         last_char = letter
    #     if not word_valid:
    #         removal_set.add(word)

    # print(len(valid_strings.difference(removal_set)))

    print("Part 2:")
    print(len([x for x in valid_strings if search("(\w\w).*\\1", x) and search("(\w).\\1", x)]))

if __name__ == '__main__':
    main()
