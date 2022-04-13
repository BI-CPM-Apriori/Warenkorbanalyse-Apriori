from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
    
def getResult(ds, param):
    te = TransactionEncoder()
    te_ary = te.fit_transform(ds)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    if param == "1":
        supp = 0.025
        threshold = 10
    elif param == "2":
        supp = 0.015
        #supp = 0.0112
        threshold = 16

    frequent_itemsets = apriori(df,min_support=supp,use_colnames=True)
    frequent_itemsets.sort_values('support',ascending=False)

    rules = association_rules(frequent_itemsets,metric='lift',min_threshold=threshold)
    rules.sort_values('lift',ascending=False)

    result = rules[['antecedents','consequents','support','confidence','lift','conviction']]
    result.sort_values('confidence',ascending=False)

    return result