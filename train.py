# train.py
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Divisez votre dataset en ensembles d'entraînement et de test
x = df_train.drop('Survived', axis=1)
y = df_train['Survived']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construisez un modèle de classification
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Évaluez la performance de votre modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Classification report
print(classification_report(y_test, y_pred))
