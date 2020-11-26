import glob, os
import pandas as pd
import re
tablo = df = pd.DataFrame({"a":[]}) # üstüne eklemek için boþ tablo tanýmlandý.
print("Boþ => " , tablo)

files = glob.glob('*.xlsx')
#print(files)


# dosyalar içindeki numaralara göre sýralanýr. This is called "natural sorting" or 
#"human sorting" (as opposed to lexicographical sorting, which is the default).
files.sort(key=lambda f: int(re.sub('\D', '', f)))

for file in files:
    file_name = file
    #print(file)
    data = pd.read_excel(file_name, skiprows=20)    
    # print(data)
    global x2
    x2 = pd.DataFrame(data, columns= ['Gate1'])    
    #print(x2)
    x2 = x2.rename(columns={'Gate1': file_name.replace(".xlsx","")})
    #print("-_" * 30)
    tablo = pd.concat([tablo, x2], axis=1) 


def remove_input_xlsx_files():
    removed_input_files = glob.glob("*.xlsx")
    print(str(len(removed_input_files))+" adet xlsx dosya siliniyor..")
    for f in removed_input_files:
        os.remove(f)

remove_input_xlsx_files()

del tablo['a'] 
print(tablo)
print("-." * 60)
tablo.to_excel("output.xlsx")
print("Output exceli oluþturuldu.")