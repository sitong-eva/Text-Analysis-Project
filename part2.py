import part1
import nltk

nltk.download("vader_lexicon")
nltk.download("punkt")
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
from thefuzz import process
import numpy as npc
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import random
import re
import os
import openai

# Summarization


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def most_common10(hist, excluding_stopwords=False, num=10):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    stopwords = part1.process_file("stopwords.txt")
    res = []
    for word in hist:
        if excluding_stopwords:
            if word in stopwords:
                continue
        freq = hist[word]
        res.append((freq, word))
    res.sort(reverse=True)
    return res[0:num]


def drakevbeatles(d1, d2):
    """
    This function compares the Drake lyrics with the Beatles lyrics to see how much of the words from the Drake lyrics is unique from the Beatles lyrics.
    """
    unique = 0
    total = 0
    for key in d1:
        total += 1
        if key not in d2:
            unique += 1
    res = unique / total * 100
    return f"{res:.2f}%"


# Natural Language Processing


def sentiment(musician):
    """
    This functions tells the sentiment of the musician based on their lyrics.
    """
    analyzer = SentimentIntensityAnalyzer()
    if isinstance(musician, int):
        musician = str(musician)
    sentences = nltk.sent_tokenize(str(musician))
    scores = []
    for sentence in sentences:
        score = analyzer.polarity_scores(
            sentence
        )  # https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664
        scores.append(score["compound"])
        average = sum(scores) / len(scores)
    return average


def similar(musician1, musician2):
    """
    This function provides a similarity score between the lyrics of two musicians.
    """
    for lyrics in musician1.values():
        musician1_lyrics = "".join(str(lyrics))
    for lyrics in musician2.values():
        musician2_lyrics = "".join(str(lyrics))
    ratio = fuzz.ratio((musician1_lyrics.lower()), musician2_lyrics.lower())
    return f"Similarity score: {ratio}"


def sentence_generator(musician):
    """
    This function generates a sentence from the artist using a Markov chain.
    """

    words = list(musician.keys())

    # https://healeycodes.com/generating-text-with-markov-chains
    markov_chain = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in markov_chain:
            markov_chain[current_word].append(next_word)
        else:
            markov_chain[current_word] = [next_word]

    current_word = random.choice(words)

    sentence = current_word.capitalize()
    while len(sentence) < 100:
        if current_word in markov_chain:
            next_word = random.choice(markov_chain[current_word])
            sentence += " " + next_word
            current_word = next_word
        else:
            break
    sentence += "."
    return sentence


def sentence_generator2(musician):
    """
    This function generates a sentence from the artist, using OpenAPI.
    """
    openai.api_key = "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"

    model_engine = "davinci"
    temperature = 0.5
    max_tokens = 50
    stop_sequence = "."

    prompt = f"Act as if you are {musician}, and you're writing a song. What's a line from your song?:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    sentence = response.choices[0].text.strip()
    return sentence


def main():
    drake_lyrics = part1.process_file("drake_lyrics.txt")
    beatles_lyrics = part1.process_file("beatles.txt")

    # print(drake_lyrics)
    # print(total_words(drake_lyrics))
    # print(most_common10(drake_lyrics,excluding_stopwords=True))
    # print(drakevbeatles(drake_lyrics,beatles_lyrics))

    # print(sentiment(drake_lyrics))
    # print(sentiment(beatles_lyrics))

    # print(similar(drake_lyrics,beatles_lyrics))

    # drake_lyrics_str = " ".join(drake_lyrics.keys())
    # drake_sentence = sentence_generator(drake_lyrics)
    # print(drake_sentence)

    # print(sentence_generator2("drake"))
    # print(sentence_generator2("beatles"))


if __name__ == "__main__":
    main()
