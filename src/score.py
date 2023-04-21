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


def count():
    nb_id = curseur.execute(f"SELECT COUNT(*) FROM table_score;")
    nb = []
    for enregistrement in nb_id:
        nb.append(enregistrement)
    return nb[0][0]


def score_min_max(min_max):
    if min_max == 1:
        m_score = curseur.execute(f"SELECT MIN(score) FROM table_score;")
    else:
        m_score = curseur.execute(f"SELECT MAX(score) FROM table_score;")
    score = []
    for enregistrement in m_score:
        score.append(enregistrement)
    return score[0][0]


def delete(new_score):
    curseur.execute(f"DELETE table_score WHERE score >= new_score and ;")


def save_score(point):
    if count() < 10 :
        curseur.execute(f"INSERT INTO table_score VALUES ({max_id()}+1, {point}, {datetime.datetime.today().replace(microsecond = 0)});")
        bdd.commit()
