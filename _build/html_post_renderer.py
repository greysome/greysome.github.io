"""
Convert my .md posts to HTML.

I extended HtmlRenderer with my own custom functionality, namely a new
Figure token and a custom preamble.
"""

import re
import html
from itertools import chain
from urllib.parse import quote
from mistletoe import block_token
from mistletoe import span_token
from mistletoe.latex_token import Math
from mistletoe.block_token import HtmlBlock
from mistletoe.span_token import SpanToken, EscapeSequence, HtmlSpan
from mistletoe.html_renderer import HtmlRenderer

class Figure(SpanToken):
    """
    Similar to an image, but with an extra scale field
    """
    alt_text = '!\[([^\]]*)\]'
    src = r'(.*?)'
    caption = r'"(.*[^"])"'
    scale = r'(([0-9]*)\%)?'
    pattern = re.compile(rf'{alt_text}\({src}\s*{caption}\s*{scale}\s*\)')

    def __init__(self, match):
        self.alt = EscapeSequence.strip(match.group(1))
        self.src = EscapeSequence.strip(match.group(2).strip())
        self.caption = EscapeSequence.strip(match.group(3))
        if match.group(5):
            self.scale = EscapeSequence.strip(match.group(5))
        else:
            self.scale = '100'
        self.dest_type = getattr(match, "dest_type", None)
        self.label = getattr(match, "label", None)
        self.title_delimiter = getattr(match, "title_delimiter", None)


class HtmlPostRenderer(HtmlRenderer):
    def __init__(
        self,
        *extras,
        html_escape_double_quotes=False,
        html_escape_single_quotes=False,
        process_html_tokens=True,
        **kwargs
    ):
        self._suppress_ptag_stack = [False]
        final_extras = chain((Figure,Math), (HtmlBlock, HtmlSpan) if process_html_tokens else (), extras)
        super().__init__(*final_extras, **kwargs)
        # parse all Images as Figures
        del self.render_map['Image']
        # for use in Figures
        self.figno = 0
        self.html_escape_double_quotes = html_escape_double_quotes
        self.html_escape_single_quotes = html_escape_single_quotes


    def __exit__(self, *args):
        super().__exit__(*args)


    def escape_html_text(self, s: str) -> str:
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        if self.html_escape_double_quotes:
            s = s.replace('"', "&quot;")
        if self.html_escape_single_quotes:
            s = s.replace('\'', "&#x27;")
        return s


    def render_math(self, token):
        """
        Math tokens are added so that the parser leaves symbols
        within math blocks alone, like & and \
        """
        return self.render_raw_text(token)


    def render_figure(self, token):
        self.figno += 1
        return f'''
<table style="margin-left:auto; margin-right:auto">
  <tr>
    <td style="text-align:center">
      <img src="/resource/{token.src}"
           alt="{token.alt}"
           style="width: {token.scale}%; height: auto"
           class="img-responsive" />
    </td>
  </tr>
  <tr>
    <td style="text-align:center;"><p>Figure {self.figno}. {token.caption}</p></td>
  </tr>
</table>
'''


    def render_document(self, token: block_token.Document) -> str:
        self.footnotes.update(token.footnotes)
        head = open('../head.html', 'r').read()
        body = '\n'.join([self.render(child) for child in token.children])
        return f'''
<html>
<head>
{head}
</head>
<body>
<a href="/index.html">&lt; Back</a> 
{body}
</body>
</html>
        '''