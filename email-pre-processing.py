import pandas as pd
import re
import numpy as np

df_emails = pd.read_csv("emails_recus.csv", sep="\t")

spam_keywords = ["promo", "newsletter", "sale", "discount", "deal", "offre", "pub"]

def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^\w\s]", "", text) 
        return text
    return ""

def extract_features(df):
    df["subject_clean"] = df["subject"].apply(clean_text)
    df["subject_length"] = df["subject_clean"].apply(len)  # Longueur du sujet
    df["num_keywords"] = df["subject_clean"].apply(lambda x: sum(1 for word in spam_keywords if word in x))  # Nombre de mots-clés spam
    df["num_links"] = df["subject"].apply(lambda x: len(re.findall(r"http[s]?://", x)) if isinstance(x, str) else 0)  # Nombre de liens
    return df

df_emails = extract_features(df_emails)

df_emails["is_spam"] = df_emails["is_spam"].map({0: "important", 1: "spam"})

df_emails = df_emails[["is_spam","subject_clean","subject_length", "num_keywords", "num_links"]]

df_emails.to_csv("emails_features_sipina.txt", index=False, sep="\t")

print("✅ Prétraitement terminé ! Données enregistrées dans 'emails_features_sipina.txt'")
