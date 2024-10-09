# Apriori
Apriori algorithm implementation

## Instructions for running
python apriori.py [input file] [minimum support level]

## Detailed Psuedocode
```Python
NECESSARY DATA STRUCTURES:
transactions (list of sets)
items (set of unique items)

BEGIN
  # Read command-line inputs: a file and minimum support level

  # Read transactions from the file and gather all unique items
  
  # Calculate the minimum support count based on the given level

  # Find all frequent 1-itemsets by counting item occurrences in transactions

  # Initialize frequent itemsets with the 1-itemsets

  k = 2
  WHILE there are frequent (k-1)-itemsets DO
    # Generate candidate k-itemsets from (k-1)-itemsets

    # Count how many transactions contain each candidate k-itemset

    # Filter out candidates that don’t meet the minimum support count

    # Add the frequent k-itemsets to the list of frequent itemsets

    k = k + 1
  END WHILE

  # Output all frequent itemsets
END

FUNCTION candidate_gen(Lk_minus_1, k)
  # Combine (k-1)-itemsets to form candidate k-itemsets
  
  # Prune candidates by removing those whose subsets are not frequent

  RETURN the remaining candidate itemsets
END FUNCTION
```
