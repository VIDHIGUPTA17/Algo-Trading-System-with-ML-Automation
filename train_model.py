# # # ml_model/train_model.py
# # from sklearn.model_selection import train_test_split
# # from sklearn.tree import DecisionTreeClassifier
# # from sklearn.metrics import accuracy_score
# # import joblib

# # def train(df):
# #     X = df[['RSI','MA20','MA50','MACD','Signal','volume']]
# #     y = df['target']
# #     X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,shuffle=False)
# #     model = DecisionTreeClassifier(max_depth=5)
# #     model.fit(X_train,y_train)
# #     preds = model.predict(X_test)
# #     print('Accuracy:', accuracy_score(y_test, preds))
# #     joblib.dump(model,'ml_model/model.pkl')


# # ml_model/train_model.py
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# import joblib

# def train(csv_path):  # <- take path
#     df = pd.read_csv(csv_path)  # <- read the CSV file here

#     X = df[['RSI', 'MA20', 'MA50', 'MACD', 'Signal', 'volume']]
#     y = df['target']

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

#     model = DecisionTreeClassifier(max_depth=5)
#     model.fit(X_train, y_train)
#     preds = model.predict(X_test)

#     print('Accuracy:', accuracy_score(y_test, preds))

#     joblib.dump(model, 'ml_model/model.pkl')  # Save model



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

def calculate_indicators(df):
    df['MA20'] = df['close'].rolling(window=20).mean()
    df['MA50'] = df['close'].rolling(window=50).mean()

    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    exp1 = df['close'].ewm(span=12, adjust=False).mean()
    exp2 = df['close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)

    # Drop rows with NaNs caused by rolling calculations
    df.dropna(inplace=True)
    return df

def train(file_path):
    df = pd.read_csv(file_path)
    df = calculate_indicators(df)

    X = df[['RSI', 'MA20', 'MA50', 'MACD', 'Signal', 'volume']]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    print('Accuracy:', accuracy_score(y_test, preds))
    joblib.dump(model, 'model.pkl')
