from data.abstract.service import Service
from lib.database import connect_to_database


class RoleService(Service):
    def __init__(self):
        pass

    def __repr__(self):
        return "".format()

    def open_connection(self):
        connection = connect_to_database()
        cursor = connection.cursor()
        return connection, cursor

    def create(self, name):
        conn, cur = self.open_connection()
        cur.execute('INSERT INTO "role" (name) VALUES (%s)', (name,))
        conn.commit()
        cur.close()
        conn.close()

    def get(self):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "role"')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        result = []
        for row in rows:
            user_data = {
                "id": row[0],
                "name": row[1],
            }
            result.append(user_data)
        try:
            return result
        except:
            return None

    def get_by_id(self, id: str):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "role" WHERE id=%s', (id,))
        rows = cur.fetchone()
        print(rows)
        cur.close()
        conn.close()
        return {
            "id": rows[0],
            "name": rows[1],
        }

    def get_by_name(self, name: str):
        conn, cur = self.open_connection()
        cur.execute('SELECT * FROM "role" WHERE name=%s', (name,))
        rows = cur.fetchone()
        cur.close()
        conn.close()
        try:
            return {
                "id": rows[0],
                "name": rows[-1],
            }
        except:
            return None

    def update(self, name: str):
        conn, cur = self.open_connection()
        cur.execute('UPDATE "role" SET name=%s WHERE id=%s', (name, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, name: str):
        conn, cur = self.open_connection()
        cur.execute('DELETE FROM "role" WHERE name=%s', (name,))
        conn.commit()
        cur.close()
        conn.close()
