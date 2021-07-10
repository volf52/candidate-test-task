from pathlib import Path
from pprint import pp
from typing import Union

import pandas as pd

EXCHANGE1_COLS = {"TRANSACTION_ID", "TYPE", "DATE", "AMOUNT", "CURRENCY"}
EXCHANGE2_COLS = {"TYPE", "TIME", "SOLD AMOUNT", "BOUGHT AMOUNT", "CURRENCIES"}


class CSVParser:
    """
    A class responsible for reading and parsing csv files from the
    crypto wallets and exchanges.
    """

    __slots__ = "transactions"

    def __init__(self, file_path: Union[str, Path]):
        self.transactions = []

        # If the files are large, we can consume the file in chunks
        df = pd.read_csv(file_path)

        _, exchange_type = self._preprocess_dataframe(df)

        for _, row in df.iterrows():
            transaction: dict

            if row["TYPE"] == "DEPOSIT":
                transaction = self.process_deposit(row, exchange_type)
            elif row["TYPE"] == "WITHDRAWAL":
                transaction = self.process_withdrawal(row, exchange_type)
            elif row["TYPE"] in {"TRADE", "BUY", "SELL"}:
                transaction = self.process_trade(row, exchange_type)
            else:
                raise ValueError(f"Unrecognized transaction type {row['TYPE']}")

            transaction["date"] = row["DATETIME"]
            self.transactions.append(transaction)

    @staticmethod
    def _preprocess_dataframe(df: pd.DataFrame, *, inplace=True):
        cols = set(df.columns)

        if not inplace:
            df = df.copy(deep=True)

        df["TYPE"] = df["TYPE"].astype(str).apply(lambda x: x.upper())

        if cols == EXCHANGE1_COLS:
            df["AMOUNT"] = df["AMOUNT"].astype(float)

            df.rename(columns={"DATE": "DATETIME"}, inplace=True)
            df.drop(columns=["TRANSACTION_ID"], inplace=True)
            exchange_type = 1
        elif cols == EXCHANGE2_COLS:
            df["SOLD AMOUNT"] = df["SOLD AMOUNT"].fillna(0).astype(float)
            df["BOUGHT AMOUNT"] = df["BOUGHT AMOUNT"].fillna(0).astype(float)

            df.rename(
                columns={"CURRENCIES": "CURRENCY", "TIME": "DATETIME"}, inplace=True
            )

            exchange_type = 2
        else:
            raise ValueError("Unrecognized Exchange Type")

        df["DATETIME"] = pd.to_datetime(df["DATETIME"]).dt.strftime("%Y-%m-%d %H:%M")

        # Can set `exchange_type` as an enum type when required
        return df, exchange_type

    @staticmethod
    def process_deposit(row: pd.Series, exchange_type: int):
        transaction = {
            "transaction_type": "Deposit",
            "sent_amount": None,
            "sent_currency_iso": None,
            "received_currency_iso": row["CURRENCY"],
        }

        if exchange_type == 1:
            col = "AMOUNT"
        elif exchange_type == 2:
            col = "BOUGHT AMOUNT"
        else:
            raise ValueError("Unrecognized Exchange Type")

        transaction["received_amount"] = row[col]

        return transaction

    @staticmethod
    def process_withdrawal(row: pd.Series, exchange_type: int):
        transaction = {
            "transaction_type": "Withdrawal",
            "received_amount": None,
            "received_currency_iso": None,
            "sent_currency_iso": row["CURRENCY"],
        }

        if exchange_type == 1:
            amount = -row["AMOUNT"]
        elif exchange_type == 2:
            amount = row["SOLD AMOUNT"]
        else:
            raise ValueError("Unrecognized Exchange Type")

        transaction["sent_amount"] = amount

        return transaction

    @staticmethod
    def process_trade(row: pd.Series, exchange_type: int):
        transaction = {
            "transaction_type": "Trade",
        }

        return transaction

    def print_results(self):
        """
        Public method printing the output from parsing transactions
        """
        pp(self.transactions)


if __name__ == "__main__":
    root = Path("exchange_files")

    file1 = root / "exchange_1_transaction_file.csv"
    file2 = root / "exchange_2_transaction_file.csv"

    parser = CSVParser(file1)
    parser.print_results()

    print("=" * 79)
    parser = CSVParser(file2)
    parser.print_results()
