"""CLI for loading articles, training model and saving it all on disk"""


import typer

from papers_recommendation.cli.find_similar_articles_cli import (
    find_similar_articles_cli,
)

if __name__ == '__main__':
    typer.run(find_similar_articles_cli)
