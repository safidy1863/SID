### Lancement de notre application

`pip3 install -r requirements.txt`

1.  Récupération des emails (Boîte de réception)
`python3 email-recovery.py`

2. Prétraitement des emails

`python3 email-pre-processing.py`

3. Importation des données dans SIPINA :
Entraîner les algorithmes de décision avec les données dans le fichier `emails_features_sipina.txt`

4. Définisser dans votre SIPINA que is_spam est un variable cible 
5. Entraîner le modèle
6. Supprimer la colonne is_spam et laisse l'arbre de décision connaître l'email si c'est un spam ou non
