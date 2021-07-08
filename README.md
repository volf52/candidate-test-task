# candidate-test-task
 A task meant to test Divly developer candidates


### Parsing transactions from CSV
A common task and recurring tasks is to build integrations for importing transactions from csv files from crypto exchanges.
The CSV files are similar in how they list transactions but often have different ways of representing transactions and the data within them.
Some transactions are listed on one row, some on two or more. It's your job to build a parser that is able to handle different kinds of CSV files.




### Requirements
- You must use Python
- You must use the `pandas` library to parse the csv files
- Follow pythons PEP 8 style guide

To store a transaction in the database the output needs to be in json as below. For each transaction 
that is parsed, the expected output should be as the below. You may show the results by printing it.


Example output:


**Trade**:

 ```json
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

 ```json
 {
     'date':'YYYY-mm-dd HH:mm',
     'transaction_type':'Trade',
     'received_amount': 20,
     'received_currency_iso': 'BTC',
     'sent_amount': null,
     'sent_currency_iso': null,
 }

```


### Guideslines
 - Design the parser for scale
 - Design the parser for readability rather than efficiency




