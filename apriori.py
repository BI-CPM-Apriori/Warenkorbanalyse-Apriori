from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
    
def getResult(ds):
    te = TransactionEncoder()
    te_ary = te.fit(ds).transform(ds)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    frequent_itemsets = apriori(df,min_support=0.025,use_colnames=True)
    frequent_itemsets.sort_values('support',ascending=False)
    rules = association_rules(frequent_itemsets,metric='lift',min_threshold=10)
    rules.sort_values('lift',ascending=False)

    result = rules[['antecedents','consequents','support','confidence','lift']]

    result.sort_values('confidence',ascending=False)

    return result