import chardet
import os
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def analyze_trading_strategy(data):
    # Load data into a pandas DataFrame
    df = pd.read_excel(data)

    print(df.describe())

    # Calculate average profit/loss by Type
    df['profit_loss'] = df['Price_2'] - df['Price_1']
    avg_profit_loss_by_type = df.groupby('Type')['profit_loss'].mean()

    # Plot the average profit/loss by Type
    avg_profit_loss_by_type.plot(kind='bar')
    plt.xlabel('Type')
    plt.ylabel('Average Profit/Loss')
    plt.title('Average Profit/Loss by Type')
    plt.show()

    # Calculate average profit/loss by Size
    avg_profit_loss_by_size = df.groupby('Size')['profit_loss'].mean()

    # Plot the average profit/loss by Size
    avg_profit_loss_by_size.plot(kind='bar')
    plt.xlabel('Size')
    plt.ylabel('Average Profit/Loss')
    plt.title('Average Profit/Loss by Size')
    plt.show()

    # Calculate average profit/loss by Item
    avg_profit_loss_by_item = df.groupby('Item')['profit_loss'].mean()

    # Plot the average profit/loss by Item
    avg_profit_loss_by_item.plot(kind='bar')
    plt.xlabel('Item')
    plt.ylabel('Average Profit/Loss')
    plt.title('Average Profit/Loss by Item')
    plt.show()

if __name__ == '__main__':
    dataset = Path('../data/2023-01-15-1802_WallStreetStory_CopyTrading_Trades_2022-09-07--2023-01-14_clean.xlsx')

    print(os.getcwd())

    encoding = get_encoding(dataset)
    print(encoding)

    analyze_trading_strategy(data = dataset)
    
# EOF .
