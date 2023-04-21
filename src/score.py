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


def save_score(new_score):
    score_min = score_min_max(1)
    if new_score >= score_min and count() >= 10:
        curseur.execute(f"DELETE FROM table_score WHERE score = {score_min};")
    id = max_id() + 1
    date = datetime.datetime.today().replace(microsecond = 0)
    print(date)
    print(id)
    print(score_min)
    curseur.execute("INSERT INTO table_score VALUES (",id,",",new_score,",",date,");")
    bdd.commit()
