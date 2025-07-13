print(f'''
          ,--.   ,--.,--.        
 ,---.  ,-|  | ,-|  |`--' ,---.  
| .-. |' .-. |' .-. |,--.| .-. : 
' '-' '\ `-' |\ `-' ||  |\   --. 
 `---'  `---'  `---' `--' `----'
distinguish that the number is odd or even.
''')

a = input("[+] masukan nomer: ")
aInt = int(float(a)) # float di dalam int tujuannya adalah untuk membulatkan input kebawah, dengan prinsip int yaitu bilangan bulat Jadi programnya akan membulatkan ke bawah.

if aInt % 2 == 0:
    print(f"angka {a} adalah angka genap")
else:
    print(f"angak {a} adalah angka ganjil")