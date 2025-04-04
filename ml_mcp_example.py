from mcp.server.fastmcp import FastMCP
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Initialize the MCP server
mcp = FastMCP("Classic ML Training Server")

# Tool: Train a classifier using data from a CSV file
@mcp.tool()
def train_classifier_from_csv(data_path: str, target_column: str, test_size: float = 0.3, random_state: int = 42) -> dict:
    """
    Trains a logistic regression classifier using data loaded from a CSV file.

    Parameters:
      - data_path: Path to the CSV file.
      - target_column: Name of the target column in the CSV.
      - test_size: Proportion of the dataset to include in the test split.
      - random_state: Seed used by the random number generator.

    Returns:
      A dictionary containing:
        - accuracy: Accuracy of the model on the test set.
        - coefficients: The model coefficients.
        - intercept: The model intercept.
    """
    try:
        # Load the dataset from CSV
        data = pd.read_csv(data_path)
        if target_column not in data.columns:
            return {"error": f"Target column '{target_column}' not found in data."}

        # Separate features and target variable
        X = data.drop(columns=[target_column])
        y = data[target_column]

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # Initialize and train the logistic regression classifier
        clf = LogisticRegression(max_iter=200, random_state=random_state)
        clf.fit(X_train, y_train)

        # Evaluate the model
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        return {
            "accuracy": accuracy,
            "coefficients": clf.coef_.tolist(),
            "intercept": clf.intercept_.tolist()
        }
    except Exception as e:
        return {"error": str(e)}

# Run the MCP server
if __name__ == "__main__":
    mcp.run()
