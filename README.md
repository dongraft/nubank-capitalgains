# Nubank Code Challenge - Capital Gains

## Introduction
**Capital Gains** is a Command Line Interface (CLI) application that calculates the taxes due based on the transaction history of stock operations, specifically focusing on buying and selling activities.

## Implementation

### Rules
- **Buying Stocks:**
  - No taxes are incurred when stocks are purchased.
  - The purchase cost is used to calculate the weighted average price of the stock holdings.

- **Selling Stocks:**
  - May result in profit or loss, depending on the selling price relative to the weighted average price.
  - Losses do not incur taxes and are carried forward to offset future profits.

- **Weighted Average Price:**
  - Represents the average cost of stocks held, recalculated with each purchase.
  - Calculated as the total cost of stock purchases divided by the total number of stocks owned.

- **Carry-Over Loss:**
  - Losses from selling stocks below the weighted average price accumulate.
  - These losses reduce taxable profits from subsequent sales.

- **Tax Calculation:**
  - Taxes apply only to profits remaining after offsetting any accumulated losses.
  - The tax rate is 20% on taxable profits.
  - Sales totaling $20,000 or less incur no taxes, irrespective of the profit or loss situation.

- **Portfolio Reset:**
  - The weighted average price resets when the entire stock portfolio is sold.
  - New purchases establish a new average price.

### Codebase
The application is written in Python, structured around specific concerns:
- `operation.py`: Defines `Operation`, capturing the action, unit cost, and quantity of a stock operation. It also calculates the total cost as `quantity * unit_cost`.
- `portfolio.py`: Manages the `Portfolio`, tracking stock quantities and updating the weighted average price for each buy or sell operation.
- `tax_calculator.py`: Contains the `TaxCalculator` class, maintaining the loss carry amount, and providing `calculate_tax` to compute taxes based on operations and the portfolio's state.

The workflow is as follows:
- `main.py`: Executes the main application logic in a single call.
- `capital_gains.py`: Houses the `calculate_taxes` function, which parses stdin input into `Operation` objects, updates the portfolio, and calculates taxes for each event.


### Testing
The application was tested, with integration tests based on scenarios from the provided PDF and unit tests for the `Portfolio` and `TaxCalculator` classes.

### Notes
The implementation aims to adhere to SOLID Principles. However, some principles were relaxed for code simplicity:

- `TaxCalculator` could utilize a `TaxCalculationStrategy` pattern. (OCP). Something like this:
```
class TaxCalculationStrategy:
    def calculate_tax(self, operation: Operation, portfolio: Portfolio) -> Decimal:
        raise NotImplementedError

class StandardTaxCalculationStrategy(TaxCalculationStrategy):
    # Implementation of standard tax calculation
```
- `Portfolio` could be designed as an interface or abstract class. (DIP). As in this example:
```
class PortfolioInterface:
    def get_weighted_average_price(self) -> Decimal:
        raise NotImplementedError

    def update(self, operation: Operation) -> None:
        raise NotImplementedError

class Portfolio(PortfolioInterface):
    # Implementation of the PortfolioInterface

```

### Running the Project
The application reads input from a file via `stdin`. It can be run using either plain Python or Docker:

#### Using Python
Compatible with Python >= 3.7.

To execute the main application:
```
python3 main.py < ../test.txt
```
To run all tests, use the command:
```
python3 -m unittest
```

#### Using Docker
When using Docker, a script `capital-gains` simplifies execution.

To run with file input, use the command:
```
./capital-gains < ../test.txt
```
To execute tests, use the command:
```
./capital-gains test
```
The script is basically an alias for `docker-compose run`
