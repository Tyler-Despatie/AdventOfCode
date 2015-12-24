import re


def main():
    raw_count = 0
    encoded_count = 0

    with open("input.txt") as f:
        for line in f:
            raw = line.strip()
            encoded = re.sub(r'(["\\])', r'\\\1', raw)

            raw_count += len(raw)
            encoded_count += len(encoded) + 2 # Quotes are not included

        print(encoded_count - raw_count)

if __name__ == '__main__':
    main()
