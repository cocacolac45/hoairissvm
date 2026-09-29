import os
import pyodbc


def get_db_connection():

    driver = os.getenv(
        "DB_DRIVER",
        "ODBC Driver 18 for SQL Server"
    )

    server = os.getenv("DB_SERVER")
    port = os.getenv(
        "DB_PORT",
        "1433"
    )

    database = os.getenv(
        "DB_DATABASE",
        "iris_classification"
    )

    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")

    # =====================================================
    # KIỂM TRA ENVIRONMENT VARIABLES
    # =====================================================

    required = {
        "DB_SERVER": server,
        "DB_USERNAME": username,
        "DB_PASSWORD": password,
    }

    missing = [
        key
        for key, value in required.items()
        if not value
    ]

    if missing:
        raise RuntimeError(
            "Thiếu biến môi trường: "
            + ", ".join(missing)
        )

    # =====================================================
    # SQL SERVER CONNECTION
    # =====================================================

    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
    )

    return pyodbc.connect(
        connection_string
    )
