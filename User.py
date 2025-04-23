from db import connection

#  metode pentru tabelul users

class User:

    #  2 metode pentru a obtine utilizatorii, acestia pot fi filtrati dupa nume si email
    @staticmethod
    def get_users(nume=None, email=None):
        if nume is None and email is None:
            cur = connection.cursor()
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            cur.close()
            return users
        else:
            cur = connection.cursor()
            query = "SELECT * FROM users "
            params = []
            conditions = []

            if nume:
                conditions.append("nume ILIKE %s")
                params.append(f"%{nume}%")
            if email:
                conditions.append("email ILIKE %s")
                params.append(f"%{email}%")

            if conditions:
                query += " WHERE " + " AND ".join(conditions)

            cur.execute(query, tuple(params))
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
    def create_user(nume, email, parola):

        if nume is None or email is None or parola is None:
            raise ValueError("Numr, email, and parola cannot be None")

        cur = connection.cursor()
        cur.execute(
            """
            INSERT INTO users (nume, email, parola) VALUES (%s, %s, %s)
            """, (nume, email, parola)
        )
        connection.commit()
        cur.close()
    
    @staticmethod
    def delete_user(user_id):
        cur = connection.cursor()
        # stergerea task-urilor corespunzatoare:

        
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()
        cur.close()