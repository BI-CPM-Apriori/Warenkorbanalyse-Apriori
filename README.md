# BI-CPM-APriori-Front-Backend

Die Anwendung setzt im Backend eine Warenkorbanalyse mit dem Apriori-Algorithmus auf Basis der Daten der MS AdventureWorks2019-Datenbank um.
Im Frontend können unterschiedliche Parameter (Quartal, Region, minSupport, minConfidence) zur Analyse gesetzt werden und die Metrics der Ergebnis-Assoziationsregeln ausgewertet werden.

Zur Ordnerstruktur:
- Apriori:  

            - dataset.py: enthält die SELECTs auf die Datenbank + Erstellung der Arrays über Bestellungen
            
            - apriori.py: enthält die Erstellung der binären Transaktionstabelle + Anwendung des Apriori-Algorithmus

- Database:  

            - dbConnection.py: enthält die Prozedur zum Aufbau der Datenbankverbindung
            
            - read.py: enthält alle SQL-SELECT-Statements

- Skripts:  

            - ProductPhotos: enthält die von uns ergänzten ProductPhotos
            
            - INSERT_PHOTOS.sql: Fügt neue Photos ein
            
            - UPDATE_PHOTOID.sql: Ordnet bestehenden Produkten die neuen Bilder zu

- images:  

            - enthält die Image-Ressourcen zur Visualisierung im Frontend

- ui:  

            - enthält die PySide6-Elemente des Frontends
            
