"""Filter out stopwords for word cloud"""

import sys
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

sw = stopwords.words("french")
sw += ["les", "recette","plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "ville","octobre","service","bruxelles","assistance publique",
       "assistance","publique","commission","conseil","communal","Bruxelles","Octobre","Assistance","demande",
       "rue","franc","commune","conseil","mesdames","messieurs","publique","Bruxelles","Rue","rue","service","services","Service","Services","Francs","Recette","recette","francs","franc"]
sw = set(sw)


def filtering(year, folder=None):
    if folder is None:
        input_path = f"../data/{year}.txt"
        output_path = f"../data/{year}_keywords.txt"
    else:
        input_path = f"{folder}/{year}.txt"
        output_path = f"{folder}/{year}_keywords.txt"
    output = open(output_path, "w", encoding='utf-8')
    with open(input_path, encoding='utf-8') as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)
    return f'Output has been written in {output_path}!'


if __name__ == '__main__':
    data_path = sys.argv[1]
    chosen_year = sys.argv[2]
    filtering(data_path, chosen_year)
