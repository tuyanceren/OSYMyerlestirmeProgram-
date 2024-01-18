class Student:
    def __init__(self,id,name,surname):
        self.id=id
        self.name=name
        self.surname=surname

liste=list()
bilgiler=list()
key=list()
dictionary={}


with open("student.txt", 'r') as file:
    for i in file:
        line=i.split()
        id=line[0]
        name=line[1]
        surname=line[2]
        dictionary[id] = Student(id, name, surname)
        liste.append(Student(id,name,surname))


def id_tanımla(liste):
    a=input("id giriniz:")
    for i in liste:
        if i.id==a :
            return i.name+ " "+i.surname
    return "student not found"
university_list=list()
universite=list()
university_name=list()

with open("university.txt",'r') as file:
    for j in file:
        j=j.strip()
        line = j.split(',')
        university = line[1]
        puan = line[2]
        kontenjan=line[3]
        school = puan + ", " + university
        universite.append(line)
        university_list.append(school)
        university_name.append(university)
        university_list.sort(reverse=True)
with open("answers.txt","r") as file:
    for j in file:
        line2=j.strip()
        bilgiler.append(line2)
with open("key.txt","r") as file:
    for i in file:
        line=i.strip()
        key.append(line)


def results():
    c = open("result.txt",'w')
    for bil in bilgiler:
        answersplit = bil.split()

        if answersplit[1] == 'B':
            true = 0
            false = 0
            blank = 0
            for i in range(len(answersplit[2])):
                if key[1][i] == answersplit[2][i]:
                    true = true + 1

                elif answersplit[2][i] == '-':
                    blank = blank + 1

                else:
                    false = false + 1
            for i in dictionary:
                a = dictionary.get(answersplit[0])

            c.write( a.id+","+ a.name +","+a.surname+"," +str(answersplit[1]) + "," + str(true) + "," + str(false) + "," + str(blank) + "," + str(true - (false / 4)) + "," + str((true-(false/4))*15) + "," + university_name[int(answersplit[3])-1] + "," + university_name[int(answersplit[4])-1] + "," + university_name[int(answersplit[5])-1] + "," + university_name[int(answersplit[6])-1] + "," + university_name[int(answersplit[7])-1] + "\n")

        elif answersplit[1] == 'A':
            true = 0
            false = 0
            blank = 0
            for i in range(len(answersplit[2])):
                if key[0][i] == answersplit[2][i]:
                    true = true + 1

                elif answersplit[2][i] == '-':
                    blank = blank + 1

                else:
                    false = false + 1
            for i in dictionary:
                a = dictionary.get(answersplit[0])

            c.write(a.id+","+ a.name +","+a.surname + "," +str(answersplit[1]) + "," + str(true) + "," + str(false) + "," + str(blank) + "," + str(true - (false / 4)) + "," + str((true-(false/4))*15) + "," + university_name[int(answersplit[3])-1] + "," + university_name[int(answersplit[4])-1] + "," + university_name[int(answersplit[5])-1] + "," + university_name[int(answersplit[6])-1] + "," + university_name[int(answersplit[7])-1] + "\n")
def ranking_students():
    with open('result.txt', 'r') as file:
        score_list=[]
        for point in file:
            point=point.strip()
            point=point.split(",")
            transform = float(point[8]),point[1],point[2],point[0]
            score_list.append(transform)
        score_list.sort(reverse=True)
        for i in (score_list):
            print(i[3], i[1], i[2], i[0])
öğrenciler=[]
mezun=[]

def ax():
    w = open("result.txt","r")
    result_list=[]
    for i in w:
        i=i.strip()
        i=i.split(",")
        result = [float(i[8]), i[0],i[1],i[2],i[9],i[10],i[11],i[12],i[13]]
        result_list.append(result)
    result_list.sort(reverse=True)
    for k in result_list:
        for t in bilgiler:
            t=t.split(" ")
            if int(k[1])==int(t[0]):
                if k[0] >= float(universite[int(t[3])-1][2]) and int(universite[int(t[3])-1][3])>0:
                    (universite[int(t[3])-1][3])=int(universite[int(t[3])-1][3])-1
                    öğrenciler.append(k[1] + " " + k[2] + " " + k[3] + " " + k[4])
                elif k[0] >= float(universite[int(t[4])-1][2]) and int(universite[int(t[4])-1][3])>0:
                    (universite[int(t[4])-1][3])=int(universite[int(t[4])-1][3])-1
                    öğrenciler.append(k[1] + " " + k[2] + " " + k[3] + " " + k[5])
                elif k[0] >= float(universite[int(t[5])-1][2]) and int(universite[int(t[5])-1][3])>0:
                    (universite[int(t[5])-1][3])=int(universite[int(t[5])-1][3])-1
                    öğrenciler.append(k[1] + " " + k[2] + " " + k[3] + " " + k[6])
                elif k[0] >= float(universite[int(t[6])-1][2]) and int(universite[int(t[6])-1][3])>0:
                    (universite[int(t[6])-1][3])=int(universite[int(t[6])-1][3])-1
                    öğrenciler.append(k[1] + " " + k[2] + " " + k[3] + " " + k[7])
                elif k[0] >= float(universite[int(t[7])-1][2]) and int(universite[int(t[7])-1][3])>0:
                    (universite[int(t[7])-1][3])=int(universite[int(t[7])-1][3])-1
                    öğrenciler.append(k[1] + " " + k[2] + " " + k[3] + " " + k[8])
                else:
                    mezun.append(k[1] + " " + k[2] + " " + k[3])






sıralama=[]
department=[]
def department_sıralama():
    for i in university_name:
        i=i.split("University")
        departmentof=i[1]
        sıralama.append(departmentof)
    for j in sıralama:
        if j not in department:
            department.append(j)

department_sıralama()



while True:
    print("""
lütfen işlem seçiniz.
1= id giriniz:
2= ünileri max göre  sıralamak.
3=öğrenci bilgilerini bastırmak.
4=puana göre öğrenciler
5=ünilerin bölümlerine yerleşen öğrencileri sıralamak
6=yerleşemeyen öğrenciler.
7=tüm bölümler.
çıkmak için q ya basınız.
    """)
    işlem =int(input("işlem seçiniz:"))
    if işlem==1:
        b=id_tanımla(liste)
        print(b)
    elif işlem==2:
        for i in university_list:
            print(i)
    elif işlem==3:
        results()
        print("txt yaratıldı.")
    elif işlem==4:
        ranking_students()
    elif işlem==5:
        ax()
        print(mezun)
    elif işlem==6:
        ax()
        print("MEZUN:")
        for i in mezun:
            print(i)
        print("mezuna kalan kişi sayısı:", len(mezun))
    elif işlem==7:
        for i in department:
            print(i)
    else:
        print("geçersiz işlem")