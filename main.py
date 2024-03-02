from config import config, db_name
from connector.api_connect import hh_get_resource
from database.create_database import (create_database, create_table,
                                      save_data_to_database)
from utils import user_interaction


def main() -> None:
    data = hh_get_resource()

    params = config()

    create_database(db_name, params)
    create_table(db_name, params)
    save_data_to_database(data, db_name, params)

    user_interaction()


if __name__ == "__main__":
    main()
