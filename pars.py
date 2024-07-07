import requests
import fake_useragent
from bs4 import BeautifulSoup

def ngueu_fi(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}

    link = 'https://lk.nsuem.ru/guest/competition-lists/13/1796579497812219159'
    res = requests.get(link, headers=header).text
    soup = BeautifulSoup(res, 'lxml')
    block =soup.find('tbody',{ "class" : "text-sm" }).text
    block = block.split()
    hui_block =[]
    k=0

    for i in block[2:]:
        k+=1
        if k==1:
            hui_block.append(i)
        if k==6 or k==7:
            hui_block.append(i)
        if i=='№':
            k=0
    for x in range(2,len(hui_block),3):
        x1=hui_block[x-2]
        x2=hui_block[x-1]
        x3=hui_block[x]
        if len(x2)==11:
            if x2+' '+x3 ==snils:
                return("Ты на " + x1 +' месте в конкурсе!  \n Всего бюджетных мест 7')
        elif len(x2)==14  or len(x2) ==7:
            if x2==snils:
                return("Ты на " + x1 +' месте в конкурсе!  \n Всего бюджетных мест 7')
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'
def ngueu_pi(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}

    link = 'https://lk.nsuem.ru/guest/competition-lists/13/1796579512805807383'
    res = requests.get(link, headers=header).text
    soup = BeautifulSoup(res, 'lxml')
    block =soup.find('tbody',{ "class" : "text-sm" }).text
    block = block.split()
    hui_block =[]
    k=0

    for i in block[2:]:
        k+=1
        if k==1:
            hui_block.append(i)
        if k==6 or k==7:
            hui_block.append(i)
        if i=='№':
            k=0
    for x in range(2,len(hui_block),3):
        x1=hui_block[x-2]
        x2=hui_block[x-1]
        x3=hui_block[x]
        if len(x2)==11:
            if x2+' '+x3 ==snils:
                return("Ты на " + x1 +' месте в конкурсе! \n Всего бюджетных мест 45')
        elif len(x2)==14 or len(x2) ==7:
            if x2==snils:
                return("Ты на " + x1 +' месте в конкурсе! \n Всего бюджетных мест 45')
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'

def sibguti_fi(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link0 = 'https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&competitiveGroupID=4910044&ajax=Y'
    link2 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=2&ajax=Y&competitiveGroupID=4910044'
    link3 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=3&ajax=Y&competitiveGroupID=4910044'
    link4 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=4&ajax=Y&competitiveGroupID=4910044'
    link5 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=5&ajax=Y&competitiveGroupID=4910044'
    link6 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=6&ajax=Y&competitiveGroupID=4910044'
    link7 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=7&ajax=Y&competitiveGroupID=4910044'
    link8 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=8&ajax=Y&competitiveGroupID=4910044'


    try:
        # подтягиваем списки со всех страниц (уменьшить количество страниц????)
        res0 = requests.get(link0).text
        res2 = requests.get(link2).text
        res3 = requests.get(link3).text
        res4 = requests.get(link4).text
        res5 = requests.get(link5).text
        res6 = requests.get(link6).text
        res7 = requests.get(link7).text
        res8 = requests.get(link8).text

        #заполнение супов для поиска
        soup0 = BeautifulSoup(res0, 'lxml')
        soup2 = BeautifulSoup(res2, 'lxml')
        soup3 = BeautifulSoup(res3, 'lxml')
        soup4 = BeautifulSoup(res4, 'lxml')
        soup5 = BeautifulSoup(res5, 'lxml')
        soup6 = BeautifulSoup(res6, 'lxml')
        soup7 = BeautifulSoup(res7, 'lxml')
        soup8 = BeautifulSoup(res8, 'lxml')

        #Поиск последнего обновления списка
        last_update=soup0.find('h2').text

        #Подтягиваю таблицу с первой страницы чтобы избавиться от мусора
        block0=soup0.find('tbody').text.split()

        konkurs=[]
        k=0
        kk=0
        for i in range(len(block0)):
            if block0[i-1]=='код':
                k+=1
                konkurs.append(k)
                if len(block0[i])==11:
                    konkurs.append(block0[i]+' '+block0[i+1])
                if len(block0[i])==14 or len(block0[i])==9:
                    konkurs.append(block0[i])

        block2=soup2.find('body').text.split()
        block3=soup3.find('body').text.split()
        block4=soup4.find('body').text.split()
        block5=soup5.find('body').text.split()
        block6=soup6.find('body').text.split()
        block7=soup7.find('body').text.split()
        block8=soup8.find('body').text.split()
        for i in range(len(block2)):
            if len(block2[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i]+' '+block2[i+1])
            if len(block2[i])==14 or len(block2[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i])

        for i in range(len(block3)):
            if len(block3[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i]+' '+block3[i+1])
            if len(block3[i])==14 or len(block3[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i])

        for i in range(len(block4)):
            if len(block4[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i]+' '+block4[i+1])
            if len(block4[i])==14 or len(block4[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i])

        for i in range(len(block5)):
            if len(block5[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i]+' '+block5[i+1])
            if len(block5[i])==14 or len(block5[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i])

        for i in range(len(block6)):
            if len(block6[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i]+' '+block6[i+1])
            if len(block6[i])==14 or len(block6[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i])

        for i in range(len(block7)):
            if len(block7[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i]+' '+block7[i+1])
            if len(block7[i])==14 or len(block7[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i])

        for i in range(len(block8)):
            if len(block8[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i]+' '+block8[i+1])
            if len(block8[i])==14 or len(block8[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i])
    except requests.exceptions.ConnectionError:
        return('Сервер не отвечает :( \nПопробуй позже')
    if snils in konkurs:
        return('Ты на '+str(konkurs[konkurs.index(snils)-1])+' месте! \nВсего бюджетных 30\n'+last_update)
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'


def sibguti_pi(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link0 = 'https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&competitiveGroupID=4910066&ajax=Y'
    link2 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=2&ajax=Y&competitiveGroupID=4910066'
    link3 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=3&ajax=Y&competitiveGroupID=4910066'
    link4 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=4&ajax=Y&competitiveGroupID=4910066'
    link5 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=5&ajax=Y&competitiveGroupID=4910066'
    link6 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=6&ajax=Y&competitiveGroupID=4910066'
    link7 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=7&ajax=Y&competitiveGroupID=4910066'
    link8 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=8&ajax=Y&competitiveGroupID=4910066'


    try:
        # подтягиваем списки со всех страниц (уменьшить количество страниц????)
        res0 = requests.get(link0).text
        res2 = requests.get(link2).text
        res3 = requests.get(link3).text
        res4 = requests.get(link4).text
        res5 = requests.get(link5).text
        res6 = requests.get(link6).text
        res7 = requests.get(link7).text
        res8 = requests.get(link8).text

        #заполнение супов для поиска
        soup0 = BeautifulSoup(res0, 'lxml')
        soup2 = BeautifulSoup(res2, 'lxml')
        soup3 = BeautifulSoup(res3, 'lxml')
        soup4 = BeautifulSoup(res4, 'lxml')
        soup5 = BeautifulSoup(res5, 'lxml')
        soup6 = BeautifulSoup(res6, 'lxml')
        soup7 = BeautifulSoup(res7, 'lxml')
        soup8 = BeautifulSoup(res8, 'lxml')

        #Поиск последнего обновления списка
        last_update=soup0.find('h2').text

        #Подтягиваю таблицу с первой страницы чтобы избавиться от мусора
        block0=soup0.find('tbody').text.split()

        konkurs=[]
        k=0
        kk=0
        for i in range(len(block0)):
            if block0[i-1]=='код':
                k+=1
                konkurs.append(k)
                if len(block0[i])==11:
                    konkurs.append(block0[i]+' '+block0[i+1])
                if len(block0[i])==14 or len(block0[i])==9:
                    konkurs.append(block0[i])

        block2=soup2.find('body').text.split()
        block3=soup3.find('body').text.split()
        block4=soup4.find('body').text.split()
        block5=soup5.find('body').text.split()
        block6=soup6.find('body').text.split()
        block7=soup7.find('body').text.split()
        block8=soup8.find('body').text.split()
        for i in range(len(block2)):
            if len(block2[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i]+' '+block2[i+1])
            if len(block2[i])==14 or len(block2[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i])

        for i in range(len(block3)):
            if len(block3[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i]+' '+block3[i+1])
            if len(block3[i])==14 or len(block3[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i])

        for i in range(len(block4)):
            if len(block4[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i]+' '+block4[i+1])
            if len(block4[i])==14 or len(block4[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i])

        for i in range(len(block5)):
            if len(block5[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i]+' '+block5[i+1])
            if len(block5[i])==14 or len(block5[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i])

        for i in range(len(block6)):
            if len(block6[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i]+' '+block6[i+1])
            if len(block6[i])==14 or len(block6[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i])

        for i in range(len(block7)):
            if len(block7[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i]+' '+block7[i+1])
            if len(block7[i])==14 or len(block7[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i])

        for i in range(len(block8)):
            if len(block8[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i]+' '+block8[i+1])
            if len(block8[i])==14 or len(block8[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i])

    except requests.exceptions.ConnectionError:
        return('Сервер не отвечает :( \nПопробуй позже')
    if snils in konkurs:
        return('Ты на '+str(konkurs[konkurs.index(snils)-1])+' месте! \nВсего бюджетных 30\n'+last_update)
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'


def sibguti_ist(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link0 = 'https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&competitiveGroupID=4910060&ajax=Y'
    link2 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=2&ajax=Y&competitiveGroupID=4910060'
    link3 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=3&ajax=Y&competitiveGroupID=4910060'
    link4 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=4&ajax=Y&competitiveGroupID=4910060'
    link5 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=5&ajax=Y&competitiveGroupID=4910060'
    link6 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=6&ajax=Y&competitiveGroupID=4910060'
    link7 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=7&ajax=Y&competitiveGroupID=4910060'
    link8 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=8&ajax=Y&competitiveGroupID=4910060'


    try:
        # подтягиваем списки со всех страниц (уменьшить количество страниц????)
        res0 = requests.get(link0).text
        res2 = requests.get(link2).text
        res3 = requests.get(link3).text
        res4 = requests.get(link4).text
        res5 = requests.get(link5).text
        res6 = requests.get(link6).text
        res7 = requests.get(link7).text
        res8 = requests.get(link8).text

        #заполнение супов для поиска
        soup0 = BeautifulSoup(res0, 'lxml')
        soup2 = BeautifulSoup(res2, 'lxml')
        soup3 = BeautifulSoup(res3, 'lxml')
        soup4 = BeautifulSoup(res4, 'lxml')
        soup5 = BeautifulSoup(res5, 'lxml')
        soup6 = BeautifulSoup(res6, 'lxml')
        soup7 = BeautifulSoup(res7, 'lxml')
        soup8 = BeautifulSoup(res8, 'lxml')

        #Поиск последнего обновления списка
        last_update=soup0.find('h2').text

        #Подтягиваю таблицу с первой страницы чтобы избавиться от мусора
        block0=soup0.find('tbody').text.split()

        konkurs=[]
        k=0
        kk=0
        for i in range(len(block0)):
            if block0[i-1]=='код':
                k+=1
                konkurs.append(k)
                if len(block0[i])==11:
                    konkurs.append(block0[i]+' '+block0[i+1])
                if len(block0[i])==14 or len(block0[i])==9:
                    konkurs.append(block0[i])

        block2=soup2.find('body').text.split()
        block3=soup3.find('body').text.split()
        block4=soup4.find('body').text.split()
        block5=soup5.find('body').text.split()
        block6=soup6.find('body').text.split()
        block7=soup7.find('body').text.split()
        block8=soup8.find('body').text.split()
        for i in range(len(block2)):
            if len(block2[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i]+' '+block2[i+1])
            if len(block2[i])==14 or len(block2[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i])

        for i in range(len(block3)):
            if len(block3[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i]+' '+block3[i+1])
            if len(block3[i])==14 or len(block3[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i])

        for i in range(len(block4)):
            if len(block4[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i]+' '+block4[i+1])
            if len(block4[i])==14 or len(block4[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i])

        for i in range(len(block5)):
            if len(block5[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i]+' '+block5[i+1])
            if len(block5[i])==14 or len(block5[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i])

        for i in range(len(block6)):
            if len(block6[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i]+' '+block6[i+1])
            if len(block6[i])==14 or len(block6[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i])

        for i in range(len(block7)):
            if len(block7[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i]+' '+block7[i+1])
            if len(block7[i])==14 or len(block7[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i])

        for i in range(len(block8)):
            if len(block8[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i]+' '+block8[i+1])
            if len(block8[i])==14 or len(block8[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i])

    except requests.exceptions.ConnectionError:
        return('Сервер не отвечает :( \nПопробуй позже')
    if snils in konkurs:
        return('Ты на '+str(konkurs[konkurs.index(snils)-1])+' месте! \nВсего бюджетных 44\n'+last_update)
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'

def sibguti_ivt(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link0 = 'https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&competitiveGroupID=4910054&ajax=Y'
    link2 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=2&ajax=Y&competitiveGroupID=4910054'
    link3 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=3&ajax=Y&competitiveGroupID=4910054'
    link4 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=4&ajax=Y&competitiveGroupID=4910054'
    link5 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=5&ajax=Y&competitiveGroupID=4910054'
    link6 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=6&ajax=Y&competitiveGroupID=4910054'
    link7 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=7&ajax=Y&competitiveGroupID=4910054'
    link8 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=8&ajax=Y&competitiveGroupID=4910054'


    try:
        # подтягиваем списки со всех страниц (уменьшить количество страниц????)
        res0 = requests.get(link0).text
        res2 = requests.get(link2).text
        res3 = requests.get(link3).text
        res4 = requests.get(link4).text
        res5 = requests.get(link5).text
        res6 = requests.get(link6).text
        res7 = requests.get(link7).text
        res8 = requests.get(link8).text

        #заполнение супов для поиска
        soup0 = BeautifulSoup(res0, 'lxml')
        soup2 = BeautifulSoup(res2, 'lxml')
        soup3 = BeautifulSoup(res3, 'lxml')
        soup4 = BeautifulSoup(res4, 'lxml')
        soup5 = BeautifulSoup(res5, 'lxml')
        soup6 = BeautifulSoup(res6, 'lxml')
        soup7 = BeautifulSoup(res7, 'lxml')
        soup8 = BeautifulSoup(res8, 'lxml')

        #Поиск последнего обновления списка
        last_update=soup0.find('h2').text

        #Подтягиваю таблицу с первой страницы чтобы избавиться от мусора
        block0=soup0.find('tbody').text.split()

        konkurs=[]
        k=0
        kk=0
        for i in range(len(block0)):
            if block0[i-1]=='код':
                k+=1
                konkurs.append(k)
                if len(block0[i])==11:
                    konkurs.append(block0[i]+' '+block0[i+1])
                if len(block0[i])==14 or len(block0[i])==9:
                    konkurs.append(block0[i])

        block2=soup2.find('body').text.split()
        block3=soup3.find('body').text.split()
        block4=soup4.find('body').text.split()
        block5=soup5.find('body').text.split()
        block6=soup6.find('body').text.split()
        block7=soup7.find('body').text.split()
        block8=soup8.find('body').text.split()
        for i in range(len(block2)):
            if len(block2[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i]+' '+block2[i+1])
            if len(block2[i])==14 or len(block2[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i])

        for i in range(len(block3)):
            if len(block3[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i]+' '+block3[i+1])
            if len(block3[i])==14 or len(block3[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i])

        for i in range(len(block4)):
            if len(block4[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i]+' '+block4[i+1])
            if len(block4[i])==14 or len(block4[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i])

        for i in range(len(block5)):
            if len(block5[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i]+' '+block5[i+1])
            if len(block5[i])==14 or len(block5[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i])

        for i in range(len(block6)):
            if len(block6[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i]+' '+block6[i+1])
            if len(block6[i])==14 or len(block6[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i])

        for i in range(len(block7)):
            if len(block7[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i]+' '+block7[i+1])
            if len(block7[i])==14 or len(block7[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i])

        for i in range(len(block8)):
            if len(block8[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i]+' '+block8[i+1])
            if len(block8[i])==14 or len(block8[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i])

    except requests.exceptions.ConnectionError:
        return('Сервер не отвечает :( \nПопробуй позже')
    if snils in konkurs:
        return('Ты на '+str(konkurs[konkurs.index(snils)-1])+' месте! \nВсего бюджетных 165\n'+last_update)
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'

def sibguti_ib(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link0 = 'https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&competitiveGroupID=4910071&ajax=Y'
    link2 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=2&ajax=Y&competitiveGroupID=4910071'
    link3 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=3&ajax=Y&competitiveGroupID=4910071'
    link4 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=4&ajax=Y&competitiveGroupID=4910071'
    link5 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=5&ajax=Y&competitiveGroupID=4910071'
    link6 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=6&ajax=Y&competitiveGroupID=4910071'
    link7 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=7&ajax=Y&competitiveGroupID=4910071'
    link8 ='https://sibsutis.ru/abitur/konkursnye-spiski/?academic_degree=bachelor&type_list=competitve_lists&basis=budget&page=8&ajax=Y&competitiveGroupID=4910071'


    try:
        # подтягиваем списки со всех страниц (уменьшить количество страниц????)
        res0 = requests.get(link0).text
        res2 = requests.get(link2).text
        res3 = requests.get(link3).text
        res4 = requests.get(link4).text
        res5 = requests.get(link5).text
        res6 = requests.get(link6).text
        res7 = requests.get(link7).text
        res8 = requests.get(link8).text

        #заполнение супов для поиска
        soup0 = BeautifulSoup(res0, 'lxml')
        soup2 = BeautifulSoup(res2, 'lxml')
        soup3 = BeautifulSoup(res3, 'lxml')
        soup4 = BeautifulSoup(res4, 'lxml')
        soup5 = BeautifulSoup(res5, 'lxml')
        soup6 = BeautifulSoup(res6, 'lxml')
        soup7 = BeautifulSoup(res7, 'lxml')
        soup8 = BeautifulSoup(res8, 'lxml')

        #Поиск последнего обновления списка
        last_update=soup0.find('h2').text

        #Подтягиваю таблицу с первой страницы чтобы избавиться от мусора
        block0=soup0.find('tbody').text.split()

        konkurs=[]
        k=0
        kk=0
        for i in range(len(block0)):
            if block0[i-1]=='код':
                k+=1
                konkurs.append(k)
                if len(block0[i])==11:
                    konkurs.append(block0[i]+' '+block0[i+1])
                if len(block0[i])==14 or len(block0[i])==9:
                    konkurs.append(block0[i])

        block2=soup2.find('body').text.split()
        block3=soup3.find('body').text.split()
        block4=soup4.find('body').text.split()
        block5=soup5.find('body').text.split()
        block6=soup6.find('body').text.split()
        block7=soup7.find('body').text.split()
        block8=soup8.find('body').text.split()
        for i in range(len(block2)):
            if len(block2[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i]+' '+block2[i+1])
            if len(block2[i])==14 or len(block2[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block2[i])

        for i in range(len(block3)):
            if len(block3[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i]+' '+block3[i+1])
            if len(block3[i])==14 or len(block3[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block3[i])

        for i in range(len(block4)):
            if len(block4[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i]+' '+block4[i+1])
            if len(block4[i])==14 or len(block4[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block4[i])

        for i in range(len(block5)):
            if len(block5[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i]+' '+block5[i+1])
            if len(block5[i])==14 or len(block5[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block5[i])

        for i in range(len(block6)):
            if len(block6[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i]+' '+block6[i+1])
            if len(block6[i])==14 or len(block6[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block6[i])

        for i in range(len(block7)):
            if len(block7[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i]+' '+block7[i+1])
            if len(block7[i])==14 or len(block7[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block7[i])

        for i in range(len(block8)):
            if len(block8[i])==11:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i]+' '+block8[i+1])
            if len(block8[i])==14 or len(block8[i])==9:
                k+=1
                konkurs.append(k)
                konkurs.append(block8[i])

    except requests.exceptions.ConnectionError:
        return('Сервер не отвечает :( \nПопробуй позже')
    if snils in konkurs:
        return('Ты на '+str(konkurs[konkurs.index(snils)-1])+' месте! \nВсего бюджетных 22\n'+last_update)
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'


def kemgu_fi(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link = 'https://kemsu.ru/abiturient/progress-campaign/online-lists/?mission=2&level=4949&branch=4&competition=2&speciality=85&sortFlag=1&snils='
    try:
        res = requests.get(link,headers=header).text
        soup=BeautifulSoup(res,'lxml')
        block=soup.find('table')
    except requests.exceptions.ConnectionError:
        return ('Попробуй еще раз :(')
    tablica=block.text.split()[37:]
    kk=0
    k=0
    konkurs=[]
    for i in range(len(tablica)):
        kk+=1
        if len(tablica[i])==11 and tablica[i][3]=='-':
            k+=1
            konkurs.append(k)
            konkurs.append(tablica[i]+' '+tablica[i+1][:2])
        if kk==49:
            kk=0
    if snils in konkurs:
        return 'Ты на ' + str(konkurs[konkurs.index(snils)-1]) +' месте из 16 бюджетных!'
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'




def kemgu_pi(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link = 'https://kemsu.ru/abiturient/progress-campaign/online-lists/?mission=2&level=4949&branch=4&competition=2&speciality=93&sortFlag=1&snils='
    try:
        res = requests.get(link,headers=header).text
        soup=BeautifulSoup(res,'lxml')
        block=soup.find('table')
    except requests.exceptions.ConnectionError:
        return ('Попробуй еще раз :(')
    tablica=block.text.split()[37:]
    kk=0
    k=0
    konkurs=[]
    for i in range(len(tablica)):
        kk+=1
        if len(tablica[i])==11 and tablica[i][3]=='-':
            k+=1
            konkurs.append(k)
            konkurs.append(tablica[i]+' '+tablica[i+1][:2])
        if kk==49:
            kk=0
    if snils in konkurs:
        return 'Ты на ' + str(konkurs[konkurs.index(snils)-1] )+' месте из 16 бюджетных!'
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'

def kemgu_mo(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link = 'https://kemsu.ru/abiturient/progress-campaign/online-lists/?mission=2&level=4949&branch=4&competition=2&speciality=8&sortFlag=1&snils='
    try:
        res = requests.get(link,headers=header).text
        soup=BeautifulSoup(res,'lxml')
        block=soup.find('table')
    except requests.exceptions.ConnectionError:
        return ('Попробуй еще раз :(')
    tablica=block.text.split()[37:]
    kk=0
    k=0
    konkurs=[]
    for i in range(len(tablica)):
        kk+=1
        if len(tablica[i])==11 and tablica[i][3]=='-':
            k+=1
            konkurs.append(k)
            konkurs.append(tablica[i]+' '+tablica[i+1][:2])
        if kk==49:
            kk=0
    if snils in konkurs:
        return 'Ты на ' + str(konkurs[konkurs.index(snils)-1]) +' месте из 13 бюджетных!'
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'

def kemgu_pim(snils):
    user = fake_useragent.UserAgent().random

    header = {'user-agent': user}


    #все страницы со списками
    link = 'https://kemsu.ru/abiturient/progress-campaign/online-lists/?mission=2&level=4949&branch=4&competition=2&speciality=12&sortFlag=1&snils='
    try:
        res = requests.get(link,headers=header).text
        soup=BeautifulSoup(res,'lxml')
        block=soup.find('table')
    except requests.exceptions.ConnectionError:
        return ('Попробуй еще раз :(')
    tablica=block.text.split()[37:]
    kk=0
    k=0
    konkurs=[]
    for i in range(len(tablica)):
        kk+=1
        if len(tablica[i])==11 and tablica[i][3]=='-':
            k+=1
            konkurs.append(k)
            konkurs.append(tablica[i]+' '+tablica[i+1][:2])
        if kk==49:
            kk=0
    if snils in konkurs:
        return 'Ты на ' + str(konkurs[konkurs.index(snils)-1]) +' месте из 14 бюджетных!'
    return 'Не смог найти твой СНИЛС в списках :( \n попробуй ввести свой снилс как XXX-XXX-XXX-XX'