import pandas as pd
from getpass import getpass
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# ---------- EXTRACT ----------
df = pd.read_csv("accidents.csv")
print("Extracted rows and columns:", df.shape)

# ---------- TRANSFORM ----------
df = df.drop(columns=["id"])

df["state_name"] = df["state_name"].str.strip()
df["type_of_accident"] = df["type_of_accident"].str.strip()

for col in ["cases", "injured", "died"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.drop_duplicates()
df = df.dropna(subset=["cases", "injured", "died"])
df[["cases", "injured", "died"]] = df[["cases", "injured", "died"]].astype(int)

df.to_csv("accidents_clean.csv", index=False)
print("Cleaned rows and columns:", df.shape)

# ---------- LOAD ----------
port_text = input("PostgreSQL 18 port (press Enter for 5432): ").strip()
port = int(port_text) if port_text else 5432
password = getpass("postgres password (typing will be hidden): ")
print("Connecting to PostgreSQL on port", port, "...")

url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password=password,
    host="127.0.0.1",
    port=port,
    database="road_accidents",
)
engine = create_engine(url, connect_args={"connect_timeout": 10})

df.to_sql("accidents", engine, if_exists="replace", index=False)

with engine.connect() as conn:
    count = conn.execute(text("SELECT COUNT(*) FROM accidents")).scalar()
print("Rows now in PostgreSQL table 'accidents':", count)