import unittest

import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split


class IrisClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(IrisClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.relu3 = nn.ReLU()
        self.fc4 = nn.Linear(hidden_size, hidden_size)
        self.relu4 = nn.ReLU()
        self.fc5 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu1(out)
        out = self.fc2(out)
        out = self.relu2(out)
        out = self.fc3(out)
        out = self.relu3(out)
        out = self.fc4(out)
        out = self.relu4(out)
        out = self.fc5(out)
        return out


class Test(unittest.TestCase):

    def test_graph_computation(self):
        x = torch.rand(5, 3)
        print(x)

        def add_function(x, y):
            c = x + y
            return c

        name = "graph.pt"
        a = torch.tensor(2.0)
        b = torch.tensor(3.0)
        graph = torch.jit.trace(add_function, (a, b))
        graph.save(name)

        loaded_graph = torch.jit.load(name)
        a2 = torch.tensor(15.0)
        b2 = torch.tensor(4.0)
        result = loaded_graph(a2, b2)
        result_value = result.item()
        print(result)
        print(result_value)

    def test_iris(self):
        # iris = load_iris()
        # Pandas DataFrame
        '''
        iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        iris_df['target'] = iris.target
        iris_df.to_csv('iris_dataset.csv', index=False)
        '''
        iris_df = pd.read_csv('test/lessons/pytorch_lessons/iris_dataset.csv')
        # split data to train and test data
        X = iris_df.drop('target', axis=1).values
        y = iris_df['target'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Normalize data
        X_train = torch.tensor(X_train, dtype=torch.float32)
        y_train = torch.tensor(y_train, dtype=torch.int64)
        X_test = torch.tensor(X_test, dtype=torch.float32)
        y_test = torch.tensor(y_test, dtype=torch.int64)

        # Model
        input_size = len(iris_df.columns) - 1
        hidden_size = 64
        output_size = len(set(y))
        model = IrisClassifier(input_size, hidden_size, output_size)

        # Train
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        num_epochs = 100
        for epoch in range(num_epochs):
            model.train()
            outputs = model(X_train)
            loss = criterion(outputs, y_train)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        torch.save(model.state_dict(), 'iris_model.pth')

        # Evaluate performance and ...
        model.eval()
        with torch.no_grad():
            correct = 0
            total = 0
            outputs = model(X_test)
            _, predicted = torch.max(outputs, 1)
            total += y_test.size(0)
            correct += (predicted == y_test).sum().item()

        # Prediction
        new_data = [5.1, 3.5, 1.4, 0.2]
        new_data = torch.tensor(new_data, dtype=torch.float32)
        model.eval()
        with torch.no_grad():
            prediction = model(new_data)
            _, predicted_class = torch.max(prediction, 0)
            print(f'Predicted class: {predicted_class.item()}')


if __name__ == "__main__":
    unittest.main()
