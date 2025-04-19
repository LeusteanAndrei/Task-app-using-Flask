from db import connection

class User:
    @staticmethod
    def get_users():
        cur = connection.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        return users
    
    @staticmethod   
    def get_user(user_id):
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        return user

    @staticmethod
    def create_user(username, email, password):

        if username is None or email is None or password is None:
            raise ValueError("Username, email, and parola cannot be None")

        cur = connection.cursor()
        cur.execute(
            """
            INSERT INTO users (nume, email, parola) VALUES (%s, %s, %s)
            """, (username, email, password)
        )
        connection.commit()
        cur.close()
    
    @staticmethod
    def delete_user(user_id):
        cur = connection.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        cur.close()