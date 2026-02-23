```python
try:
    result = 1 / x
except:
    # Catches EVERY ERROR, even the user trying to exit (Ctrl+C), and continues as normal
    pass
```

```python
try:
    result = 10 / x
except ZeroDivisionError:
    result = 0
    print("Warning: Division by zero. Defaulting to result = 0.")
except TypeError:
    print("Error: Please provide a number.")
```