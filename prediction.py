import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

file_path = r'C:\Users\OS\Desktop\Workspace\hapt\Housing1.csv' 

housing_data = pd.read_csv(file_path)

X = housing_data.drop('price', axis=1)
y = housing_data['price']

numerical_transformer = StandardScaler()

categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, X.select_dtypes(include=['int64', 'float64']).columns),
        ('cat', categorical_transformer, X.select_dtypes(include=['object']).columns)])

model = LinearRegression()

pipeline = Pipeline(steps=[('preprocessor', preprocessor),('model', model)])

pipeline.fit(X, y)

def predict_house_price(value):
    
    inputs = {}
    count = 0
    for col in X.columns:

        inputs[col] = [value[count]]
        count += 1
    user_input = pd.DataFrame.from_dict(inputs)
    predicted_price = pipeline.predict(user_input)
    return predicted_price[0]

def suggest_house_features(user_price):
    
    dataset_prices = y.tolist()
    closest_price = min(dataset_prices, key=lambda x: abs(x - user_price))
    closest_price_index = dataset_prices.index(closest_price)
    closest_price_features = X.iloc[closest_price_index]
    return y[dataset_prices.index(min(dataset_prices))],closest_price_features






