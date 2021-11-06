"""CLI for loading articles, training model and saving it all on disk"""


import typer

from papers_recommendation.cli.load_articles_cli import (
    load_articles_and_train_model_cli,
)

if __name__ == '__main__':
    typer.run(load_articles_and_train_model_cli)
