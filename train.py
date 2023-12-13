# train.py
from Td.py import df_train
from process.py import clean_df_train
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# Divisez votre dataset en ensembles d'entraînement et de test
X = clean_df_train(df_train).drop('Survived', axis=1)
y = clean_df_train(df_train)['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train['Name'] = label_encoder.fit_transform(X_train['Name'])
X_test['Name'] = label_encoder.fit_transform(X_test['Name'])

numerical_columns = ['Age']

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))  # Remplace les valeurs manquantes par la moyenne
])

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Remplace les valeurs manquantes par la valeur la plus fréquente
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Supposez que 'Name' est la colonne avec des noms
label_encoder = LabelEncoder()
X_train['Name'] = label_encoder.fit_transform(X_train['Name'])
X_test['Name'] = label_encoder.fit_transform(X_test['Name'])

# Supprimer la colonne 'Sex' du DataFrame X_train
X_train.drop(columns=['Sex'], inplace=True)

# Supprimer la colonne 'Sex' du DataFrame X_test
X_test.drop(columns=['Sex'], inplace=True)

# Supprimer la colonne 'Ticket' du DataFrame X_train
X_train.drop(columns=['Ticket'], inplace=True)

# Supprimer la colonne 'Ticket' du DataFrame X_test
X_test.drop(columns=['Ticket'], inplace=True)

# Supprimer la colonne 'Cabin' du DataFrame X_train
X_train.drop(columns=['Cabin'], inplace=True)

# Supprimer la colonne 'Cabin' du DataFrame X_test
X_test.drop(columns=['Cabin'], inplace=True)

# Supprimer la colonne 'Embarked' du DataFrame X_train
X_train.drop(columns=['Embarked'], inplace=True)

# Supprimer la colonne 'Embarked' du DataFrame X_test
X_test.drop(columns=['Embarked'], inplace=True)

# Construisez un modèle de classification
model = LogisticRegression()
model.fit(X_train, y_train)

# Évaluez la performance de votre modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Rapport de classification
print(classification_report(y_test, y_pred))
