from db import connection


class Comment:
    @staticmethod
    def get_comments(task_id=None, user_id=None, comment=None):
        if task_id is None and user_id is None:
            cur = connection.cursor()
            cur.execute("SELECT * FROM comments")
            comments = cur.fetchall()
            cur.close()
            return comments
        else:
            cur = connection.cursor()
            query = "SELECT * FROM comments  "
            params = []
            conditions = []
            if task_id:
                conditions.append( "task_id = %s ")
                params.append(task_id)
            
            if user_id:
                conditions.append("user_id = %s")
                params.append(user_id)
            if comment:
                conditions.append("LOWER(comment) LIKE %s")
                params.append(f"%{comment.lower()}%")
            
            if conditions:
                query += " WHERE " + " AND ".join(conditions)


            cur.execute(query, tuple(params))
            comments = cur.fetchall()
            cur.close()
            return comments
    
    @staticmethod
    def get_comment(comment_id):
        cur = connection.cursor()
        cur.execute("SELECT * FROM comments WHERE id = %s", (comment_id,))
        comment = cur.fetchone()
        cur.close()
        return comment
    
    @staticmethod
    def create_comment(task_id, user_id, comment):
        if task_id is None or user_id is None or comment is None:
            raise ValueError("Task ID, User ID, and comment cannot be None")
        cur = connection.cursor()
        cur.execute(
            """
            INSERT INTO comments (task_id, user_id, comment) VALUES (%s, %s, %s)
            """, (task_id, user_id, comment)
        )
        connection.commit()
        cur.close()

    @staticmethod
    def delete_comment(comment_id):
        cur = connection.cursor()
        cur.execute("DELETE FROM comments WHERE id = %s", (comment_id,))
        connection.commit()
        cur.close()