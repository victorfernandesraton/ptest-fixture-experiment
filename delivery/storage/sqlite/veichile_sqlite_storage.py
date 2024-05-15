from datetime import datetime
from sqlite3 import Connection

from delivery.domain.models import VeichileModel, VeichileStatus
from delivery.repository import VeichileRepository


class VeichileStorageSqlite(VeichileRepository):
    def __init__(self, conn: Connection, table_name: str = "veichile"):
        self.conn = conn
        self.table_name = table_name

    def create_table(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY,
                    plate TEXT NOT NULL UNIQUE,
                    status INT NOT NULL DEFAULT 1,
                    created_at NUMERIC,
                    updated_at NUMERIC
                )
                """
            )

    def drop_table(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                f"""
                DROP TABLE {self.table_name}
                """
            )

    def create_veichile(self, veichile: VeichileModel) -> VeichileModel:
        created_at = datetime.now().timestamp()
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                    INSERT INTO veichile (plate, status, created_at, updated_at)
                    VALUES (?, ?, ?, ?)
                """,
                (veichile.plate, veichile.status.value, created_at, created_at),
            )
            veichile_id = cursor.lastrowid
            return VeichileModel(
                id=veichile_id,
                plate=veichile.plate,
                status=veichile.status,
                created_at=datetime.fromtimestamp(created_at),
                updated_at=datetime.fromtimestamp(created_at),
            )

    def get_veichile_by_id(self, veichile_id: int) -> VeichileModel | None:
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM veichile WHERE id = ?", (veichile_id,))
            if cursor.rowcount == 0:
                return None
            row = cursor.fetchone()
            if not row:
                return None
            print(row)
            return VeichileModel(
                id=row[0],
                plate=row[1],
                status=VeichileStatus(row[2]),
                created_at=datetime.fromtimestamp(row[3]),
                updated_at=datetime.fromtimestamp(row[4]),
            )

    def update_veichile_status(
        self, veichile_id: int, status: VeichileStatus
    ) -> VeichileModel | None:

        old_veichile = self.get_veichile_by_id(veichile_id)
        if not old_veichile:
            return None

        now = datetime.now().timestamp()
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE veichile
                SET status = ?, updated_at = ?
                WHERE id = ?
            """,
                (status.value, now, veichile_id),
            )
            if cursor.rowcount == 0:
                return None

            update_veichile = self.get_veichile_by_id(veichile_id)
            return update_veichile
