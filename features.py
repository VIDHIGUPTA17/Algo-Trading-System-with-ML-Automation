# ml_model/features.py
def build_features(df):
    df['MACD'] = df['close'].ewm(span=12).mean() - df['close'].ewm(span=26).mean()
    df['Signal'] = df['MACD'].ewm(span=9).mean()
    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)
    return df.dropna()

# ml_model/train_model.py
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

def train(df):
    X = df[['RSI','MA20','MA50','MACD','Signal','volume']]
    y = df['target']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,shuffle=False)
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train,y_train)
    preds = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, preds))
    joblib.dump(model,'ml_model/model.pkl')
