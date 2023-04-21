import sqlite3
import datetime


# Connexion à la base de données Livres
bdd = sqlite3.connect('src/SCORE.db')
curseur = bdd.cursor()

def max_id():
    max_id = curseur.execute(f"SELECT MAX(id) FROM table_score;")
    id = []
    for enregistrement in max_id:
        id.append(enregistrement)
    return id[0][0]


def score_min(min_max):
    if min_max == 1:
        m_score = curseur.execute(f"SELECT MIN(score) FROM table_score;")
    else:
        m_score = curseur.execute(f"SELECT MAX(score) FROM table_score;")
    score = []
    for enregistrement in m_score:
        score.append(enregistrement)
    return score[0][0]


def save_score(point):
    curseur.execute(f"INSERT INTO table_score VALUES ({max_id()}+1, {point}, {datetime.datetime.today().replace(microsecond = 0)});")
    bdd.commit()    # Validation la requete (les modifications)

print(score_min())