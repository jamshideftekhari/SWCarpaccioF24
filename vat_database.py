import sqlite3

def create_database():
    """
    Create an SQLite database and a table for storing VAT values.

    Returns:
    - connection: SQLite database connection.
    - cursor: SQLite database cursor.
    """
    connection = sqlite3.connect("vat_database.db")
    cursor = connection.cursor()

    # Create a table for VAT values if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS vat_values
                      (country_code TEXT PRIMARY KEY, vat_rate REAL)''')

    return connection, cursor

def add_vat_to_database(connection, cursor, country_code, vat_rate):
    """
    Add VAT values to the SQLite database.

    Parameters:
    - connection: SQLite database connection.
    - cursor: SQLite database cursor.
    - country_code: The country code.
    - vat_rate: The VAT rate for the specified country in Europe.
    """
    cursor.execute("INSERT OR REPLACE INTO vat_values (country_code, vat_rate) VALUES (?, ?)",
                   (country_code, vat_rate))
    connection.commit()

def get_vat_from_database(cursor, country_code):
    """
    Get VAT values from the SQLite database.

    Parameters:
    - cursor: SQLite database cursor.
    - country_code: The country code.

    Returns:
    - vat_rate: The VAT rate for the specified country in Europe.
    """
    cursor.execute("SELECT vat_rate FROM vat_values WHERE country_code = ?", (country_code,))
    result = cursor.fetchone()
    return result[0] if result else None

def close_database(connection):
    """
    Close the SQLite database connection.

    Parameters:
    - connection: SQLite database connection.
    """
    connection.close()

# Example usage:
try:
    connection, cursor = create_database()

    country_code_input = input("Enter the country code: ")
    vat_rate_input = float(input("Enter the VAT rate: "))

    add_vat_to_database(connection, cursor, country_code_input, vat_rate_input)

    retrieved_vat_rate = get_vat_from_database(cursor, country_code_input)

    if retrieved_vat_rate is not None:
        print(f"The VAT rate for {country_code_input} in Europe is {retrieved_vat_rate}%.")
    else:
        print("Invalid country code or not a European country.")

finally:
    close_database(connection)
