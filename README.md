# candidate-test-task
 A task meant to test Divly Python developer candidates


### Parsing transactions from CSV
A common task and recurring tasks is to build integrations for importing transactions via csv files from crypto exchanges.
The CSV files are similar in how they list transactions but often have different ways of representing transactions and the data within them.
Some transactions are listed on one row, some on two or more. It's your job to design and build a parsing design that can read and output
the two provided example csv files which represenets two real files from two different crypto exchanges. How a transaction is read
isn't always obvious and how well you figure this out is part of the assesment in the test.


### Input
The `CSVParser` class takes a path to a csv_file as input.

### Requirements
- You must use Python 3.x
- You must use the `pandas` library to parse the csv files
- Follow pythons PEP 8 style guide
- The `CSVParser` class must be used for printing the results as already written in `main.py`. Aside from that you may design and structure other functions, classes or data structures exactly how you want to. Your design choices are evaluated in the test.
- You must be able to parse all existing transactions in the the two different example files

### Expected output
To store a transaction in the database the output needs to be in json as below. For each transaction 
that is parsed, the expected output should be as the below for each of the transactin types. You may show the results simply by printing it
using the `print_results()` method in the `CSVParser` class found in `main.py`. Note that there are three different transaction types and how they differ in their output formatt below.


Example output:


**Trade**:

 ```javascript
 {
     'date':'YYYY-mm-dd HH:mm',
     'transaction_type':'Trade',
     'received_amount': 20
     'received_currency_iso': 'BTC'
     'sent_amount': 100
     'sent_currency_iso': 'USD'
 }

```

**Deposit**:

 ```javascript
 {
     'date':'YYYY-mm-dd HH:mm',
     'transaction_type':'Deposit',
     'received_amount': 20,
     'received_currency_iso': 'BTC',
     'sent_amount': null,
     'sent_currency_iso': null,
 }

```

**Withdrawal**:

 ```javascript
 {
     'date':'YYYY-mm-dd HH:mm',
     'transaction_type':'Withdrawal',
     'received_amount': null,
     'received_currency_iso': null,
     'sent_amount': 20,
     'sent_currency_iso': 'BTC',
 }

```


### What we asses in your code test:
 - How well your chosen design the parser for scale
 - How easy the design and code is to understand
 - How well the design works if we would like to add more files in the future.
 - How well you understand how transactions should be interpreted without explicit instructions on what the file lists (as it will be in the real world.)
 - How Pythonic the code style is (not super important)
 



