# Code du projet

## Fichiers : fonctions et scripts

### Participations au projet

"Participer au projet" peut dire plusieurs choses. Cela peut se faire :

- En créant une ou des branches afin de suggérer directement des modification ou
des nouvelles fonctionnalités qui peuvent être implémantées par la suite dans le code global du projet
- En signalant des bugs, en envoyant des suggestions sans créer de branche,
en signalant des potentiels risques et vulnérabilités
- En rejoignant directement l'équipe des collaborateurs et en étant actif sur le projet

### Copie partielle et utilisation du projet

Cette page GitHub a été créée dans le but de savoir exactement ce que fait Hot Zone Bot,
créant une transparence entre développeurs et utilisateurs.

La copie partielle des fichiers du projet est autorisée. Tant que
vous n'en faites aucune utilisation commerciale.

### Copie totale et usurpation

Comme dit précédemment, il est autorissé de copier et utiliser des fichiers du projet.
Cependant, il est strictement prohibé de copier et d'utiliser l'intégralité des fichiers présents
tout en créant une copie parfaite du bot relié au projet.

## Données des utilisateurs

Toute donnée collectée par le bot est stockée dans ses fichiers. L'intégralité de ses données resteront privées
et ne seront pas partagées avec des tiers.
Seules les données nécessaires au fonctionnement du bot sont collectées.
Cela exclut toute donnée sensible ou personnelle des utilisateurs.

## Installation des modules

Pour faire fonctionner le bot, vous devez installer les modules suivants :

- `discord.py` - 2.6.3
- `python-dotenv` - 1.0.0
- `requests` - 2.31.0
- `pyyaml` - 6.0

L'installation de ces modules sur votre machine doit se faire via un terminal ou une invite de commande.
Vous pouvez utiliser la commande `pip install -r requirements.txt` pour installer automatiquement
tous les modules nécessaires qui apparaissent dans le fichier `requirements.txt`.

> Assurez-vous d'avoir `pip` installé sur votre machine avant d'exécuter cette commande.

Vous pourrez ensuite installer les modules dans votre environnement virtuel si vous en utilisez un.

> Vous pouvez créer un environnement virtuel avec la commande `python -m venv "nom_de_votre_env"`.

Pour activer l'environnement virtuel, utilisez la commande appropriée en fonction de votre système d'exploitation :

- Sur Windows :

```text
"nom_de_votre_env"\Scripts\activate
```

- Sur macOS et Linux :

```text
source "nom_de_votre_env"/bin/activate
```

> Vous pouvez aussi choisir l'interprêteur Python de votre environnement virtuel
directement dans votre éditeur de code (en bas à droite dans VSCode par exemple).

Après avoir activé votre environnement virtuel, vous pouvez exécuter la commande `pip install -r requirements.txt`
directement dans le terminal de votre éditeur de code avec l'environnement virtuel activé.

## Lancement du bot

Plusieurs fichiers `.py` permettent de lancer le bot.
Ceux-ci sont situés à la racine du projet et commencent par `S_`.

Ceux-ci lancent le bot avec des configurations différentes.
Par exemple, `S_En Ligne.py` lance le bot en mode en ligne,
tandis que `S_Updating.py` lance le bot avec le statut "Mise à jour en cours...".

> Le bot est capable de tourner en 24/7 si votre hébergeur le permet.

## Mise à jour du bot

Les fichiers du projet sont mis à jour régulièrement pour ajouter des fonctionnalités,
corriger des bugs et améliorer la sécurité.
Vous pouvez consulter l'historique des modifications dans l'onglet "Commits" de ce dépôt GitHub.
Il est recommandé de vérifier régulièrement les mises à jour
et de les appliquer pour bénéficier des dernières améliorations.

> Vous pouvez également suivre les discussions
et les demandes de fonctionnalités dans l'onglet "Issues" de ce dépôt GitHub.
---
> Notez qu'aucun module ne sera supprimé et que ceux déjà présents dans le projet ne seront pas mis à jour de manière
régulière afin d'éviter de rendre des commandes inutilisables et de devoir les réécrire.
Cependant, des mises à jour ponctuelles des modules peuvent être effectuées si nécessaire.

---

## Support et contact

Pour toute question, suggestion ou problème lié au projet, vous pouvez ouvrir une "Issue" dans ce dépôt GitHub.
Vous pouvez également contacter l'équipe de développement et des collaborateurs
via le [serveur Discord du projet](https://discord.gg/SC2X7yWU6Y)