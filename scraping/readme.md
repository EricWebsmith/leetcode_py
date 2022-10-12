# Install:

pip install python-leetcode

url: https://pypi.org/project/python-leetcode/

use:
```
python scraper.py title_slug
```
you can find title_slug from url.
like
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
slug is "sum-of-mutated-array-closest-to-target"
```
python scraper.py "sum-of-mutated-array-closest-to-target"
```
you should create .env yourself.
it contains only the following two variables.
open the following url from chrome to check the following two variable

> chrome://settings/cookies/detail?site=leetcode.com

or check out this article:

https://cookie-script.com/documentation/how-to-check-cookies-on-chrome-and-firefox

I load them like that:

leetcode_session = env['LEETCODE_SESSION']

csrf_token = env['CSRF_TOKEN']