import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('titanic.csv')

df.drop(['PassengerId','Name', 'Ticket', 'Fare', 'Cabin', 'Embarked'], axis = 1, inplace = True)

age1 = df[df['Pclass'] == 1]['Age'].median()
age2 = df[df['Pclass'] == 2]['Age'].median()
age3 = df[df['Pclass'] == 3]['Age'].median()


def fill_age(value):
    if pd.isnull(value['Age']):
        if value['Pclass'] == 1:
            return age1
        if value['Pclass'] == 2:
            return age2
        if value['Pclass'] == 3:
            return age3
    return value['Age']

def fill_gender(value):
    if value == 'male':
        return 1
    else:
        return 0

# def fill_embarked(value):
#     if value == 'S':
#         return 1
#     if value == 'Q':
#         return 2
#     else:
#         return 3


df['Sex'] =  df['Sex'].apply(fill_gender)
# df['Embarked'] =  df['Embarked'].apply(fill_embarked)
df['Age'] = df.apply(fill_age, axis = 1)

X = df.drop('Survived', axis = 1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.50)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print('Percentage of correctly predicted outcomes:', accuracy_score(y_test, y_pred) * 100)
print('Confusion matrix:')
print(confusion_matrix(y_test, y_pred))


