#کدی که داره هر کاراکتر فایل رو جداگانه می خونه و جدا می کنه که درست نیست و خیلی سختههه
# from statistics import mean
# def calculate_averages(input_file_name):
#     grades=[]
#     output_file_name=[]
#
#     input_file_name=open("grades.csv")
#     pure_list=input_file_name.read().split()
#     print(pure_list)
#     person_grade=dict()
#     m=0
#     name=""
#     name_list=[]
#     Sum=[]
#     a=""
#     for each_str in pure_list:
#         for i in range(len(each_str)):
# #             print("each_str[i] ",each_str[i])
#
#             if each_str[i].isalpha():
#                 name=name+each_str[i]
#             elif each_str[i].isdigit() and each_str[i-1].isdigit():
#                 a=each_str[i-1]+each_str[i]
# #                 print("a= ",a)
#                 m=m+int(a)
#                 print('m= ',m)
#
#             elif each_str[i]==",":
#                 continue
#             elif each_str[i].isdigit():
#                 m=m+int(each_str[i])
#
#         Sum.append(m)
#         name_list.append(name)
#         name=" "
#         m=0
#     print("name_list= ", name_list, Sum)
#
#

#########توجه کننن، که این کد اینجا رو عوض نکردی و کد توی مایکروسافت

import csv

# For the average
from statistics import mean


def calculate_averages(input_file_name, output_file_name):
    list_adad=[]
    mean_of_eachline=[]
    nahai=[]
    names=[]
    file=[]
    f=open(input_file_name)
    for line in f:
        line=line.strip().split(",")
        file.append(line)
#         print(line)
        adad=map(float,line[1:])
        list_adad.append(list(adad))
#     print("file= %s \n  \nlist_adad=%s \n " %(file, list_adad)) it is written for checking the output
#         print(list_adad)
    f.close()
    for element in list_adad:
        element=mean(element)
        element=str(element)
        mean_of_eachline.append(element)
#     print(mean_of_eachline)
#     print(mean_of_eachline)
    for i in range(len(file)):
        names.append(file[i][0])
    final=list(zip(names,mean_of_eachline))
#     print(final)
    for eachtuple in final:
        eachtuple=list(eachtuple)
        nahai.append(eachtuple)
#     print(nahai)
#     print(nahai)

    file=open(output_file_name,"w")
    for i in range(len(nahai)):#توی اینجا داره اون خروجی رو می سازه
        file.writelines(nahai[i][0])# تا وقتی اسلش n نباشه
        #نمی ره خط بعدی
        file.write(",")
        file.write(nahai[i][1])
        file.write("\n")
#         print()
    file.close()
    file=open(output_file_name)
    print(file.read())

from statistics import mean
def calculate_sorted_averages(input_file_name,output_file_name):
    list_adad=[]
    mean_of_eachline=[]
    nahai=[]
    nahai_sorted=[]
    names=[]
    file=[]
    f=open(input_file_name)
    for line in f:
        line=line.strip().split(",")
        file.append(line)
#         print(line)
        adad=map(float,line[1:])
        list_adad.append(list(adad))
#     print("file= %s \n  \nlist_adad=%s \n " %(file, list_adad)) it is written for checking the output
#         print(list_adad)
    f.close()
    for element in list_adad:
        element=mean(element)
        element=str(element)
        mean_of_eachline.append(element)
#     print(mean_of_eachline)
#     print(mean_of_eachline)
    for i in range(len(file)):
        names.append(file[i][0])
    final=list(zip(names,mean_of_eachline))#inja keys v value sakhte mishe
#     print(final)
    for eachtuple in final:
        eachtuple=list(eachtuple)
        nahai.append(eachtuple)

#     print(nahai)
    nahai_sorted=sorted(nahai, key = lambda x: float(x[1]))# inja ham bar asase horof alefba v ham adad check mikone
    print("nahai_sorted ", nahai_sorted,"\n")
    miangin=[]
    for i in range(len(nahai_sorted)):
        b=float(nahai_sorted[i][1])
        miangin.append(b)
    print("miangin ",miangin,"\n")
    esm=[]
    for i in range(len(nahai_sorted)):
        a=nahai_sorted[i][0]
        esm.append(a)
    if all(x == miangin[0] for x in miangin):
        esm=sorted(esm)
    # print("esm ", esm,"\n")
    f=open(output_file_name,mode="w")
    n=len(nahai_sorted)-1
    i=0
    while i<=n:
        f.write(esm[i])
        f.write(",")
        f.write(str(miangin[i]))
        f.write("\n")
        i=i+1
    f.close()
    with open(output_file_name) as f:
        print(f.read())

from statistics import mean
def calculate_three_best(input_file_name, output_file_name):
    list_adad=[]
    mean_of_eachline=[]
    nahai=[]
    nahai_sorted=[]
    names=[]
    file=[]
    f=open(input_file_name)
    for line in f:
        line=line.strip().split(",")
        file.append(line)
#         print(line)
        adad=map(float,line[1:])
        list_adad.append(list(adad))
#     print("file= %s \n  \nlist_adad=%s \n " %(file, list_adad)) it is written for checking the output
#         print(list_adad)
    f.close()
    for element in list_adad:
        element=mean(element)
        element=str(element)
        mean_of_eachline.append(element)
#     print(mean_of_eachline)
#     print(mean_of_eachline)
    for i in range(len(file)):
        names.append(file[i][0])
    final=list(zip(names,mean_of_eachline))#inja keys v value sakhte mishe
#     print(final)
    for eachtuple in final:
        eachtuple=list(eachtuple)
        nahai.append(eachtuple)

#     print(nahai)
    nahai_sorted=sorted(nahai, key = lambda x: float(x[1]))# inja ham bar asase horof alefba v ham adad check mikone
    miangin=[]
    for i in range(len(nahai_sorted)):
        b=float(nahai_sorted[i][1])
        miangin.append(b)
#     print("miangin= ",miangin)
    esm=[]
    for i in range(len(nahai_sorted)):
        a=nahai_sorted[i][0]
        esm.append(a)
#     print("esm= ",esm)
    output_list = nahai_sorted[-1:-4:-1]
    output_list = sorted(output_list, key=lambda x: float(x[1]))
    with open(output_file_name,mode="w") as f:
        output_list.reverse()
        for name,score in output_list:
            f.write(f"{name},{score}\n")
#         print("changed",output_list)

    with open(output_file_name) as f:
        print(f.read())


def calculate_three_worst(input_file_name,output_file_name):
    list_adad=[]
    mean_of_eachline=[]
    nahai=[]
    nahai_sorted=[]
    names=[]
    file=[]
    f=open(input_file_name)
    for line in f:
        line=line.strip().split(",")
        file.append(line)
#         print(line)
        adad=map(float,line[1:])
        list_adad.append(list(adad))
#     print("file= %s \n  \nlist_adad=%s \n " %(file, list_adad)) it is written for checking the output
#         print(list_adad)
    f.close()
    for element in list_adad:
        element=mean(element)
        element=str(element)
        mean_of_eachline.append(element)
#     print(mean_of_eachline)
#     print(mean_of_eachline)
    for i in range(len(file)):
        names.append(file[i][0])
    final=list(zip(names,mean_of_eachline))#inja keys v value sakhte mishe
#     print(final)
    for eachtuple in final:
        eachtuple=list(eachtuple)
        nahai.append(eachtuple)

#     print(nahai)
    nahai_sorted=sorted(nahai, key = lambda x: float(x[1]))# inja ham bar asase horof alefba v ham adad check mikone
#     print(nahai_sorted)
    miangin=[]
    for i in range(len(nahai_sorted)):
        b=float(nahai_sorted[i][1])
        miangin.append(b)
    esm=[]
    for i in range(len(nahai_sorted)):
        a=nahai_sorted[i][0]
        esm.append(a)
    f=open(output_file_name,mode="w")
    n=len(nahai_sorted)-1
    i=0
    while i<=2:

        f.write(str(miangin[i]))
        f.write("\n")
        i=i+1
    f.close()
    with open(output_file_name) as f:
        print(f.read())


from statistics import mean
def calculate_average_of_averages(input_file_name, output_file_name):
    list_adad=[]
    mean_of_eachline=[]
    nahai=[]
    nahai_sorted=[]
    names=[]
    file=[]
    f=open(input_file_name)
    for line in f:
        line=line.strip().split(",")
        file.append(line)
#         print(line)
        adad=map(float,line[1:])
        list_adad.append(list(adad))
#     print("file= %s \n  \nlist_adad=%s \n " %(file, list_adad)) it is written for checking the output
#         print(list_adad)
    f.close()
    for element in list_adad:
        element=mean(element)
        element=str(element)
        mean_of_eachline.append(element)
#     print(mean_of_eachline)
#     print(mean_of_eachline)
    for i in range(len(file)):
        names.append(file[i][0])
    final=list(zip(names,mean_of_eachline))#inja keys v value sakhte mishe
#     print(final)
    for eachtuple in final:
        eachtuple=list(eachtuple)
        nahai.append(eachtuple)

#     print(nahai)
    nahai_sorted=sorted(nahai, key = lambda x: float(x[1]))# inja ham bar asase horof alefba v ham adad check mikone
#     print(nahai_sorted)
    miangin=[]
    for i in range(len(nahai_sorted)):
        b=float(nahai_sorted[i][1])
        miangin.append(b)
    c=mean(miangin)
    c=str(c)
#     print(c)
    f=open(output_file_name,mode="w")
    f.write(c)
    f.close()
    with open(output_file_name) as f:
        print(f.read())
