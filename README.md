# Multi-label Text Classification for Stack Overflow Tags

## Description

Ce projet vise à développer un système automatique de suggestion de tags pour les questions posées sur **Stack Overflow**, une plateforme utilisée quotidiennement par des millions de développeurs. Les tags permettent d’organiser les informations et de faciliter la recherche, mais leur attribution manuelle peut être imprécise. Ce projet teste des solutions basées sur l’apprentissage supervisé et non-supervisé pour améliorer ce processus.

## Fonctionnalités principales

- **Prétraitement des données textuelles** :
  - Nettoyage des titres et corps des questions.
  - Extraction et nettoyage des tags avec des approches robustes.
  - Utilisation de techniques avancées comme TF-IDF, Word2Vec, BERT et USE pour la vectorisation des textes.
  
- **Analyse exploratoire des données** :
  - Distribution des mots et tokens.
  - Création de nuages de mots et analyse des tokens les plus fréquents.

- **Approches de modélisation** :
  - **Non-supervisée** : Utilisation de LDA (Latent Dirichlet Allocation) pour identifier les topics dominants.
  - **Supervisée** : Implémentation de modèles comme Logistic Regression, SGDClassifier, et LinearSVC pour une classification multi-label à l’aide de OneVsRestClassifier.
  
- **Suivi et validation** :
  - Optimisation des hyperparamètres avec RandomizedSearchCV.
  - Suivi des expérimentations avec MLFlow.
  - Évaluation des performances avec le Jaccard Score.

- **API de prédiction** :
  - Développement d’une API pour suggérer automatiquement des tags en texte libre.
  - Déploiement cloud via AWS (API Gateway, Lambda, EC2).
  - Intégration et validation de bout en bout avec Postman.
  - <a href="https://misszeferino.github.io/NLP-Multilabel-Classification/" target="_blank">>>> Click here to test the API</a>

## Technologies utilisées

- **Prétraitement des données** : Python, BeautifulSoup, scikit-learn.
- **Vectorisation** : CountVectorizer, TF-IDF, Word2Vec, BERT, USE.
- **Modélisation** : Logistic Regression, SGDClassifier, LinearSVC.
- **Déploiement** : AWS (API Gateway, Lambda, EC2, CloudWatch), Docker.
- **Suivi des expérimentations** : MLFlow.

## Résultats

- La meilleure précision a été obtenue avec un modèle **LinearSVC**, avec des scores Jaccard supérieurs à ceux obtenus avec Logistic Regression et SGDClassifier.

## Utilisation

- **Prédiction des tags** : Utilisez l’API déployée pour obtenir des suggestions de tags en fonction de questions en texte libre.

## Ressources

- [Documentation du projet](https://github.com/misszeferino/NLP-Multilabel-Classification/blob/4063e953c56ea10f51403f90b456a91e11791af1/Multi-label%20Text%20Classification.pdf)
- [API déployée sur AWS](https://misszeferino.github.io/NLP-Multilabel-Classification/)

## Auteurs

- **Luciana Zeferino** - Projet réalisé dans le cadre du parcours Machine Learning Engineer chez OpenClassrooms.

