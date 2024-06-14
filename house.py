import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = r'C:\Users\OS\Desktop\Workspace\hapt\Housing1.csv' #Tự thay link vào nhé

housing_data = pd.read_csv(file_path)

# Splitting the dataset
X = housing_data.drop('price', axis=1)
y = housing_data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing for numerical data
numerical_transformer = StandardScaler()

# Preprocessing for categorical data
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, X.select_dtypes(include=['int64', 'float64']).columns),
        ('cat', categorical_transformer, X.select_dtypes(include=['object']).columns)
    ])

# Define model
model = LinearRegression()

# Create and evaluate the pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', model)
                           ])

# Train the model
pipeline.fit(X_train, y_train)

# Function to make predictions based on user input
def predict_house_price(model, preprocessor):
    inputs = {}
    for col in X.columns:
        if col in X.select_dtypes(include=['object']).columns:
            unique_values = X[col].unique()
            value = input(f"Enter {col} (Available options: {list(unique_values)}): ")
            # Ensure value is among the unique values in the column
            if value not in unique_values:
                print("Invalid input! Please select from the available options.")
                return None
        else:
            value = input(f"Enter {col}: ")
            # Ensure numerical columns are converted to float
            value = float(value)
        inputs[col] = [value]

    # Convert user input into DataFrame
    user_input = pd.DataFrame.from_dict(inputs)

    # Making prediction
    predicted_price = pipeline.predict(user_input)
    return predicted_price[0]

# User input and prediction
predicted_price = predict_house_price(model, preprocessor)
if predicted_price is not None:
    print(f"The predicted house price is: {predicted_price}")