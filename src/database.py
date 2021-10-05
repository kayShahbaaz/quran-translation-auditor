# src/database.py
# ─────────────────────────────────────────────────────────────────────────────
# Quranic Cross-Lingual Translation Auditor
# Database engine — SQLite schema, seeding, queries
# ─────────────────────────────────────────────────────────────────────────────

import sqlite3
import json
import os
import sys

# Allow imports from src/ when called directly
sys.path.insert(0, os.path.dirname(__file__))
from mock_data import AYAT_DATA

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")


def get_connection():
    """Return a new SQLite connection with row factory enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialise the ayat table schema if it does not exist."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ayat (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            ayah_key         TEXT    NOT NULL UNIQUE,
            surah_name       TEXT    NOT NULL,
            arabic           TEXT    NOT NULL,
            roots            TEXT    NOT NULL,
            trans_sahih      TEXT    NOT NULL,
            trans_haleem     TEXT    NOT NULL,
            trans_khattab    TEXT    NOT NULL,
            trans_soliman    TEXT    NOT NULL,
            divergence_score REAL    DEFAULT 0.0
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Schema initialised.")


def seed_db():
    """Seed database from mock_data.py. Idempotent via INSERT OR IGNORE."""
    conn = get_connection()
    cursor = conn.cursor()
    for entry in AYAT_DATA:
        cursor.execute("""
            INSERT OR IGNORE INTO ayat
                (ayah_key, surah_name, arabic, roots,
                 trans_sahih, trans_haleem, trans_khattab, trans_soliman,
                 divergence_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            entry["ayah_key"],
            entry["surah_name"],
            entry["arabic"],
            json.dumps(entry["roots"], ensure_ascii=False),
            entry["trans_sahih"],
            entry["trans_haleem"],
            entry["trans_khattab"],
            entry["trans_soliman"],
            0.0
        ))
    conn.commit()
    conn.close()
    print(f"[DB] Seeded {len(AYAT_DATA)} Ayat records.")


def fetch_all_ayat():
    """Return all Ayat rows ordered by id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ayat ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_divergence_score(ayah_key, score):
    """Persist computed divergence score for a given Ayah."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE ayat SET divergence_score = ? WHERE ayah_key = ?",
        (round(score, 4), ayah_key)
    )
    conn.commit()
    conn.close()


def reset_db():
    """Drop and recreate the database — useful for clean test runs."""
    conn = get_connection()
    conn.cursor().execute("DROP TABLE IF EXISTS ayat")
    conn.commit()
    conn.close()
    print("[DB] Database reset.")
    init_db()
    seed_db()


if __name__ == "__main__":
    print("[DB] Running standalone setup...")
    init_db()
    seed_db()
    rows = fetch_all_ayat()
    print(f"[DB] Total records: {len(rows)}")
    for row in rows:
        print(f"  {row['ayah_key']:>7}  {row['surah_name']:<14}  score={row['divergence_score']}")
