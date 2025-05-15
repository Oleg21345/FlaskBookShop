from src.flask_engine.app import app, socketio
from src.database.create_table import create_table, drop_tabl
from src.mongodatabase.config_mongo import init_db


def main():
    init_db()
    drop_tabl()

    create_table()
    socketio.run(app, debug=True)

if __name__ == "__main__":
    main()