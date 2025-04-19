from db import connection


class Comment:
    @staticmethod
    def get_comments():
        cur = connection.cursor()
        cur.execute("SELECT * FROM comments")
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