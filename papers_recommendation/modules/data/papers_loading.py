"""Module for papers retrieving"""

import math
import os
from typing import List

import paperswithcode
from tqdm import tqdm

from papers_recommendation.modules.data.code_paper import CodePaper


class PapersLoader:
    PAPERS_WITH_CODE_TOKEN_ENV = 'PAPERS_WITH_CODE_TOKEN_ENV'

    def __init__(self, verbose: bool = False):
        self._papers_client = paperswithcode.PapersWithCodeClient(
            token=os.environ[self.PAPERS_WITH_CODE_TOKEN_ENV]
        )

        self.verbose = verbose

    def get_papers_by_query(
        self, query: str, max_number_of_papers: int = 500
    ) -> List[CodePaper]:
        items_per_page = 100
        num_of_pages = math.ceil(max_number_of_papers / items_per_page)

        all_papers: List[CodePaper] = []

        for page_num in tqdm(range(1, num_of_pages + 1), postfix='Loading pages...'):
            papers = self._get_papers_by_query_from_page(
                query=query, page=page_num, items_per_page=items_per_page
            )

            all_papers.extend(papers)

        return all_papers[:max_number_of_papers]

    def _get_papers_by_query_from_page(
        self, query: str, page: int, items_per_page: int = 100
    ) -> List[CodePaper]:
        code_papers = []

        try:
            papers = self._papers_client.paper_list(
                q=query, page=page, items_per_page=items_per_page
            ).results

            code_papers = [CodePaper(paper=curr_paper) for curr_paper in papers]
        except Exception as exc:
            print(exc)

        return code_papers
