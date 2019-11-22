import pandas as pd

df = pd.read_csv('C:\\Users\Lenovo\Documents\ICUP Assignment Problems\ICUP Assignment Problems\Problem Statement 13\election_data_1.csv')
dg = pd.read_csv('C:\\Users\Lenovo\Documents\ICUP Assignment Problems\ICUP Assignment Problems\Problem Statement 13\election_data_2.csv')
df_list=[df,dg]
result=pd.concat(df_list)
result
s = result.shape[0]
print("total votes =",result.shape[0])
print("unique candidates :",result.Candidate.unique())
print("Votes for each Candidate:")
a=result['Candidate'].value_counts()
y = str(a)
print(a)
print("maximum votes are=",a.max())

f = open("results1.txt", "w+")
f.write(str(s))
f.write(str(result.Candidate.unique()))
f.write(y)
f.write(str(a.max()))
f.write("hello")
