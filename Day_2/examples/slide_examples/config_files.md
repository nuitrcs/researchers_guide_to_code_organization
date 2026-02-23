```yaml
#config.yaml
paths:
  data_in: "data/raw/"
  data_out: "results/simulations/"

model:
  architecture: "random_forest"

hyperparameters:
  iterations: 500
  error_tolerance: 1e-5
```

```toml
# config.toml
[paths]
data_in  = "data/raw/"
data_out = "results/simulations/"

[model]
architecture = "random_forest"

[hyperparameters]
iterations      = 500
error_tolerance = 1e-5
```

```json
{
  "paths": {
    "data_in": "data/raw/",
    "data_out": "results/simulations/"
  },
  "model": {
    "architecture": "random_forest"
  },
  "hyperparameters": {
    "iterations": 500,
    "error_tolerance": 0.00001
  }
}
```