# Apriori
Apriori algorithm implementation

## Instructions for running
python apriori.py [input file] [minimum support level]

## Detailed Psuedocode
```Python
BEGIN
  # Read command-line arguments
  IF number of arguments != 2 THEN
    PRINT "Usage: myapriori filename minsup"
    EXIT
  END IF

  filename ← argv[1]
  minsup_level ← float(argv[2]) / 100.0

  # Read transactions and collect all items
  transactions ← []
  items ← ∅
  OPEN file(filename) AS file
    FOR each line IN file DO
      transaction ← SET(line.strip().split())
      transactions.append(transaction)
      items ← items ∪ transaction
    END FOR
  CLOSE file

  N ← length(transactions)
  minsup_count ← ceil(minsup_level × N)

  # Generate frequent 1-itemsets (L1)
  item_counts ← {}
  FOR each transaction IN transactions DO
    FOR each item IN transaction DO
      item_counts[item] ← item_counts.get(item, 0) + 1
    END FOR
  END FOR

  L1 ← ∅
  FOR each item, count IN item_counts DO
    IF count ≥ minsup_count THEN
      L1 ← L1 ∪ {item}
    END IF
  END FOR

  freq_itemsets ← L1
  k ← 2
  Lk_minus_1 ← L1

  # Generate frequent itemsets
  WHILE Lk_minus_1 ≠ ∅ DO
    # Generate candidate itemsets Ck
    Ck ← candidate_gen(Lk_minus_1, k)

    # Count supports
    candidate_counts ← {}
    FOR each transaction IN transactions DO
      FOR each candidate IN Ck DO
        IF candidate ⊆ transaction THEN
          candidate_counts[candidate] ← candidate_counts.get(candidate, 0) + 1
        END IF
      END FOR
    END FOR

    # Generate frequent itemsets Lk
    Lk ← ∅
    FOR each candidate, count IN candidate_counts DO
      IF count ≥ minsup_count THEN
        Lk ← Lk ∪ {candidate}
      END IF
    END FOR

    freq_itemsets ← freq_itemsets ∪ Lk
    Lk_minus_1 ← Lk
    k ← k + 1
  END WHILE

  # Output frequent itemsets
  FOR each itemset IN freq_itemsets DO
    PRINT sorted(itemset)
  END FOR
END

FUNCTION candidate_gen(Lk_minus_1, k)
  Ck ← ∅
  Lk_minus_1_list ← sorted list of elements in Lk_minus_1
  FOR i FROM 0 TO length(Lk_minus_1_list) - 1 DO
    FOR j FROM i + 1 TO length(Lk_minus_1_list) - 1 DO
      itemset1 ← Lk_minus_1_list[i]
      itemset2 ← Lk_minus_1_list[j]
      IF first (k - 2) items of itemset1 = first (k - 2) items of itemset2 THEN
        candidate ← itemset1 ∪ itemset2
        # Prune candidates whose subsets are not frequent
        all_subsets_frequent ← TRUE
        FOR each subset IN combinations(candidate, k - 1) DO
          IF subset ∉ Lk_minus_1 THEN
            all_subsets_frequent ← FALSE
            BREAK
          END IF
        END FOR
        IF all_subsets_frequent THEN
          Ck ← Ck ∪ {candidate}
        END IF
      END IF
    END FOR
  END FOR
  RETURN Ck
END FUNCTION
```
