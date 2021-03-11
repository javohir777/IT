art = [ ] 
carObj = {
    'name':"LEONARDO DAVINCHI",
    'tavaludi':"1452",
    'vafotyili':"1519",
    'ishlar':"3",
}
art.append(carObj)
carObj = {
    'name':"MIKIANJELO KARVADJO",
    'tavaludi':"1571",
    'vafotyili':"1610",
    'ishlar':"3",
}
art.append(carObj)
carObj = {
    'name':"ANDREY AMANTENY",
    'tavaludi':"1431",
    'vafotyili':"1506",
    'ishlar':"3",
}
art.append(carObj)

carObj = {
    'name':"DJOTTO",
    'tavaludi':"1266",
    'vafotyili':"1337",
    'ishlar':"3",
}
art.append(carObj)

carObj = {
    'name':"IVAN SHISHKIN",
    'tavaludi':"1832",
    'vafotyili':"1898",
    'ishlar':"3",
}
art.append(carObj)

carObj = {
    'name':"NIKOLAYEVICH KRAMSKOY",
    'tavaludi':"1837",
    'vafotyili':"1887",
    'ishlar':"3",
}
art.append(carObj)

carObj = {
    'name':"VAN GOG",
    'tavaludi':"1853",
    'vafotyili':"1890",
    'ishlar':"3",
}
art.append(carObj)

rasmlar = []




print ("\n\n\n--------------------------------------------------------------------------")
print ("\t\t ASSALOMU ALEKUM \t")
print ("\t Saytimiz rassomchilik to'grisida\n")
print ("--------------------------------------------------------------------------")
print("\t1)\t UZBEK tilida")
print("\t2)\t РУССКИЙ язык")
print ("--------------------------------------------------------------------------")
print ("Tizim tilini tanlang\t  |\tВыберите язык")
TizmTili = int(input("\t\t\t1 | 2 : "))

while TizmTili == 1:
    def menyu():
        print ("\n--------------------------------------------------------------------------")
        print ("\t\t\t***MENYU***")
        print ("____________________________________________________________________________")
        print ("\t1)\tRassomlar haqida")
        print ("\t2)\tRassomlarni ishi haqida")
        print ("\t3)\tRassom qoshish")
        print ("\t4)\tIsh qo'shish")
        print ("\t5)\tRassom o'chirish")
        print ("\t6)\tIsh o'chirish") 
        print ("\n\t0)\t Chiqish")      
        print ("\n--------------------------------------------------------------------------")
    def rassomlar():
        print ("\n--------------------------------------------------------------------------")
        print ("\t\t\t***RASSOMLAR***")
        print("\n---------------------------------------------------------------------------------------")
        print("No\t", "Ismi\t\t\t","Tug'ulgan yili\t", "Vafot etkan yili\t", "Saytdagi ishlari")
        if len(art) == 0:
            print("RO'YHAT BO'SH")
            return
        if len(art) > 0:
            s= 1
            for nameArt in art:
                print ("_______________________________________________________________________________________________")
                print (s,'\t', nameArt['name'],'\t',nameArt['tavaludi'],'\t\t\t',nameArt['vafotyili'],'\t\t\t', nameArt['ishlar'])
                s+=1

    def ishlar():
        if len(rasmlar) == 0:
            print("Ishlar hali tayyor emas!!!")
        print ("\n--------------------------------------------------------------------------")
        st ='Rasmlar'
        print ("\t\t\t***", st.upper(), '***')
        print("\n---------------------------------------------------------------------------------------")
        print("No\t", "Rasmlar\t\t","Rassom\t\t", "Sana\t", "Stil")
        if len(rasmlar) > 0:
            s= 1
            for rasm in rasmlar:
                print ("_______________________________________________________________________________________________")
                print (s,'\t', rasm['IshNomi'],'\t',rasm['Rassom'],'\t\t',rasm['sana'],'\t\t\t', rasm['stil'])
                s+=1
        

    def rassombor(art1):
        for name1 in art:
            if name1['name'] == art1:
                return True
        return False
    
    def AddNewRassom() :
        print("\n---------------------------------------------------------------------------------------")
        name = input("Rassom Ismini kiriting:")

        if len(name) == 0:
            print ("\t!!!!!!**Rassom ismi bo'sh bulishi mumkin emas**!!!!!!")
            print("---------------------------------------------------------------------------------------\n")
            return

        if rassombor(name):
            print("\n\t\tBu ismdagi rassom sistemada mavjut")
            print("---------------------------------------------------------------------------------------\n")
            return
        tavaludi =input("\t\tRassom tug'ulgan sana  :")
        vfotyili =input("\t\tVafot etkan sana    :")
        ishlari = input("\t\tIshlar soni   :")

        
        carObj = {
            'name':name,
            'tavaludi':tavaludi,
            'vafotyili':vfotyili,
            'ishlar':ishlari,
        }

    
        art.append(carObj)
        print("\t\tRassom royhatga qoshildi.!!!!")
        print("---------------------------------------------------------------------------------------\n")

    def rasmbor(art1):
        for name1 in rasmlar:
            if name1['name'] == art1:
                return True
        return False
    def addrasm():
        q = input("Ishni nomi:")
        if len(q) == 0:
            print ("\t!!!!!!**Ish nomi bo'sh bulishi mumkin emas**!!!!!!")
            print("---------------------------------------------------------------------------------------\n")
            return

        if rasmbor(q):
            print("\n\t\tBu ismdagi rasim sistemada mavjut")
            print("---------------------------------------------------------------------------------------\n")
            return
        s =input("Ishni chizgan rassom :")
        g =input("Chizilgan sana :")
        h =input("Nima orqali chizilgan :")
        carObj = {
            'IshNomi':q,
            'Rassom':s,
            'sana':g,
            'stil':h,
        }
        rasmlar.append(carObj)


    def rassomminus():
        if len(rasmlar) == 0 :
            print("\t\tROYXAT BO'SH")

    def deletart() :
        print("\n---------------------------------------------------------------------------------------")
        ismi = input("O'chirmoqchi bugan rassomingizni ismi :")
        for ismi1 in art:
            if ismi1['name'] == ismi:
                art.remove(ismi1)
                print("\n\n\t\t Rassom o'chirish arizangiz mufoqyatli amalga oshdi!!!!")
                break
        print("---------------------------------------------------------------------------------------\n")


    
    def deletish() :
        if len(rasmlar) == 0:
            print("Rasmlar ro'yhati bo'sh!!!!")
            return
        print("\n---------------------------------------------------------------------------------------")
        nomi = input("O'chirmoqchi bugan rasmingizni nomi :")
        for nom in rasmlar:
            if ismi1['name'] == ismi:
                cars.remove(car)
                print("\n\n\t\t Ish o'chirish arizangiz mufoqyatli amalga oshdi!!!!")
                break
        print("---------------------------------------------------------------------------------------\n")



    def start():
        menyu()
        tanlang=input("\t\tMenyuni tanlang :")
        

        if tanlang == '1':
            rassomlar()
        elif tanlang == '2':
            ishlar()
        elif tanlang == '3':
            AddNewRassom()
        elif tanlang == '4' :
            addrasm()
        elif tanlang == '5' :
            deletart()
        elif tanlang == '6' :
            deletish()
        else :
            print ("\t\tNo'to'gri son kiritingiz!!!!")

        print ("-------------------------------------------------------------------------------------------------------")
        
    print ("-------------------------------------------------------------------------------------------------------")
    u =int(input("\n\t\tCHIQMOQCHI BO'LSANGIZ 0 NI KIRITING davom etirmoqch bolsangiz 1:"))
    if u == 0:
        print ("\t\tHAYR SALOMAT BOLING")
        break
    else:
        start()

    


while TizmTili == 2:
    def menyu():
        print ("\n--------------------------------------------------------------------------")
        print ("\t\t\t***MENYU***")
        print ("____________________________________________________________________________")
        print ("\t1)\tО художниках")
        print ("\t2)\tО творчестве художников")
        print ("\t3)\tДобавить художника")
        print ("\t4)\tДобавить работу")
        print ("\t5)\tУдалить художника")
        print ("\t6)\tРаботу удалить")      
        print ("\n--------------------------------------------------------------------------")
    def rassomlar():
        print ("\n--------------------------------------------------------------------------")
        st ='Художники'
        print ("\t\t\t***", st.upper(), '***')
        print("\n---------------------------------------------------------------------------------------")
        print("No\t", "Имя\t\t\t","Год рождения\t", "Год смерти\t", "Работы на участке")
        if len(art) == 0:
            print("СПИСОК ПУСТОЙ")
            return
        if len(art) > 0:
            s= 1
            for nameArt in art:
                print ("_______________________________________________________________________________________________")
                print (s,'\t', nameArt['name'],'\t',nameArt['tavaludi'],'\t\t\t',nameArt['vafotyili'],'\t\t\t', nameArt['ishlar'])
                s+=1

    def ishlar():
        if len(rasmlar) == 0:
            print("Вещи еще не готовы!!!")
        print ("\n--------------------------------------------------------------------------")
        st ='Работы'
        print ("\t\t\t***", st.upper(), '***')
        print("\n---------------------------------------------------------------------------------------")
        print("No\t", "Работа\t\t","Художник\t\t", "Год\t", "Стилы")
        if len(rasmlar) > 0:
            s= 1
            for rasm in rasmlar:
                print ("_______________________________________________________________________________________________")
                print (s,'\t', rasm['IshNomi'],'\t',rasm['Rassom'],'\t\t',rasm['sana'],'\t\t\t', rasm['stil'])
                s+=1

    def rassombor(art1):
        for name1 in art:
            if name1['name'] == art1:
                return True
        return False
    
    def AddNewRassom() :
        print("\n---------------------------------------------------------------------------------------")
        name = input("Введите имя художника:")

        if len(name) == '':
            print ("\t!!!!!!**Имя художника не может быть пустым**!!!!!!")
            print("---------------------------------------------------------------------------------------\n")
            return

        if rassombor(name):
            print("\n\t\tХудожник с этим именем находится в системе.")
            print("---------------------------------------------------------------------------------------\n")
            return
        tavaludi =input("\t\tДата рождения художника  :")
        vfotyili =input("\t\tДата смерти   :")
        ishlari = input("\t\tКоличество дел   :")

        
        carObj = {
            'name':name,
            'tavaludi':tavaludi,
            'vafotyili':vfotyili,
            'ishlar':ishlari,
        }

    
        art.append(carObj)
        print("\t\tХудожник присоединился в систему.!!!!")
        print("---------------------------------------------------------------------------------------\n")

    def rasmbor(art1):
        for name1 in rasmlar:
            if name1['name'] == art1:
                return True
        return False
    def addrasm():
        q = input("Название работы:")
        if len(q) == '':
            print ("\t!!!!!!**Название не может быть пустым**!!!!!!")
            print("---------------------------------------------------------------------------------------\n")
            return

        if rasmbor(q):
            print("\n\t\tВ официальной системе это имя есть")
            print("---------------------------------------------------------------------------------------\n")
            return
        s =input("Художник, который рисует работу:")
        g =input("Дата рисования :")
        h =input("Матерял  :")
        carObj = {
            'IshNomi':q,
            'Rassom':s,
            'sana':g,
            'stil':h,
        }
        rasmlar.append(carObj)


    def rassomminus():
        if len(rasmlar) == 0 :
            print("\t\tПУСТОЙ")

    def deletart() :
        print("\n---------------------------------------------------------------------------------------")
        ismi = input("Имя исполнителя, которого вы хотите удалить :")
        for ismi1 in art:
            if ismi1['name'] == ismi:
                art.remove(ismi1)
                print("\n\n\t\t Удаление художника сделано!!!!")
                break
        print("---------------------------------------------------------------------------------------\n")


    
    def deletish() :
        if len(rasmlar) == 0:
            print("Список картинок пуст!!!!")
            return
        print("\n---------------------------------------------------------------------------------------")
        nomi = input("Назовите изображение, которое вы хотите удалить :")
        for nom in rasmlar:
            if ismi1['name'] == ismi:
                cars.remove(car)
                print("\n\n\t\t Ваше заявление об удалении работы было сделано !!!!")
                break
        print("---------------------------------------------------------------------------------------\n")



    def start():
        menyu()
        tanlang=input("\t\tВыберите меню :")
        

        if tanlang == '1':
            rassomlar()
        elif tanlang == '2':
            ishlar()
        elif tanlang == '3':
            AddNewRassom()
        elif tanlang == '4' :
            addrasm()
        elif tanlang == '5' :
            deletart()
        elif tanlang == '6' :
            deletish()
        else :
            print ("\t\tВведите правильное число!!!!")

        print ("-------------------------------------------------------------------------------------------------------")
        
    print ("-------------------------------------------------------------------------------------------------------")
    u =int(input("\n\t\tВведите 0 если вы хотите выйти, 1 если вы хотите продолжить:"))
    if u == 0:
        print ("\t\tДО СВИДАНИЯ")
        break
    else:
        start()
        
