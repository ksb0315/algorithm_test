import numpy
import pandas as pd

p = "C:/Users/sunbum/Desktop/work2(algo)/algorithm_test/"
csv_test = pd.read_csv(p + "records.csv")
print(csv_test)
ans = []
csv_test = csv_test.fillna("NULL")

# print(csv_test)
for i in range(csv_test.shape[0]):
    temp = []
    for j in range(csv_test.shape[1]):
        # print(type(csv_test.iloc[i][j]))
        if type(csv_test.iloc[i][j]) == str:
            temp.append(str(csv_test.iloc[i][j]))
        elif type(csv_test.iloc[i][j]) == numpy.int64 or type(csv_test.iloc[i][j]) == numpy.float64 or type(csv_test.iloc[i][j]) == int:
            if type(csv_test.iloc[i][j]) == float:
                temp.append(csv_test.iloc[i][j])
            else:
                temp.append(int(csv_test.iloc[i][j]))
        
    ans.append(temp)
    
for a in ans:
    print(tuple(a))