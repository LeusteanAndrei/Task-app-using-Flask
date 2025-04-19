from db import connection



class Task:
    @staticmethod
    def get_tasks():
        cur = connection.cursor()
        cur.execute("SELECT * FROM tasks")
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

    