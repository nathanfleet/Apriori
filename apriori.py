import sys
import math
from itertools import combinations

def apriori():
    if len(sys.argv) != 3:
        print("Usage: python myapriori.py filename minsup")
        sys.exit(1)

    filename = sys.argv[1]
    minsup_level = float(sys.argv[2]) / 100.0

    transactions = []
    items = set()

    with open(filename, 'r') as f:
        for line in f:
            transaction = set(line.strip().split())
            transactions.append(transaction)
            items.update(transaction)

    N = len(transactions)
    minsup_count = math.ceil(minsup_level * N)

    # Generate frequent 1-itemsets
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    L1 = []
    for item, count in item_counts.items():
        if count >= minsup_count:
            L1.append(frozenset([item]))

    freq_itemsets = []
    freq_itemsets.extend(L1)

    # Iteratively generate frequent itemsets
    k = 2
    Lkminus1 = L1
    while Lkminus1:
        # Generate candidates Ck
        Ck = []
        Lkminus1_list = list(Lkminus1)
        Lkminus1_set = set(Lkminus1)
        for i in range(len(Lkminus1_list)):
            for j in range(i+1, len(Lkminus1_list)):
                l1 = list(Lkminus1_list[i])
                l2 = list(Lkminus1_list[j])
                l1.sort()
                l2.sort()
                if l1[:-1] == l2[:-1]:
                    candidate = Lkminus1_list[i] | Lkminus1_list[j]
                    # Prune candidates whose subsets are not frequent
                    subsets = list(combinations(candidate, k-1))
                    if all(frozenset(subset) in Lkminus1_set for subset in subsets):
                        Ck.append(candidate)

        # Count supports
        candidate_counts = {}
        for transaction in transactions:
            for candidate in Ck:
                if candidate.issubset(transaction):
                    candidate_counts[candidate] = candidate_counts.get(candidate, 0) + 1

        # Generate Lk
        Lk = []
        for candidate, count in candidate_counts.items():
            if count >= minsup_count:
                Lk.append(candidate)

        freq_itemsets.extend(Lk)
        Lkminus1 = Lk
        k += 1

    # Output frequent itemsets
    for itemset in freq_itemsets:
        items = list(itemset)
        items.sort()
        print(' '.join(items))

if __name__ == '__main__':
    apriori()