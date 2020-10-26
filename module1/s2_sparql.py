<<<<<<< HEAD
"""Query Wikidata for Belgian politicians"""

import argparse
from datetime import datetime as dt

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?monument ?monumentLabel ?monumentAddress ?location WHERE {
        ?monument   wdt:P31/wdt:P279 wd:Q4989906.
        ?monument   wdt:P131 wd:Q239.
        ?monument   wdt:P6375 ?MonumentAddress.
        ?monument   wdt:P625 ?location.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    }
    ORDER BY ?monumentLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Monuments from Brussels found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n monuments (default=10)"""
    if name_filter:
        rows = [row for row in rows if name_filter in row['monumentLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            monumentLabel = row['monumentLabel']['value']
        except ValueError:
            monumentLabel = "===="
        try:
            monumentAddress = row['monumentaddress']['value']
        except ValueError: 
            monumentAddress = "===="
        try:
            loc = row['location']['value']
        except ValueError: 
            monumentAddress = "===="
        print(monumentLabel + "/ " + monumentAddress + "/ "  + loc)

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)
=======
"""Query Wikidata for Belgian politicians"""

import argparse
from datetime import datetime as dt

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?monument ?monumentLabel ?monumentAddress ?location WHERE {
        ?Monument   wdt:P31/wdt:P279 wd:Q4989906.
        ?Monument   wdt:P131 wd:Q239.
        ?Monument   wdt:P6375 ?MonumentAddress.
        ?Monument   wdt:P625 ?location.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    }
    ORDER BY ?monumentLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Monuments from Brussels found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n monuments (default=10)"""
    if name_filter:
        rows = [row for row in rows if name_filter in row['monumentLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            monumentLabel = row['monumentLabel']['value']
        except ValueError:
            monumentLabel = "===="
        try:
            monumentAddress = row['monumentaddress']['value']
        except ValueError: 
            monumentAddress = "===="
        try:
            loc = row['location']['value']
        except ValueError: 
            monumentAddress = "===="
        print(monumentLabel + "/ " + monumentAddress + "/ "  + loc)

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)
>>>>>>> e871ace8fd3b5dc8ba2d2f83a64a253af74236f8
