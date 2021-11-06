"""CLI for finding similar articles"""

from pathlib import Path
from typing import Generator, List, Tuple

import typer

from papers_recommendation.cli.utils import pickle_load
from papers_recommendation.modules.data.code_paper import CodePaper
from papers_recommendation.modules.models.similar_papers_finder import (
    SimilarPapersFinder,
)


def find_similar_articles_cli(
    paper_id: str = typer.Option(..., help='Id of query paper'),
    fasttext_model_path: Path = typer.Option(
        default='cc.en.300.bin', help='Path to saved fasttext model'
    ),
    cache_folder: Path = typer.Option(
        default=Path('cache').absolute(),
        help='Folder to which result articles and model would be saved',
    ),
) -> None:
    papers_path = cache_folder.joinpath('papers.pickle')
    papers: List[CodePaper] = pickle_load(path=papers_path)

    query_paper = find_paper_by_id(paper_id=paper_id, papers=papers)

    similar_papers_finder = SimilarPapersFinder(
        papers=papers, titles_model_path=fasttext_model_path
    )

    similar_papers_finder.train_abstract_model()
    similar_papers_finder.train_nearest_neighbours_model()

    nearest_papers_score_and_idx = similar_papers_finder.get_nearest_papers(
        paper=query_paper
    )

    print_nearest_papers(
        papers_idx_and_score=nearest_papers_score_and_idx, papers=papers
    )


def print_nearest_papers(
    papers_idx_and_score: List[Tuple[int, float]], papers: List[CodePaper]
) -> None:
    def nearest_papers_generator() -> Generator[str, None, None]:
        for paper_id, paper_dist in papers_idx_and_score:
            curr_paper = papers[paper_id]

            paper_description = ''
            paper_description += typer.style(
                text=f'{curr_paper.title} {paper_dist}', fg=typer.colors.GREEN
            )
            paper_description += typer.style(
                text=f' {curr_paper.id} \n', fg=typer.colors.RED
            )

            paper_description += f'{curr_paper.abstract} \n'

            yield paper_description

    typer.echo_via_pager(nearest_papers_generator)


def find_paper_by_id(paper_id: str, papers: List[CodePaper]) -> CodePaper:
    for curr_paper in papers:
        if curr_paper.id == paper_id:
            return curr_paper

    raise ValueError(f'No paper with such id: {paper_id}!')
