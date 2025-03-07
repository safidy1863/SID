### Lancement de notre application

* Installation des dépendances
```bash 
pip3 install -r requirements.txt
```

* Récupération des emails (Boîte de réception)
```bash 
python3 email-recovery.py
```

* Prétraitement des emails

```bash 
python3 email-pre-processing.py
```

* Importation des données dans SIPINA :
Entraîner les algorithmes de décision avec les données dans le fichier `emails_features_sipina.txt`

* Définisser dans votre SIPINA que is_spam est un variable cible 
* Entraîner le modèle
* Supprimer la colonne is_spam et laisse l'arbre de décision connaître l'email si c'est un spam ou non
