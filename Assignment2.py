import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as analyzer
import csv
import json

names = list()
purposes = list()

# Take elements from .txt file
file1 = open("WS1.txt", "r").read()
file1 = json.loads(file1)
names.extend(list(file1.keys()))
purposes.extend(list(file1.values()))


# Take elements form .txt file
file2 = pd.read_csv("WS2.txt", sep=":", header=None)
file2[1] = file2[1].str.rstrip(",Purpose")
names.extend(list(file2[1]))
purposes.extend(list(file2[2]))


# Take elements form .csv file
file3 = pd.read_csv("WS3.csv")
names.extend(list(file3["Name"]))
purposes.extend(list(file3["Purpose"]))

# Take elements from .txt file
file4 = pd.read_csv("WS4.txt", sep=":", header=None)
names.extend(list(file4.iloc[0::2, 1]))
purposes.extend(list(file4.iloc[1::2, 1]))

# Take elements form .txt file
file5 = pd.read_csv("WS5.txt", sep=":", header=None)
names.extend(list(file5.iloc[0:50, 1]))
purposes.extend(list(file5.iloc[50:100, 1]))

# Take elements form .txt file
file6 = pd.read_csv("WS6.csv")
names.extend(list(file3["Name"]))
purposes.extend(list(file3["Purpose"]))

# Take elements form .txt file
file7 = pd.read_csv("WS7.txt", sep=":", header=None)
names.extend(list(file7.iloc[0::2, 1]))
purposes.extend(list(file7.iloc[1::2, 1]))

# Take elements form .txt file
file8 = pd.read_csv("WS8.txt", sep="\n", header=None)
file8[0] = file8[0].str.lstrip("0123456789) ")
names.extend(list(file8.iloc[0::2, 0]))
purposes.extend(list(file8.iloc[1::2, 0]))

# Take elements form .txt file
file9 = pd.read_csv("WS9.txt", sep="\t+", engine="python")
names.extend(list(file9["Name"]))
purposes.extend(list(file9["Purpose"]))

# Take elements form .csv file
file10 = pd.read_csv("WS10.csv")
names.extend(list(file10["Name"]))
purposes.extend(list(file10["Purpose"]))

# create data frame with names and purposes

finalData = pd.DataFrame(columns=["score", "names", "purposes"], index=range(0, 500))
finalData["names"] = names
finalData["purposes"] = purposes

score = []

for j in range(len(finalData["purposes"])):
    sentiment = analyzer().polarity_scores(finalData["purposes"][j])
    score.append(sentiment["compound"])

finalData["score"] = score

finalData = finalData.sort_values(by="score", ascending=False)
finalData.reset_index()
finalData.drop("index", axis=True, inplace=True)
top10 = finalData.loc[
    0:9,
]
bottom10 = finalData.loc[
    490:499,
]
