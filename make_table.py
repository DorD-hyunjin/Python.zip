import pandas as pd


"""
표 형태 만들어보기
"""
col = ['A', 'B', 'C']
ind = [1, 2, 3]
con = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
df = pd.DataFrame(con, columns = col, index = ind)
print(df)
# Jupyter: 마지막 혹은 지정된 인스턴스 자동 출력/ 타 IDE: 변수 저장 및 출력이 수동


"""
빈칸으로 채워진 표 만들어보기
"""
col = ["", "", ""]
ind = ["", "", ""]
con = [["", "", ""], ["", "", ""], ["", "", ""]]
df = pd.DataFrame(con, columns = col, index = ind)
print(df)


"""
함수를 이용한 표 형태 만들기
"""
def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0, col_num):
        col.append(fill)
    for i in range(0, ind_num):
        ind.append(fill)
    for i in range(0, ind_num):
        con.append(col)
    return pd.DataFrame(con, columns = col, index = ind)

# 확인
print(df_maker(10, 10, "blank"))


"""
표 내용 채우기
"""
df = df_maker(2, 2, 0)

# update columns 
print(df.columns) # int64index([0, 0], dtype='int64') 
print(df.columns[0]) # indexing 가능
df.columns = ["국어", "수학"]
print(df.columns) # index(['국어', '수학'], dtype='object')

# update index
print(df.index) # int64index([0, 0], dtype='int64')
df.index = ['철수', '영희']
print(df.index) # index(['철수', '영희'], dtype='object')

# update contents 가로.ver
print(df.loc['철수']) # 국어0 수학0 Name: 철수, dtype:int64 (loc: location method)
print(df.iloc[0]) # 국어0 수학0 Name: 철수, dtype:int64 (iloc: indexing method)
df.loc["철수"] = [70, 90]
print(df) # 확인
df.loc["철수"][0] = 100 # indexing 사용
print(df) # 확인
df.iloc[1] = [80, 80] # indexing (iloc, 영희)
print(df) # 확인

# update contents 세로.ver
print(df.columns[0]) # '국어'
print(df.columns[1]) # '수학'
print(df['수학']) # 철수90 영희80 Name: 수학, dtype:int64
print(df[df.columns[1]]) # 철수90 영희80 Name: 수학, dtype:int64
df["국어"] = [10, 20] # 세로 update
df["국어"][1] = 80 # indexing 사용한 update
df[df.columns[1]] = [80, 80] # 수학 철수80 영희80 update 



"""
열 추가하기
"""
df = df_maker(3, 3, 0)
col = ["A", "B", "C"]
ind = [1, 2, 3]
df.columns = col
df.index = ind
print(df) # 3 x 3 table

# 새로운 컬럼명 추가
df["D"] = [1, 2, 3]
print(df) # 3 x 4 table

# 동일한 컬럼명 추가
df["E"] = [1, 2, 3]

print(df.columns) # index(['A', 'B', 'C', 'D', 'E'], dtype='object')
print(df.columns[-1]) # 'E'
# df.columns[-1] = "A" # TypeError: Index does not support mutable operations
print(type(df.columns)) # pandas.core.indexes.base.index

df.columns = ["A", "B", "C", "D", "A"]
print(df) # 변경 확인


# 확인요함
# """
# 행 추가하기
# """

# # 새로운 행 만들기
# df = df_maker(3, 3, 0)
# df2 = pd.DataFrame([[0, 0, 0]], columns = col, index = [4])
# print(df2) # 삽입할 New행 확인
# print(df.append(df2)) # 4 x 4 table 확인
# print(df) # 3 x 4 table 확인(비영구적)
# df = df.append(df2) # 변수 처리
# print(df) # 4 x 4 table 확인(영구적)

# df = df.append(df)
# print(df) # 8 x 4 table 확인(영구적)


"""
이중 index, columns 만들기
"""
# Basic Table Setting
col = ["국어", "수학", "영어"]
ind = ["철수중간", "철수기말", "영희중간", "영희기말"]
con = [[90, 70, 80], [80, 80, 80], [60, 70, 80], [70, 70, 70]]
df = pd.DataFrame(con, columns = col, index = ind)

ind = [["철수", "철수", "영희", "영희"], ["중간", "기말", "중간", "기말"]]
df.index = ind
print(df) # 이중 index 확인

col = [["과목", "과목", "과목"], ["국어", "수학", "영어"]]
df.columns = col
print(df) # 이중 columns 확인

