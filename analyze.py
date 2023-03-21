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


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    stopwords = process_file("stopwords.txt")
    res = []
    for word in hist:
        if excluding_stopwords:
            if word in stopwords:
                continue
        freq = hist[word]
        res.append((freq, word))
    res.sort(reverse=True)
    return res


def drakevbeatles(d1, d2):
    unique = 0
    total = 0
    for key in d1:
        total += 1
        if key not in d2:
            unique += 1
    res = unique / total * 100
    return f"{res:.2f}%"


def main():
    hist = process_file("drake_lyrics.txt")
    # print(hist)
    # print(total_words(hist))
    # print(most_common(hist,excluding_stopwords=True))
    drake=process_file("drake_lyrics.txt")
    beatles=process_file("beatles.txt")
    print(drakevbeatles(drake,beatles))

if __name__ == "__main__":
    main()
