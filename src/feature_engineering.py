def prepare_time_series_features(df):
    df = df.sort_values("Date").copy()
    df["time_index"] = range(len(df))
    return df
