"""Module for loading articles and pickling articles finder"""

from pathlib import Path
from typing import Generator, List

import typer

from papers_recommendation.cli.utils import pickle_save
from papers_recommendation.modules.data.code_paper import CodePaper
from papers_recommendation.modules.data.papers_loading import PapersLoader


def load_articles_and_train_model_cli(
    query: str = typer.Option(..., help='Query to search in articles'),
    max_num_of_articles: int = typer.Option(..., help='Max number of articles to load'),
    verbose: bool = typer.Option(default=True, is_flag=True),
    cache_folder: Path = typer.Option(
        default=Path('cache').absolute(),
        help='Folder to which result articles and model would be saved',
    ),
) -> None:
    papers_loader = PapersLoader(verbose=verbose)

    papers = papers_loader.get_papers_by_query(
        query=query, max_number_of_papers=max_num_of_articles
    )

    cache_folder.mkdir(exist_ok=True)
    papers_path = cache_folder.joinpath('papers.pickle')
    pickle_save(obj=papers, path=papers_path)

    print_all_papers(papers=papers)


def print_all_papers(papers: List[CodePaper]) -> None:
    def papers_generator() -> Generator[str, None, None]:
        for idx in range(len(papers)):
            curr_paper = papers[idx]

            paper_description = ''
            paper_description += typer.style(
                text=f'{curr_paper.title}', fg=typer.colors.GREEN
            )
            paper_description += typer.style(
                text=f' {curr_paper.id} \n', fg=typer.colors.RED
            )

            yield paper_description

    typer.echo_via_pager(papers_generator)
