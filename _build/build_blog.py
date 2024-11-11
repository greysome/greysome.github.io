import os
import shutil
import pathlib
from datetime import datetime
from distutils import dir_util
from mistletoe import Document
from html_post_renderer import HtmlPostRenderer

SITE_DIR = '../_site'
head_html = open('../head.html', 'r').read()

def write_index_html():
    # POSTS -------------------------------------------------------------------------------
    post_entries = ''
    num_posts = 0
    posts = []
    for filename in os.listdir('../posts'):
        if not filename.endswith('.md'): continue
        num_posts += 1
        date = datetime.strptime(filename[:10], "%Y-%m-%d")
        # The title is the content of the first # heading
        for line in open(f'../posts/{filename}', 'r').readlines():
            if line.startswith('#'):
                title = line[1:].lstrip(' \t')
                break
        posts.append((date, filename, title))

    posts.sort(key=lambda x: x[0], reverse=True)

    for date, filename, title in posts:
        # %-d only works on Linux, %#d only works on Windows
        date = date.strftime('%b %-d, %Y')
        post_entries += f'<tr><td class="postdate">{date}</td>'
        post_entries += f'<td><a href="/posts/{filename[:-3]}.html">{title}</a></td></tr>\n'
        posts_heading = str(num_posts) + (' posts' if num_posts > 1 else ' post')


    # WRITEUPS -------------------------------------------------------------------------------
    writeup_entries = ''
    num_writeups = 0
    for filename in os.listdir('../writeups'):
        if not filename.endswith('.pdf') and not filename.endswith('.txt'):
            continue
        num_writeups += 1
        writeup_entries += f'<tr><td><a target="blank" href="/writeups/{filename}">{filename}</a></td></tr>\n'
    writeups_heading = str(num_writeups) + (' writeups' if num_writeups > 1 else ' writeup')

    content = f'''
<html>
  <head>{head_html}</head>
  <body>
    <h1>wy's blog</h1>
    
    <p>{posts_heading}</p>
    <table>
      {post_entries}
    </table>

    <br>
    
    <p>{writeups_heading}</p>
    <table>
      {writeup_entries}
    </table>

    <br>

    <p>Tell me something nice <a href="comments.html">here</a> ☺</p>
  </body>
</html>
 '''
    with open(f'{SITE_DIR}/index.html', 'w') as f:
        print(f'Writing {SITE_DIR}/index.html')
        f.write(content)


def write_comments_html():
    comments_body_html = open('../comments_body.html', 'r').read()
    content = f'''
<html>
  <head>{head_html}</head>
  <body>
    {comments_body_html}
  </body>
</html>
 '''
    with open(f'{SITE_DIR}/comments.html', 'w') as f:
        print(f'Writing {SITE_DIR}/comments.html')
        f.write(content)


def copy_static_files():
    print(f'Copying /404.html over to {SITE_DIR}')
    shutil.copyfile('../404.html', f'{SITE_DIR}/404.html')
    print(f'Copying /style.css over to {SITE_DIR}')
    shutil.copyfile('../style.css', f'{SITE_DIR}/style.css')
    print(f'Copying /writeups over to {SITE_DIR}')
    dir_util.copy_tree('../writeups', f'{SITE_DIR}/writeups')
    print(f'Copying /resource over to {SITE_DIR}')
    dir_util.copy_tree('../resource', f'{SITE_DIR}/resource')


def render_post(filename):
    with open(f'../posts/{filename}', 'r') as f:
        with HtmlPostRenderer() as renderer:
            rendered = renderer.render(Document(f))

    write_path = f'{SITE_DIR}/posts/{filename[:-3]}.html'
    with open(write_path, 'w') as f:
        print(f'Writing {write_path}')
        f.write(rendered)


if __name__ == '__main__':
    # Make sure that relative paths are correct
    os.chdir(os.path.dirname(__file__))
    try:
        shutil.rmtree(f'{SITE_DIR}')
    except FileNotFoundError:
        print(f'{SITE_DIR} doesn\'t exist yet')

    # Create site directory
    pathlib.Path(f'{SITE_DIR}').mkdir(parents=True, exist_ok=True)
    # Create site/posts
    pathlib.Path(f'{SITE_DIR}/posts').mkdir(parents=True, exist_ok=True)
    for filename in os.listdir('../posts'):
        if filename.endswith('.md'):
            render_post(filename)
    # Create site/resources, site/writeups and other files
    copy_static_files()
    # Write home pages
    write_index_html()
    write_comments_html()