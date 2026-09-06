#project2  Data Classi f ication using AI

# 1. Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Load the dataset
data = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

# 3. Understand the dataset
print("First 5 rows:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nDataset Shape:")
print(data.shape)

# 4. Select features and target
X = data[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]]
y = data["OrderStatus"]

# 5. Convert target labels into numbers
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# 6. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# 7. Create the classification model
model = DecisionTreeClassifier(random_state=42)

# 8. Train the model
model.fit(X_train, y_train)

# 9. Make predictions
y_pred = model.predict(X_test)

# 10. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))