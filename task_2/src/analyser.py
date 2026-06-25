import json
import pandas as pd

def read_submissions() -> pd.DataFrame:
    
    try :
        df = pd.read_csv("task_2/data/submissions.csv")

        df["score"] = pd.to_numeric(df["score"])

    except FileNotFoundError :
        print("ERROR : CSV file does not exist.")

    except ValueError :
        print ("ERROR : Data type does not match the required data type of the field.")

    if df.empty :
        print ("ERROR : Empty CSV file.")

    if df["score"].isnull().any() :
        print ("ERROR : Missing value in Score column")

    return df

def get_submitted_students(df):
    submitted_students = df[df["submitted"] == "yes"]
    return submitted_students


def calculate_average_score(df):
    average = df["score"].mean()
    return round(average, 2)


def get_domain_wise_average(df):
    domain_average = {}

    for domain in df["domain"].unique():
        average = df[df["domain"] == domain]["score"].mean()
        domain_average[domain] = round(average, 2)

    return domain_average


def get_missing_submissions(df):
    missing_students = df[df["submitted"] != "yes"]["name"]
    return list(missing_students)


def write_summary(summary, output_path):
    with open(output_path, "w") as file:
        json.dump(summary, file, indent=4)
    print ("Summary was successfully written.")

