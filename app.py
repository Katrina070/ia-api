
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/get-active-url")
def get_active_url():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        cur = conn.cursor()
        cur.execute("SELECT url FROM urls WHERE status = 'active' LIMIT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            return jsonify({"url": result[0]})
        return jsonify({"error": "No active URL found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
