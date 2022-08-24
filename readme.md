# Scrap Problem 

Go to scraping/readme.md

# Modulos

Do not use, because it is float. and the answer will be wrong. 
```python
# Do not use this.
mod = 1e9+7
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