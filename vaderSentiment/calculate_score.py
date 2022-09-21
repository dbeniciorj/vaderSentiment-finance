import sys
meaning = sys.argv[1]
print(f"meaning was\n",meaning)
from vaderSentiment import SentimentIntensityAnalyzer as vaderSA
vader = vaderSA()
score = vader.polarity_scores(meaning)
print(score)
