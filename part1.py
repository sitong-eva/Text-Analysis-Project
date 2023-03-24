def process_file(filename):
    hist = {}
    fp = open(filename, encoding="UTF8")

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    for line in fp:
        for word in line.split():
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1

    return hist


def main():
    hist = process_file("drake_lyrics.txt")
    drake = process_file("drake_lyrics.txt")
    beatles = process_file("beatles.txt")


if __name__ == "__main__":
    main()
