import pandas as pd
import datetime

log_file = "activity_log.csv"


def log_activity(activity):
    df = pd.DataFrame([[datetime.datetime.now(), activity]], columns=['Timestamp', 'Activity'])
    df.to_csv(log_file, mode='a', header=False, index=False)


def generate_report():
    try:
        df = pd.read_csv(log_file)
        print(df)
    except FileNotFoundError:
        print("No logs available.")
