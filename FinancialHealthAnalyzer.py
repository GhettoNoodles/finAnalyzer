import unittest
from io import StringIO


# FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
# This class does not need to be edited
class FinancialTransaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)


class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    # Adds together all transactions labeled "Income"
    def total_revenue(self):
        return round(sum(transaction.amount for transaction in self.transactions if transaction.type == "Income"),2)

    # Adds together all transactions labeled "Expense"
    def total_expenses(self):
        return round(sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense"),2)

    def profit(self):
        return round(self.total_revenue() - self.total_expenses(),2)

    def profit_margin(self):
         return round(self.profit() / self.total_revenue(),2)

    def average_transaction_amount(self):
        return self.profit()/len(self.transactions)

    # Determines finalncial health and returns the corresponding string
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        elif -1000 >= profit < 0:
            return "Warning"
        else:
            return "Critical"


class TestFinancialHealthAnalyzer(unittest.TestCase):
    # Setup data allows for code to be tested without manually writing test transaction code for every test function.
    # setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 1000),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 2000),
            FinancialTransaction("2024-01-06", "Income", 870),
            FinancialTransaction("2024-01-08", "Expense", 400.03),
            FinancialTransaction("2024-01-10", "Expense", 575.99),
            FinancialTransaction("2024-01-11", "Income", 1692),
            FinancialTransaction("2024-01-15", "Income", 1000.1),
            FinancialTransaction("2024-02-18", "Expense", 800.78),
            FinancialTransaction("2024-03-20", "Expense", 300.90),
            FinancialTransaction("2025-01-24", "Income", 2300)
        ]
        self.transactions = transactions_data

    #Test the method that calculates the total revenue
    def test_total_revenue(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_revenue(), 8862.1, "Total revenue should be 8862.1")

    # Test the method that calculates the total expenses
    def test_total_expenses(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_expenses(), 2877.7, "Total expenses should be 2877.7")

    # Test the method that calculates the profit
    def test_profit(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit(),5984.4, "Profit is should be 5984.4")

    # Test the method that calculates the profit margin
    def test_profit_margin(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit_margin(),0.68,"Profit margin should be 0.68")

    # Test the method that calculates the average transaction amount
    def test_average_transaction_amount(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.average_transaction_amount(),498.7,"Average transaction amount should be 498.7")

    def test_financial_health(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.financial_health(),"Healthy","Financial health should be healthy")

# Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main
if __name__ == '__main__':
    # Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
        FinancialTransaction("2024-01-01", "Income", 50),
        FinancialTransaction("2024-01-02", "Expense", 500),
        FinancialTransaction("2024-01-03", "Expense", 300),
        FinancialTransaction("2024-01-04", "Income", 75)
    ]
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)
    print("Profit: ")
    print("Profit margin: ")
    print("Average transaction amount: ")
    print("Financial health: ")
    unittest.main()
