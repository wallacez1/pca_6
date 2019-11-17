import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
filmes = pd.read_csv('./data.csv')

filmes = filmes.dropna()

filmes.rename(columns={"Nome": "nome", "Classificação(Anderson)": "nota",
                       "Tipo": "tipo", "Categoria": "categoria"}, inplace=True)

del filmes['Orçamento']
del filmes['Diretor']
del filmes['nome']


X = pd.get_dummies(
    filmes, prefix=['tipo', 'categoria'], columns=['tipo', 'categoria'])

del X['nota']

Y = pd.get_dummies(
    filmes, prefix=['nota'], columns=['nota'])

del Y['categoria']
del Y['tipo']


X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.80, random_state=1)


clf = DecisionTreeClassifier()

# # Train Decision Tree Classifer
clf.fit(X_train, y_train)

print(y_train)

y_pred = clf.predict(X_test)

print(y_pred)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
