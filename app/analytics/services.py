import pandas as pd
from app.models import Employee
from app import database as db


def extract_data(file, filename):
    try:
        # read file into pandas 
        if filename.lower().endswith(".csv"):
            data = pd.read_csv(file)
        else:
            data = pd.read_excel(file)
        data = data.rename(columns={'Name': 'name', 'Unit': 'unit', 'Tenure (Years)': 'tenure_year'})
        data_dict = data.to_dict(orient='records')
        for row in data_dict:
            new_record = Employee(**row)
            db.session.add(new_record)
        db.session.commit()
    except FileNotFoundError:
        # handle file not found error
        error_message = "File not found!"
        return ("analytics.analytics_upload", error_message)
    except ValueError:
        # handle value error
        error_message = "Error in data format!"
        return ("analytics.analytics_upload", error_message)
    except Exception as e:
        # handle any other exception
        error_message = """
        Error in column(s) name, columns name must be : 
        'Name', 'Unit',and 'Tenure (Year)'
        """
        return ("analytics.analytics_upload", error_message)
    return ("analytics.analytics_upload", "File uploaded successfully")

    
    