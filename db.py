import psycopg2

connection = psycopg2.connect(
    database = "taskdb",
    user =  "postgres",
    password = "parola",
    host = "localhost",
    port = "5432"
)

if __name__ == "__main__":
    cur = connection.cursor()


    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            nume VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            parola VARCHAR(100) NOT NULL
        )
        '''
    )

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks(
            id SERIAL PRIMARY KEY,
            titlu VARCHAR(100) NOT NULL,
            descriere TEXT,
            due_date TIMESTAMP,
            responsabil INTEGER REFERENCES users(id),
            parent_id INTEGER REFERENCES tasks(id)
        )
        '''
    )

    # cur.execute(
    #     """
    #     INSERT INTO users (nume, email, parola) VALUES (%s, %s, %s)
    #     """, ('administrator', 'admina@test.com', 'admin123')
    # )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS comments(
            id SERIAL PRIMARY KEY,
            task_id INTEGER REFERENCES tasks(id),
            user_id INTEGER REFERENCES users(id),
            comment TEXT NOT NULL
        )
        """
    )


    connection.commit()

    cur.close()
    connection.close()