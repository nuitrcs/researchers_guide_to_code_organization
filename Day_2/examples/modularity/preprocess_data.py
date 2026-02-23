def get_column_average(df, columns):
    avg = df[columns].mean(axis=1)
    return avg