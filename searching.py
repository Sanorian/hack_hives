import psycopg2
from nltk.stem.snowball import SnowballStemmer

class Searcher:
    def __init__(self):
        self.stemmer = SnowballStemmer("russian")

    def create_query(self, question: str)->str:
        query = """
            BEGIN;
            ALTER TABLE Video
            ADD Rating INTEGER SET DEFAULT 0;
        """
        question_words = question.split()
        words_combinations = question_words + [self.stemmer.stem(word) for word in question.split()]

        for i in range(0, len(question_words)-1):
            word = question_words[i]
            for j in range(i+1, len(question_words)-1):
                word+=" "+question_words[j]
                words_combinations.append(word)

        for comb in words_combinations:
            query+= f"""
                UPDATE Video SET Rating = Rating + {2**len(comb.split())} WHERE Description LIKE '%{comb}%';
                UPDATE Video SET Rating = Rating + {2**(2*len(comb.split()))} WHERE Image LIKE '%{comb}%';
            """
        query+="UPDATE Video SET Rating = Rating * 1.5 WHERE Upload_date between (now() - '1 week'::interval) and now();"
        query+="SELECT * FROM Video WHERE Rating != 0 ORDER BY DESC Rating;"
        query += "ROLLBACK;"
        return query

    def execute_search_query(query: str)->list[str]:
        with psycopg2.connect(dbname='videos', user='videos_user', password='videos_password', host='db') as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
