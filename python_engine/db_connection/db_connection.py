from sqlalchemy import create_engine
import pandas as pd
def get_engine():
    user = "postgres"
    password = "postgres"
    host = "localhost"
    port = 5432
    db_name = "netflix_db"
    url = f"postgres://{user}:{password}@{host}:{port}/{db_name}"

    return create_engine(url)
if __name__ == "__main__":
    engine = get_engine()
    print("Engine created:", engine)

    df = pd.read_sql("SELECT * FROM netflix_titles", engine)
    df.head(5) #printing the first 5 rows
    print(df[0])