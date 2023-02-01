import pandas as pd
from prefect import flow, task
import click


@task
def load_file_to_db(file_name):
    df = pd.read_csv(file_name)
    return df


@task
def ctas(df):
    new_col = []
    for x in df['url']:
        new_col.append(x.split("/", )[2])
    df['domain_of_url'] = new_col
    return df


@task
def copy_to_file(df):
    df.to_csv('norm.csv.gz')
    return 'norm.csv.gz'


@click.command()
@click.argument('file_name')
@flow
def api_flow(file_name):
    return copy_to_file(ctas(load_file_to_db(file_name)))

