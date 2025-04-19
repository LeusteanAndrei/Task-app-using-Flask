from db import connection



class Task:
    @staticmethod
    def get_tasks(titlu=None, descriere=None, responsabil=None):
        if titlu is None and descriere is None:
            cur = connection.cursor()
            cur.execute("SELECT * FROM tasks")
            tasks = cur.fetchall()
            cur.close()
            return tasks
        else:
            cur = connection.cursor()
            query = "SELECT * FROM tasks "
            params = []
            first = True
            conditions = []
            
            if titlu:
                conditions.append("LOWER(titlu) LIKE %s")
                params.append(f"%{titlu.lower()}%")
            if descriere:
                conditions.append("LOWER(descriere) LIKE %s")
                params.append(f"%{descriere.lower()}%")
            if responsabil:
                conditions.append("responsabil = %s")
                params.append(responsabil)
            
            if conditions:
                query += " WHERE " + " AND ".join(conditions)

            cur.execute(query, tuple(params))   
            tasks = cur.fetchall()
            cur.close()
            return tasks            
    
    @staticmethod
    def get_task(task_id):
        cur = connection.cursor()
        cur.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cur.fetchone()
        cur.close()
        return task
    

    @staticmethod
    def create_task(titlu, descriere = None, due_date = None, responsabil = None, parent_id = None):
        if titlu is None:
            raise ValueError("Titlu cannot be None")
        cur = connection.cursor()
        cur.execute(
            """
            INSERT INTO tasks (titlu, descriere, due_date, responsabil, parent_id) VALUES (%s, %s, %s, %s, %s)
            """, (titlu, descriere, due_date, responsabil, parent_id)
        )
        connection.commit()
        cur.close()

    @staticmethod
    def delete_task(task_id):
        cur = connection.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        connection.commit()
        cur.close()

    def update_task(task_id, titlu=None, descriere=None, due_date=None, responsabil=None, parent_id=None):
        cur = connection.cursor()
        query = "UPDATE tasks SET "
        params = []
        if titlu:
            query += "titlu = %s,"
            params.append(titlu)
        if descriere:
            query += "descriere = %s,"
            params.append(descriere)
        if due_date:
            query += "due_date = %s,"
            params.append(due_date)
        if responsabil:
            query += "responsabil = %s,"
            params.append(responsabil)
        if parent_id:
            query += "parent_id = %s,"
            params.append(parent_id)
        
        query = query.rstrip(',') + " WHERE id = %s"
        params.append(task_id)

        cur.execute(query, tuple(params))
        connection.commit()
        cur.close()

    @staticmethod
    def get_task_by_title(titlu):
        cur = connection.cursor()
        cur.execute("SELECT * FROM tasks WHERE titlu = %s", (titlu,))
        task = cur.fetchone()
        cur.close()
        return task