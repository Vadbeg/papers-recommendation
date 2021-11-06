"""Module with code paper"""

import paperswithcode


class CodePaper:
    def __init__(self, paper: paperswithcode.client.Paper):
        self._paper = paper

    @property
    def id(self):
        return self._paper.id

    @property
    def title(self):
        return self._paper.title

    @property
    def abstract(self):
        return self._paper.abstract
