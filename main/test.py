from Data_Extraction import reading as rd

input_path = "/home/razz/Rajesh/data_extraction/source_files/mtcars.json"
input_path_par = "/home/razz/Rajesh/data_extraction/source_files/MT cars.parquet"



df = rd.read_from_json_file(input_path)
df1 = rd.read_from_parquet_file(input_path_par)

print(df.head())
print(df1.head())