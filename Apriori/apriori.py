from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder
from numpy import signedinteger
import pandas as pd
    
def getResult(ds, minSupport, minConfidence, sortedBy, singleAnalyse):
    te = TransactionEncoder()
    te_ary = te.fit_transform(ds)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df,min_support=minSupport,use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

    if singleAnalyse == True:
        frequent_itemsets = frequent_itemsets[(frequent_itemsets['length'] < 3)]
    else:
         frequent_itemsets = frequent_itemsets[(frequent_itemsets['length'] < 4)]

    

    rules = association_rules(frequent_itemsets,metric='confidence',min_threshold=minConfidence)

    result = rules[['antecedents','consequents','support','confidence','lift','conviction']]
    result.sort_values(by=[sortedBy], ascending=False, inplace=True)

    
   # size = int(result.index.size/2)

    #result = result.iloc[:size, :]
    #print(result)

    return result