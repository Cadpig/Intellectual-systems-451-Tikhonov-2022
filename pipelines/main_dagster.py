from dagster import job, op
import pandas as pd


@op
def load_file_to_db():
    df = pd.read_csv("pipelines/original.csv")
    return df

@op
def ctas(df):
    new_col = []
    for x in df['url']:
        new_col.append(x.split("/",)[2])
    df['domain_of_url'] = new_col
    return df

@op
def copy_to_file(df):
    df.to_csv('pipelines/norm.csv.gz')
    return 'norm.csv.gz'


@job
def serial():
    df1 = load_file_to_db()
    df2 = ctas(df1)
    print(copy_to_file(df2))