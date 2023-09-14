def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = {}

            for word in words:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1

        return word_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python wordcount.py")
        sys.exit(1)

    filename = sys.argv[1]
    word_count = count_words(filename)

    for word, count in word_count.items():
        print(f"{word}: {count}")
