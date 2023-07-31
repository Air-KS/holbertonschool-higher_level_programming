#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Se connecter à la base de données MySQL
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user=username, passwd=password, db=database)

    # Créer un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécuter une requête SELECT sur la table des états
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupérer et afficher les résultats
    results = cursor.fetchall()
    for row in results:
        state_id = row[0]
        state_name = row[1]
        print("{}: {}".format(state_id, state_name))

    # Fermer le curseur et la connexion à la base de données
    cursor.close()
    db.close()
