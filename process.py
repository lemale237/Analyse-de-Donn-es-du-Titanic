# process.py
import pandas as pd

def clean_df_train(df_train):
    # Identifiez et traitez les valeurs manquantes
    df_train['Age'].fillna(df['Age'].median(), inplace=True)
    df_train['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

  # la raison d'utilisation de fillna est qu'elle remplace les données manquantes par des données appropriées au lieu de les
  # supprimer entièrement avec dropna.

    return df_train


def clean_df_train(df_train):
    # Identifiez et traitez les valeurs manquantes
    df_test['Age'].fillna(df['Age'].median(), inplace=True)
    df_test['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    return df_test
