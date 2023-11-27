#부동산 정보 처리

#변환
"""import pandas as pd

target = "./apt.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("./apttt.csv", encoding="utf8")
print(df.head())"""

import pandas as pd

df = pd.read_csv("./apttt.csv", index_col=0)
print(df.head())

#칼럼명 바꾸기/컬럼 타입변경
df.rename(columns={"분양가격(제곱미터)":"분양가"})
print(df)
print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
print(df.dtypes)
print("\n---------------------\n")

#array 변환
arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr))

print(df.describe())

#축변환
print(df.transpose())
print("\n---------------------\n")
print(df.T.head())

#정렬
#res = df.sort_values(by="지역명")
#print(res)

res= df.sort_values(by="연도")[:5]
#res = df.sort_values("지역명", ascending=False)
print(res.head(5))

#칼럼이름 출력
res = df[["지역명", "연도"]]
res = df[["지역명", "연도", "분양가"]][:7]
print(res)
print("\n---------------------\n")
res = df.loc[:, ["지역명", "연도"]][:][:5]
print(res)

res = df.loc[6:, ["지역명", "연도"]]
res = df.loc[6:, ["지역명", "연도"]][3:]
print(res)

res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
#res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10]
print(res)

df0 = df.copy()
print(df0)

res = df.iloc[2]
res = df.iloc[2][1]
print(res)

res = df[df.index > 3560]
print(res)

res= df[df.월 == 3]
print(res)

res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
print(res)

columns=list(df.columns)
print(columns)

df1 = df.reindex(columns=list(df.columns)) + ["extra"]
print(df)
print("\n--------------------\n")
print(df1)

df1.loc[:6, "extra"] = '0'
df1.loc[:4, "extra"] = 'False'
print(df1)

df2 = df1.copy()


res = df2.dropna(how="any", inplace=True)
res = df2.fillna(how="1234", inplace=True)
print(df2)
print("\n--------------------------\n")
print(res)

res = pd.isna(df1)
print(res)

res = df["연도"].value_counts()
#res = df["지역명"].value_counts()
print(res)

res = df.groupby(["지역명", "연도", "월"]).sum()
print(res)

res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)
