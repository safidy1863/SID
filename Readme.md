### Lancement de notre application

`pip3 install -r requirements.txt`

- Récupération des emails (Boîte de réception)
`python3 email-recovery.py`

- Prétraitement des emails

Avant de classer les emails, il faut extraire des caractéristiques (features).

📌 Exemples de caractéristiques à extraire :

    Présence de mots-clés : "promo", "newsletter", "offre", "gagner"
    Nombre de majuscules
    Nombre de liens (URLs)
    Longueur du sujet


