from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
    
def getResult(ds, supp, threshold):
    te = TransactionEncoder()
    te_ary = te.fit_transform(ds)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df,min_support=supp,use_colnames=True)
    frequent_itemsets.sort_values('support',ascending=False)

    rules = association_rules(frequent_itemsets,metric='lift',min_threshold=threshold)
    rules.sort_values('lift',ascending=False)

    result = rules[['antecedents','consequents','support','confidence','lift','conviction']]
    result.sort_values(by=['confidence'], ascending=False, inplace=True)

    print(result)
    size = int(result.index.size/2)

    result = result.iloc[:size, :]

    return result