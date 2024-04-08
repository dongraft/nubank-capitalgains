# Nubank Code Challenge - Capital Gains
## Introduction
Capital Gains is a CLI (Command Line Interface) that calculates how many taxes should be paid based on the history of
transactions of two main operations: Selling and Buying stock.

## Implementation
### Rules

    Buying Stocks:
        When stocks are purchased, the transaction does not incur any taxes.
        The cost of purchasing these stocks is used to calculate the weighted average price of the stock holdings.

    Selling Stocks:
        Selling stocks may result in either a profit or a loss, depending on the selling price compared to the weighted
        average price.
        No taxes are paid on losses. Instead, losses are carried forward to offset profits in future sell transactions.

    Weighted Average Price:
        The weighted average price represents the average cost of stocks held, calculated each time stocks are bought.
        It is computed as the total cost of all stock purchases divided by the total number of stocks owned.

    Carry-Over Loss:
        Losses from selling stocks at a price lower than the weighted average price are accumulated.
        These losses are then used to reduce taxable profits from future sales.

    Tax Calculation:
        Taxes are only paid on profits that remain after offsetting any accumulated losses.
        A 20% tax rate is applied to the taxable profits.
        No taxes are due if the total sale amount (selling price times quantity) is $20,000 or less, regardless of the
        profit or loss situation.

    Portfolio Reset:
        If all stocks in the portfolio are sold, the weighted average price resets.
        Subsequent purchases of stock will establish a new weighted average price.


### Codebase
The code was written in Python. Divided by concerns:
- `operation.py`- Container of `Operation` which saves the action, unit cost and quantity of a stock operation.
   It also defines the total cost of an Operation as `quantity * unit_cost`.
- `portfolio.py`- Defining `Portfolio`, it saves the number of stock and the weighted average price, updated everytime a
   sell or buy action are performed.
- `tax_calculator.py`- Home of the `TaxCalculator` class. It saves the loss carry amount defined everytime a tax is
   calculated by `calculate_tax`, which receives an operation and a `weighted_average_price`.

It proceeds as follows:
- `main.py`- Executes the main application in a single call
- `capital_gains.py` - Home for `calculate_taxes` function which will parse the stdin input into `Operation` elements,
   update the portfolio with the operation and calculate the corresponding taxes everytime an event occurs.

#### Testing
Testing was done. Integration tests by defining the examples at the pdf sent. And unit testing the Portfolio and Tax
Calculator.
#### Notes

The implementation tries to follow SOLID Principles, but for simplicity of the code, some principles were left out.

For example, `TaxCalculator` could be implemented using a `TaxCalculationStratety` and `Portfolio`could have been an
interface or abstract class

#### Running the project
The application uses a file as input from `stdin`
In order to run in it, there are two ways:
##### Just Python
Any version of Python >= 3.7 should work.

`python3 main.py < ../test.txt` should run the main code with a file input
`python3 -m unittest` runs all the tests
##### Docker
If Docker is the preferred way, a simple script was made: `capital-gains`
`./capital-gains < ../test.txt`uses a file input, while `./capital-gains test` runs all the tests.
The script is basically an alias for `docker-compose run`
