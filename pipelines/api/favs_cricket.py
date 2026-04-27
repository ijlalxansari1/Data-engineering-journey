

df=pd.DataFrame({ "Name":["virat kohli" , "Imran Khan" , "Kallis"],
               "Country":["India" , "Pakistan","South Africa" ],
               "Runs":[28000 ,13000 , 22000]

               })




filtered = df[(df["Country"]=="India") | (df["Runs"]>0)]
filtered.sort_values(by="Runs" ,ascending=False)

# print(filtered)

# Try these one by one and tell me what each does
print(df_data.head())
# print(df.dtypes)
# print(df.columns)