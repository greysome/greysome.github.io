"""
Convert my .md posts to HTML.

I extended HtmlRenderer with my own custom functionality, namely a new
Figure token, footnotes and a custom preamble.
"""

import re
import html
from itertools import chain
from urllib.parse import quote
from mistletoe import block_token
from mistletoe import span_token
from mistletoe.latex_token import Math
from mistletoe.block_token import Footnote
from mistletoe.span_token import SpanToken, HtmlSpan
from mistletoe.html_renderer import HtmlRenderer


class Figure(SpanToken):
    """
    Similar to an image, but with an extra scale field
    """
    alt_text = '!\[([^\]]*)\]'
    src = r'(.*?)'
    caption = r'"([^"]*)"'
    scale = r'(([0-9]*)\%)?'
    pattern = re.compile(rf'{alt_text}\({src}\s*{caption}\s*{scale}\s*\)')

    def __init__(self, match):
        self.alt = match.group(1)
        self.src = match.group(2)
        self.caption = match.group(3)
        if match.group(5):
            self.scale = match.group(5)
        else:
            self.scale = '100'


class FootReference(SpanToken):
    pattern = re.compile(rf'\[\^(.*?)\]')

    def __init__(self, match):
        self.ref = match.group(1)


class Footnote(SpanToken):
    pattern = re.compile(rf'^\[\^(.*?)\]:\s(.*)$')
    parse_group = 2
    parse_inner = True

    def __init__(self, match):
        self.ref = match.group(1)
        self.content = match.group(2)


class HtmlPostRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(Math, Figure, FootReference, Footnote)
        # parse all Images as Figures
        del self.render_map['Image']
        # for use in Figures
        self.figno = 0
        self.footnotes = []


    # Turns a heading like "My Heading 1!" into "my-heading-1"
    def _create_id(self, heading):
        _id = ''
        nonalnum_start = True
        for c in heading:
            if c.isalnum():
                nonalnum_start = True
                _id += c.lower()
            elif nonalnum_start:
                _id += '-'
                nonalnum_start = False
        if _id[-1] == '-':
            return _id[:-1]
        return _id
    

    def render_heading(self, token: block_token.Heading) -> str:
        level = token.level
        inner = self.render_inner(token)
        heading = ''.join(child.content for child in token.children)
        print(heading)
        _id = self._create_id(heading)
        return f'<h{level} id="{_id}">{inner}</h{level}>'
        

    def render_math(self, token):
        """
        Math tokens are added so that the parser leaves symbols
        within math blocks alone, like & and \
        """
        return self.render_raw_text(token)


    def render_footnote(self, token):
        content = ''
        for child in token.children:
            content += self.render(child)
        self.footnotes.append(f'{token.ref}. {content} <a id="footnote-{token.ref}" href="#footnoteref-{token.ref}">back</a>')
        return ''


    def render_foot_reference(self, token):
        return f'<sup><a id="footnoteref-{token.ref}" href="#footnote-{token.ref}">{token.ref}</a></sup>'


    def render_figure(self, token):
        self.figno += 1
        return \
f'''
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
        head = open('../head.html', 'r').read()
        body = '\n'.join([self.render(child) for child in token.children])
        body += '\n<div class="footnote">'
        for footnote in self.footnotes:
            body += footnote + '<br>'
        body += '\n</div>\n'
        return \
f'''
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