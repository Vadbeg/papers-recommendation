"""Module with API"""


import os
import warnings
from typing import Any, List, Optional

import fastapi
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from papers_recommendation.modules.data.code_paper import CodePaper
from papers_recommendation.modules.data.papers_loading import PapersLoader
from papers_recommendation.modules.models.similar_papers_finder import (
    SimilarPapersFinder,
)
from papers_recommendation.utils import find_paper_by_id

warnings.filterwarnings('ignore')

PAPERS_WITH_CODE_TOKEN_ENV = 'PAPERS_WITH_CODE_TOKEN_ENV'
if os.getenv(PAPERS_WITH_CODE_TOKEN_ENV) is None:
    raise ValueError(
        'No paperswithcode API, you can get it here: '
        'https://paperswithcode.com/accounts/generate_api_token'
    )

app = FastAPI()


MODEL_PATH = '/home/vadbeg/Downloads/cc.en.300.bin'

papers_loader = PapersLoader(verbose=True)
papers: Optional[List[CodePaper]] = None

similar_papers_finder: SimilarPapersFinder = SimilarPapersFinder(
    titles_model_path=MODEL_PATH
)


@app.get(path='/papers', response_class=JSONResponse)
def load_papers(query: str, max_number_of_papers: int = 50) -> JSONResponse:
    global papers
    papers = papers_loader.get_papers_by_query(
        query=query, max_number_of_papers=max_number_of_papers
    )

    papers_response = [
        {
            'id': curr_paper.id,
            'title': curr_paper.title,
            'abstract': curr_paper.abstract,
        }
        for curr_paper in papers
    ]

    return JSONResponse(content=papers_response, status_code=fastapi.status.HTTP_200_OK)


@app.get(path='/train', response_class=JSONResponse)
def train_models() -> JSONResponse:
    status_code = fastapi.status.HTTP_204_NO_CONTENT
    content = f'No papers downloaded: {papers}'

    if papers and len(papers) > 0:
        similar_papers_finder.train_abstract_model(papers=papers)
        similar_papers_finder.train_nearest_neighbours_model(papers=papers)

        status_code = fastapi.status.HTTP_201_CREATED
        content = f'Models trained'

    return JSONResponse(content=content, status_code=status_code)


@app.get(path='/similar', response_class=JSONResponse)
def get_similar_papers(paper_id: str) -> JSONResponse:
    status_code = fastapi.status.HTTP_204_NO_CONTENT
    content: Any = f'No papers downloaded: {papers}'

    if papers and len(papers) > 0:
        query_paper = find_paper_by_id(paper_id=paper_id, papers=papers)

        if query_paper:
            try:
                papers_idx_and_score = similar_papers_finder.get_nearest_papers(
                    paper=query_paper
                )

                status_code = fastapi.status.HTTP_200_OK
                content = [
                    {
                        'id': papers[paper_id].id,
                        'title': papers[paper_id].title,
                        'abstract': papers[paper_id].abstract,
                        'paper_dist': paper_dist,
                    }
                    for paper_id, paper_dist in papers_idx_and_score
                ]
            except ValueError as exc:
                status_code = fastapi.status.HTTP_405_METHOD_NOT_ALLOWED
                content = str(exc)
        else:
            status_code = fastapi.status.HTTP_404_NOT_FOUND
            content = 'No query find'

    return JSONResponse(content=content, status_code=status_code)
