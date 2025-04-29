def validate_data(data):
    assert data.isnull().sum().sum() == 0, "Missing values found!"
    assert 'species' in data.columns, "Target column missing!"
    return True
