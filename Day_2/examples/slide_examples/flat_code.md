```bash
data_1 = load("data.csv")
data_1_normalized = normalize(data_1)
data_2 = load("auxiliary_data.csv")
data_2_normalized = normalize(data_2)
data_merged = merge(data_1_normalized, data_2_normalized)
data = drop_nulls(data_merge)
data = encode_categories(data)
exploratory_stats = stats(data)
plot_histogram(exploratory_stats)
processed_data = process(data)
metrics = analysis(processed data)
make_figure(processed_data, metrics)
```

