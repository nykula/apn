#!/usr/bin/python3

site = 'Актуальні проблеми нефрології'

links = [['/17/', 'Випуск 17'],
         ['/18/', 'Випуск 18'],
         ['/19/', 'Випуск 19'],
         ['/20/', 'Випуск 20'],
         ['/21/', 'Випуск 21'],
         ['/22/', 'Випуск 22'],
         ['/23/', 'Випуск 23'],
         ['/24/', 'Випуск 24']]

import re
import sys

script, raw_file = sys.argv
m = re.search('^(.+)\.txt$', raw_file)

if None == m:
    sys.exit(1)

f1 = open(raw_file, 'r')
source = f1.read()
f1.close()

ready_file = ''.join([m.group(1), '.html'])
print(ready_file)

import bs4
import jinja2
import markdown

f2 = open('template.html', 'r')
template = jinja2.Template(f2.read())
f2.close()

article = markdown.markdown(source)
soup = bs4.BeautifulSoup(article, 'lxml')
title = str(soup.h1.string)

output = ''
raw = template.render(site=site, links=links,
                      title=title, article=article)

for line in re.split('\n', raw):
    line = re.sub('^\s+', '', line)
    output = output + line

output = re.sub('/em>', '/em> ', output)
output = re.sub('<h2', '<hr /><h2', output)
output = re.sub('<p><str(.+)ong></p>', '<hr /><p><str\\1ong></p>', output)

f3 = open(ready_file, 'w')
f3.write(output)
