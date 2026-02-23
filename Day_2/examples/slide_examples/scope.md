```python
alpha = 0.05

def is_significant(p_value):
    return p_value < alpha
```

```python
def is_significant(p_value, alpha):
    return p_value < alpha
```