import sqlite3
import datetime


# connect the base of data
bdd = sqlite3.connect('src/SCORE.db')
curseur = bdd.cursor()

def max_nb_try():
    """give the number of try"""
    max_nb_try = curseur.execute(f"SELECT MAX(nb_try) FROM table_score;")
    nb_try = []
    for enregistrement in max_nb_try:
        nb_try.append(enregistrement)
    return nb_try[0][0]


def count():
    """count the number of save"""
    nb_try = curseur.execute(f"SELECT COUNT(*) FROM table_score;")
    nb = []
    for enregistrement in nb_try:
        nb.append(enregistrement)
    return nb[0][0]


def score_min_max(min_max):
    """give the score min or max"""
    if min_max == 1:
        m_score = curseur.execute(f"SELECT MIN(score) FROM table_score;")
    else:
        m_score = curseur.execute(f"SELECT MAX(score) FROM table_score;")
    score = []
    for enregistrement in m_score:
        score.append(enregistrement)
    return score[0][0]


def save_score(new_score):
    """management the sql, to save a score"""
    score_min = score_min_max(1)
    if new_score >= score_min:
            if count() >= 10:
                curseur.execute(f"DELETE FROM table_score WHERE score = {score_min};")
            nb_try = max_nb_try() + 1
            date = datetime.datetime.today().replace(microsecond = 0)
            curseur.execute(f"INSERT INTO table_score VALUES ({nb_try},{new_score},'{date}');")
            bdd.commit()
