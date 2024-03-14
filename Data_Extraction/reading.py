import pandas as pd
import json
import mysql.connector
import psycopg2



def read_data_from_file(file_format, file_path):
    """
    Read data from various file formats or databases.

    Parameters:
        file_format (str): The format of the file or database.
        file_path (str): The path to the file or the connection string for the database.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data.
    """
    supported_formats = ["csv", "excel", "parquet", "mysql", "postgres"]

    if file_format not in supported_formats:
        raise ValueError(f"Unsupported file format: {file_format}")

    if file_format == "csv":
        df = read_from_csv_file(file_path)
    elif file_format == "excel":
        df = read_from_excel_file(file_path)
    elif file_format == "parquet":
        df = read_from_parquet_file(file_path)
    elif file_format == "mysql":
        df = read_from_mysql_db(file_path)
    elif file_format == "postgres":
        df = read_from_postgres_db(file_path)
    
    return df

# def read_data_from_file(file_format,input_path):
#     if file_format == "csv":
#         df = read_from_csv_file(input_path)
#     elif file_format == 'excel':
#         df = read_from_excel_file(input_path)
#     elif file_format == "parquet":
#         df = read_from_parquet_file(input_path)
#     elif file_format == 'mysql':
#         df = read_from_mysql_db(input_path)
#     elif file_format == "postgres":
#         df = read_from_postgres_db(input_path)
    
#     return df


def read_from_csv_file(input_path):

    """
    Read data from a CSV file and return a pandas DataFrame.

    Parameters:
    input_path (str): The path to the CSV file to be read.

    Returns:
    pd.DataFrame: A DataFrame containing the data read from the CSV file.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    IOError: If there is an error reading the file.
    """

    try:
        df = pd.read_csv(input_path)
        return df
    
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    
    except IOError as e:
        print(f"Error: reading file '{input_path}' : {e}")
        return None
    
def read_from_excel_file(input_path):

    """
    Read data from a Excel file and return a pandas DataFrame.

    Parameters:
    input_path (str): The path to the Excel file to be read.

    Returns:
    pd.DataFrame: A DataFrame containing the data read from the Excel file.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    IOError: If there is an error reading the file.
    """

    try:
        df = pd.read_excel(input_path,engine="xlrd")
        return df
    
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    
    except IOError as e:
        print(f"Error: reading file '{input_path}' : {e}")
        return None
    
def read_from_parquet_file(input_path):

    """
    Read data from a parquet file and return a pandas DataFrame.

    Parameters:
    input_path (str): The path to the parquet file to be read.

    Returns:
    pd.DataFrame: A DataFrame containing the data read from the parquet file.

    Raises:
    FileNotFoundError: If the specified file does not exist.
    IOError: If there is an error reading the file.
    """

    try:
        df = pd.read_parquet(input_path,engine='pyarrow')
        return df
    
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    
    except IOError as e:
        print(f"Error: reading file '{input_path}' : {e}")
        return None


def read_from_mysql_db(input_path):
    try:
        with open(input_path, 'r') as jsondata:
            creds = json.load(jsondata)

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=creds['host'],
            user=creds['user'],
            password=creds['password'],
            database=creds['database']
        )

        if connection.is_connected():
            print("Connected to MySQL successfully!")
            cursor = connection.cursor()

            table_name = creds.get('table_name', None)
            if table_name:
                query = f"SELECT * FROM {table_name}"
                cursor.execute(query)
                result = cursor.fetchall()

                # Get column names
                column_names = [desc[0] for desc in cursor.description]

                # Create DataFrame
                df = pd.DataFrame(result, columns=column_names)

                # Clean up
                cursor.close()
                connection.close()

                return df
            else:
                print("Error: 'table_name' not specified in credentials.")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input file.")
    except mysql.connector.Error as e:
        print(f"Error: Failed to connect to MySQL database - {e}")
    except Exception as e:
        print(f"Error: {e}")

    
# def read_from_mysql_db(input_path):
#     with open(input_path,'r') as jsondata:
#         creds = json.load(jsondata)
#         try:
#             connection = mysql.connector.connect(
#             host=creds['host'],
#             user=creds['user'],
#             password=creds['password'],
#             database=creds['database']
#             )
#             print("Connected to MySQL successfully!")
#             if connection:
#                 cursor = connection.cursor()
#                 table_name = creds['table_name']
#                 query = f"SELECT * FROM {table_name}"
#                 cursor.execute(query)
#                 result = cursor.fetchall()
#                 column_names = [desc[0] for desc in cursor.description]
                
#                 df = pd.DataFrame(result, columns=column_names)
#                 cursor.close()
#                 connection.close()
#                 return df
#         except Exception as e:
#             print(f"Error: {e}")


def read_from_postgres_db(input_path):
    try:
        with open(input_path, 'r') as jsondata:
            creds = json.load(jsondata)
            
        connection = psycopg2.connect(
            host=creds['host'],
            user=creds['user'],
            password=creds['password'],
            database=creds['database']
        )
        
        print("Connected to PostgreSQL successfully!")

        if connection:
            table_name = creds['table_name']
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, con=connection)
            return df

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading credentials file: {e}")
    except psycopg2.OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None

# def read_from_postgres_db(input_path):
#     with open(input_path,'r') as jsondata:
#         creds = json.load(jsondata)
#         try:
#             connection = psycopg2.connect(
#             host=creds['host'],
#             user=creds['user'],
#             password=creds['password'],
#             database=creds['database']
#             )
#             print("Connected to MySQL successfully!")
#             if connection:
#                 table_name = creds['table_name']
#                 df = pd.read_sql(f"SELECT * FROM {table_name}",con=connection)
#                 return df
#         except Exception as e:
#             print(f"Error: {e}")

