# __author__ = 'tusharmakkar08'

from sentiment_analysis import find_sentiment

text_to_analyse = 'I had a lovely experience with your product'
overall_sentiment, sentiment_probabilities = find_sentiment(text_to_analyse)

print(overall_sentiment)
# Prints "pos"

print(sentiment_probabilities)
# Prints "{'neg': 0.37184351366773916, 'neutral': 0.10038615633006975, 'pos': 0.6281564863322608}"

