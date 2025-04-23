import psycopg2

# concetarea la baza de date
connection = psycopg2.connect(
    database = "taskdb",
    user =  "postgres",
    password = "parola",
    host = "localhost",
    port = "5432"
)

if __name__ == "__main__":
    #  partea folosita pentru creearea tabelelor

    cur = connection.cursor()

    # tabelul users cu relatiile:
    #  - one to many( users - tasks)
    #  - one to many( users - comments)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            nume VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            parola VARCHAR(100) NOT NULL
        )
        '''
    )

    # tabelul tasks cu relatiile:
    #  - one to many( users - tasks)
    #  - one to many( tasks - tasks)  - prin parent_id
    #  - one to many( tasks - comments)
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks(
            id SERIAL PRIMARY KEY,
            titlu VARCHAR(100) NOT NULL,
            descriere TEXT,
            due_date TIMESTAMP,
            responsabil INTEGER REFERENCES users(id) ON DELETE SET NULL,
            parent_id INTEGER REFERENCES tasks(id) ON DELETE CASCADE
        )
        '''
    )

    # tabelul comments cu relatiile:
    #  - one to many( users - comments)
    #  - one to many( tasks - comments)
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS comments(
            id SERIAL PRIMARY KEY,
            task_id INTEGER REFERENCES tasks(id) ON DELETE CASCADE,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            comment TEXT NOT NULL
        )
        """
    )

    connection.commit()

    cur.close()
    connection.close()