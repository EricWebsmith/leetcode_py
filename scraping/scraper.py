import os
import re
import subprocess
import sys

from scraping.code_generator import CodeGenerator
from scraping.scraper_contest import ContestScraper
from scraping.scraper_problem import ProblemScraper
from scraping.scraper_result import ScraperResult

DESIGN = 'DESIGN'
COMMON = 'COMMON'


title_slug = sys.argv[1] if len(
    sys.argv) >= 2 else 'time-based-key-value-store'

scraper_result: ScraperResult
if title_slug.find('contest') > 0:
    print('----------------------contest----------------------')
    scraper_result = ContestScraper()(title_slug)
else:
    title_slug = re.sub('https://leetcode[.]c(n|om)/problems/', '', title_slug)
    title_slug = re.sub(
        'https://leetcode[.]c(n|om)/contest/(bi)?weekly-contest-\d+/problems/', '', title_slug)
    title_slug = title_slug.replace('solution/', '')
    title_slug = title_slug.replace('description/', '')
    title_slug = title_slug.replace('discussion/', '')
    title_slug = title_slug.replace('submissions/', '')
    title_slug = re.sub('\?.*', '', title_slug)
    title_slug = re.sub('/$', '', title_slug)
    scraper_result = ProblemScraper()(title_slug)


problem_type = ''
if len(sys.argv) >= 3:
    problem_type = sys.argv[2]

cg = CodeGenerator(scraper_result, problem_type)
cg()

if not os.path.exists('test'):
    os.mkdir('test')

title_slug_fixed = cg.title_slug.replace('-', '_')

path = f'test/lc_{cg.id}_{title_slug_fixed}.py'

with open(path, mode='w') as f:
    f.write(cg.code)

print(f'{cg.id}. {cg.title} done')

subprocess.call(['code', path])
