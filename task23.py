#Напишите функцию котoрый будет определять введенный год, 
#высокосный или нет.
def yaear(a):
    return
a = int(input("Kakoi seychas god ? :"))
if a % 4 == 0:
    print(a,"-Eto visokosnyi god")
elif a % 4 !=0:
    print(a,"-Eto neviskosnyi god")