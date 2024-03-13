Forex EUR/USD Price Prediction

Overview

This project focuses on predicting the movement of EUR/USD prices in the Forex market, which is the largest and most liquid financial market globally. Due to the complexity and volatility of Forex markets, accurately predicting currency price movements is challenging but crucial for traders. This dataset aims to serve as a gateway for people interested in applying machine learning to trading in the Forex market.

Dataset

The dataset contains historical price data for the EUR/USD currency pair, captured at 4-hour intervals. It includes various features that are commonly used in financial market analysis.

Attributes include:

Date/Time: Timestamp of the data point.
Open: The opening price of the currency pair.
High: The highest price of the currency pair during the interval.
Low: The lowest price of the currency pair during the interval.
Close: The closing price of the currency pair.
Volume: The volume of trades.
Technical Indicators: Various technical indicators computed from the price data, such as moving averages, RSI, MACD, etc.
The target variable, 'tipo', classifies price movements as either an increase (1) or decrease (0) from the opening to the closing price within each 4-hour interval.

Preprocessing Steps

The dataset was cleaned to handle missing values and remove any irrelevant features.
Features were scaled using MinMaxScaler to normalize the input data for neural network training.
The dataset was divided into training, testing, and validation sets using train_test_split.
Models Developed
Two models were developed for the project:

Model 1: A basic neural network model without specific optimization techniques for binary classification of price movements.

Model 2: An optimized neural network model incorporating L1 and L2 regularization and the Adam optimizer to enhance model performance and prevent overfitting.

Libraries and Tools Used

Data manipulation and analysis: numpy, pandas
Data visualization: seaborn, matplotlib.pyplot
Machine learning and neural network modeling: tensorflow/keras
Model evaluation: confusion_matrix, f1_score, classification_report from sklearn.metrics
Optimization Techniques
To tackle the challenges of modeling financial market data, which often contains noise and irrelevant features, optimization techniques such as L1 and L2 regularization were employed. Additionally, the Adam optimizer was utilized for its adaptive learning rate capabilities, improving the model's convergence and generalization.

Model Evaluation and Prediction

The models were evaluated based on their accuracy, loss, specificity, F1 score, and a detailed classification report. The optimized model demonstrated a consistent improvement over the basic model, indicating the effectiveness of the applied optimization techniques.

Conclusion and Future Directions

This project showcases the application of neural networks to the challenging task of Forex price prediction. The findings highlight the importance of optimization techniques in improving model performance. Future work will explore more sophisticated models, including LSTM and CNN, to capture the temporal dependencies in price movements better.
