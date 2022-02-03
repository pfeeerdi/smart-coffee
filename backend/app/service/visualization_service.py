import pandas as pd
from app.service.coffee_service import get_hist

def get_df():
    data = get_hist()
    df = pd.DataFrame(data)
    return df


def print_df():
    print(get_df())
