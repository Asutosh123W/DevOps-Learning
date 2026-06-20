from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():

    container_name = os.getenv("CONTAINER_NAME")

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]

        cur.close()
        conn.close()

        return f"""
        <h2>Response From: {container_name}</h2>
        <p>{version}</p>
        """

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

