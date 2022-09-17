# install
```bash
pip install lxml
pip install python-dotenv
pip install python-leetcode
```

# vs code config

`.vscode/settings.json`

```json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./test",
        "-p",
        "*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true,
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/Thumbs.db": true,
        "__pycache__": true,
        "**/__pycache__": true
    }
}
```

# Scrap Problem 

Go to scraping/readme.md

# Modulos

Do not use, because it is `float`. and the answer will be wrong. 
```python
# Do not use this.
mod = 1e9+7
# Do not use this.
```

Use
```
mod = 1_000_000_007
```
or 
```python
mod = 10 ** 9 + 7
```

# Using Numpy

Don't forget to make the array int.
```
np.zeros([4, m, n], dtype=int)
```

# Queue
Use collections.deque in stead of queue.Queue. 

https://www.geeksforgeeks.org/difference-between-queue-queue-vs-collections-deque-in-python/

# Serialize

> 297. Serialize and Deserialize Binary Tree

# int max
```
sys.maxsize
```

# array

del is 3 times faster

```
del arr[k]
```

```
arr = arr[:k] + arr[k+1:]
```

I guess the later will reconstruct arr. 