# Run SQL queries saved in the sql folder
# and output the results in the terminal

import sqlite3

# Main function used in this script
def run_sql_query(sql_query_file, description):
    """
    Retrieve SQL query statement from file.
    Then runs that SQL query on the database.
    The results are printed to the terminal
    with a description of the results provided
    beforehand.

    Parameters
    ----------
    sql_query_file: string
        The location of the file where the SQl query
        statement is stored

    description: string
        Description of the results that shows before the results
        on the terminal
    """
    with open(sql_query_file, "r") as f:
        sql_query = f.read()
    cur.execute(sql_query)
    rows = cur.fetchall()
    print(description)
    for row in rows:
        print(row)

# Create connection to SQL database
db = "output/results.db"
conn = sqlite3.connect(db)
cur = conn.cursor()

# Results:

