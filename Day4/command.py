import wordcount

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python command.py")
        sys.exit(1)

    filename = sys.argv[1]
    word_count = wordcount.count_words(filename)

    for word, count in word_count.items():
        print(f"{word}: {count}")
