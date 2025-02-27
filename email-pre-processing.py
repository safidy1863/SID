import re
import pandas as pd


df = pd.read_csv("emails_recus.csv")

def extract_features(subject):
    keywords = ["promo", "offre", "newsletter", "gagner", "rabais"]
    num_keywords = sum(1 for word in keywords if word.lower() in subject.lower())
    num_uppercase = sum(1 for char in subject if char.isupper())
    num_links = len(re.findall(r"https?://\S+", subject))
    length = len(subject)
    
    return pd.Series([num_keywords, num_uppercase, num_links, length])

df[["num_keywords", "num_uppercase", "num_links", "length"]] = df["subject"].apply(extract_features)

df.to_csv("emails_features_sipina.txt", sep="\t", index=False)
