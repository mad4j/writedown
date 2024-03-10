"""
MarkPy - Easy Markdown document generator.

"""

# Daniele Olmisani <daniele.olmisani@gmail.com>
# see LICENSE file


from typing import List, Self
from markpy.exceptions import InvalidArgumentException

from markpy.renders.lists import render_dl, render_ul
from markpy.renders.headings import render_hn, render_uhn, render_ruler
from markpy.renders.sections import render_para, render_quote, render_code

from markpy.renders.tables import render_table_header
from markpy.renders.tables import render_table_row
from markpy.renders.tables import render_table_footer
from markpy.renders.tables import get_table_cell_align


class MDoc:

    """Class for easily generate pretty-readable Markdown documents.
    """

    def __init__(self: Self, page_width: int = 80) -> None:
        self.doc = ''
        self.page_width = page_width
        self.cell_widths = []
        self.cell_aligns = []
        self.list_used_bullets = ['', '', '', '', '', '']

    def __str__(self: Self) -> str:
        return self.doc


    def get_doc(self: Self) -> str:
        """Return the document as an str object.
        """
        # return interal document representation
        return self.doc

    def append(self: Self, doc: str) -> None:
        """Append the content of anohter MDoc object.
        """
        self.doc += doc.get_doc()

#   Headers and rulers
#   ------------------

    def add_h1(self: Self, text: str) -> None:
        """Append a H1 heading to current document.
        """
        self.doc += render_hn(text, level=1)

    def add_uh1(self: Self, text: str) -> None:
        """Append a H1 heading to current document using underlined syntax.
        """
        self.doc += render_uhn(text, level=1)

    def add_h2(self: Self, text: str) -> None:
        """Append a H2 heading to current document.
        """
        self.doc += render_hn(text, level=2)

    def add_uh2(self: Self, text: str) -> None:
        """Append a H2 heading to current document using underlined syntax.
        """
        self.doc += render_uhn(text, level=2)

    def add_h3(self: Self, text: str) -> None:
        """Append a H3 heading to current document.
        """
        self.doc += render_hn(text, level=3)

    def add_h4(self: Self, text: str) -> None:
        """Append a H4 heading to current document.
        """
        self.doc += render_hn(text, level=4)

    def add_h5(self: Self, text: str) -> None:
        """Append a H5 heading to current document.
        """
        self.doc += render_hn(text, level=5)

    def add_h6(self: Self, text: str) -> None:
        """Append a H6 heading to current document.
        """
        self.doc += render_hn(text, level=6)

    def add_ruler(self: Self) -> (None | InvalidArgumentException):
        """Append an horizontal ruler.
        """
        try:
            self.doc += render_ruler(self.page_width)
        except InvalidArgumentException:
            raise



#   Sections
#   --------

    def add_para(self: Self, text: str) -> None:
        """Append a new paragraph of text.
        """
        self.doc += render_para(text, page_width=self.page_width, trailer="  \n\n")

    def add_simple(self: Self, text: str) -> None:
        """Append unformatted text.
        """
        self.doc += render_para(text, page_width=self.page_width)

    def add_quote(self: Self, text: str) -> None:
        """Append a new blockquote section.
        """
        self.doc += render_quote(text, self.page_width)

    def add_code(self: Self, text: str, language: str = "text") -> None:
        """Append a new fenced code section.
        """
        self.doc += render_code(text, language, self.page_width)



#   Bullet lists
#   ------------

    def add_ul(self: Self, text: str, marker: str = '*', level: int = 1):
        """Append a bullet of un un-ordered list
        """
        self.doc += render_ul(
            text, 
            marker, 
            level,
            self.list_used_bullets,
            self.page_width)
        
    def add_dl(self: Self, term: str, text: str):
        """_summary_

        Args:
            term (str): _description_
            text (str): _description_
        """
        self.doc += render_dl(term, text, self.page_width)
        


#   Tables
#   ------

    def add_table_header(self: Self, *headers: List[str]) -> None:
        """Append a new table header.
        """

        # update interal state
        self.cell_widths = list(map(len, headers))
        self.cell_aligns = list(map(get_table_cell_align, headers))

        # add rendered header
        self.doc += render_table_header(*headers)


    def add_table_row(self: Self, *columns) -> None:
        """Append a new table row.
        """
        self.doc += render_table_row(
            *columns,
            widths=self.cell_widths,
            aligns=self.cell_aligns
        )

    def add_table_footer(self: Self) -> None:
        """Append a table trailer.
        """
        # add rendered footer
        self.doc += render_table_footer()
        # reset internal table state
        self.cell_widths = []
        self.cell_aligns = []
