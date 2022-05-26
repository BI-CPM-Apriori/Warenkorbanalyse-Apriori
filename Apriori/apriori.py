from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder
from numpy import signedinteger
import pandas as pd
    
def getResult(ds, minSupport, minConfidence, sortedBy, allowItemsets):

    # Binäre Transaktionstabelle erzeugen 
    te = TransactionEncoder()
    df = pd.DataFrame(te.fit_transform(ds), columns=te.columns_)

    # Apriori-Algorithmus auf binäre Transaktionstabelle anwenden
    frequent_itemsets = apriori(df,min_support=minSupport,use_colnames=True)

    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

    if allowItemsets == True:
        frequent_itemsets = frequent_itemsets[(frequent_itemsets['length'] < 4)]
    else:
         frequent_itemsets = frequent_itemsets[(frequent_itemsets['length'] < 3)]

    # min. Confidence setzen
    rules = association_rules(frequent_itemsets,metric='confidence',min_threshold=minConfidence)

    # Spalten für Assoziationsregeln festlegen
    result = rules[['antecedents','consequents','support','confidence','lift','conviction']]

    # Ergebnisse sortieren
    result.sort_values(by=[sortedBy], ascending=False, inplace=True)


    return result