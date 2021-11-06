"""Module with utils for whole project"""

from typing import List, Optional

from papers_recommendation.modules.data.code_paper import CodePaper


def find_paper_by_id(paper_id: str, papers: List[CodePaper]) -> Optional[CodePaper]:
    for curr_paper in papers:
        if curr_paper.id == paper_id:
            return curr_paper

    return None
