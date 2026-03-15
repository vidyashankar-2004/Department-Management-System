import sqlite3, os, sys
p = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
if not os.path.exists(p):
    print('MISSING_DB', p)
    sys.exit(0)
conn = sqlite3.connect(p)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print('TABLES:', tables)
for tn in tables:
    if 'department' in tn.lower():
        print('\nSCHEMA for', tn)
        cur.execute(f"PRAGMA table_info('{tn}')")
        for r in cur.fetchall():
            print(r)
conn.close()
