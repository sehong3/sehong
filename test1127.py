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
print(res)
