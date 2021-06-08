"""
Getting Afinn sentiment scores for the data to compare with Danish Vader. Sanity Check.
"""
import pandas as pd
from afinn import Afinn
from sentida import Sentida

SV = Sentida()
afinn = Afinn(language='da')

def sentida_sentiment(row):
    tweet = row["mentioneless_text"]
    return SV.sentida(text = tweet, output = 'mean', normal = True)

def get_Afinn_sentiment(row):
    text = row["mentioneless_text"]
    return afinn.score(text)

df = pd.read_csv("../../hope-keyword-templates/vaccin_vis.csv")
df = df.sort_values("created_at")

df["sentida_sentiment"] = df.apply(lambda row: sentida_sentiment(row), axis = 1)
df["afinn_sentiment"] = df.apply(lambda row: get_Afinn_sentiment(row), axis = 1)

df.to_csv("../vaccin_vis_afinn.csv", index=False)