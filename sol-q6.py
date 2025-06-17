import numpy as np
import pandas as pd

DATA_PATH = "data.csv"


def get_data():
    "데이터를 불러오는 함수"

    df = pd.read_csv(DATA_PATH)
    return df


def add_type(df):
    "지시사항에 따라 df에 Type칼럼을 추가하고 반환합니다."

    df["Type"] = np.where(df["Age"] < 19, "kid", "adult")

    df.loc[(df["Type"] == "kid") & (df["Sex"] == "male"), "Type"] = "boy"
    df.loc[(df["Type"] == "kid") & (df["Sex"] == "female"), "Type"] = "girl"

    return df


def main():
    # 데이터 불러오기
    df = get_data()
    print("추가 전\n", df.head())

    # 1. 새로운 특성 생성
    df_new = add_type(df.copy())
    print("추가 후\n", df_new.head())


if __name__ == "__main__":
    main()