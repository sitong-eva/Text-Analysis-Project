import part1
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thefuzz import fuzz
from thefuzz import process
import numpy as npc
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

#Summarization

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
    This function compares the Drake lyrics with the Beatles lyrics to see how much of the Drake lyrics is unique from the Beatles lyrics.
    """
    unique = 0
    total = 0
    for key in d1:
        total += 1
        if key not in d2:
            unique += 1
    res = unique / total * 100
    return f"{res:.2f}%"

#Natural Language Processing

def sentiment(musician):
    """
    This functions tells the sentiment of the musician based on their lyrics.
    """
    analyzer=SentimentIntensityAnalyzer()
    if isinstance(musician, int):
        musician=str(musician)
    sentences=nltk.sent_tokenize(str(musician))
    scores=[]
    for sentence in sentences:
        score = analyzer.polarity_scores(sentence)
        scores.append(score['compound'])
        average=sum(scores)/len(scores)
    return average

def similar(musician1, musician2):  
    """
    This function provides a similarity score between the lyrics of two musicians.
    """ 
    for lyrics in musician1.values():
        musician1_lyrics=''.join(str(lyrics))
    for lyrics in musician2.values():                                 
        musician2_lyrics=''.join(str(lyrics))
    ratio=fuzz.ratio((musician1_lyrics.lower()),musician2_lyrics.lower())
    return f'Similarity score: {ratio}'



def main():
    drake=part1.process_file("drake_lyrics.txt")
    beatles=part1.process_file("beatles.txt")

    # print(drake)
    # print(total_words(drake))
    # print(most_common10(drake,excluding_stopwords=True))
    # print(drakevbeatles(drake,beatles))

    # print(sentiment(drake))
    # print(sentiment(beatles))

    print(similar(drake,beatles))

if __name__ == "__main__":
    main()