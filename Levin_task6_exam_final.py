
# coding: utf-8

# In[13]:

from requests import get


class Employee:
    """Конструктор:"""
    def __init__(self, page):
        
        data = get(page).content #Загружаем исходный код страницы
        input_data = data.decode()
  
        #Ищем имя:
        index_name_begin = input_data.find("Сотрудники - ") + len("Сотрудники - ")
        index_name_end = input_data.find(" — Национальный исследовательский университет «Высшая школа экономики»")
        employee_name = input_data[index_name_begin:index_name_end]
        
        #Ищем телефон:
        index_tel_begin = input_data.find("Телефон:") + len("Телефон:") + 4
        index_tel_end = input_data.find("Электронная почта:") - 9
        employee_phone = input_data[index_tel_begin:index_tel_end]
        
        #Ищем почту:
        index_email_begin = input_data.find("Электронная почта:") + len("Электронная почта:<br><script>hseEObfuscator(")
        index_email_end = input_data.find("Адрес") - len(");</script></dd><dd>")
        employee_almost_email = input_data[index_email_begin:index_email_end]
        index_new_email_begin = employee_almost_email.find("[") + 1
        index_new_email_end = employee_almost_email.find("]")
        employee_better_email = employee_almost_email[index_new_email_begin:index_new_email_end]
        employee_email = ""
        #Исправим почту, она хранится очень плохо, удалим запятые и кавычки:
        for i in employee_better_email:
            if (i != '"') and (i != ','):
                employee_email += i
    
    
        self.info_name = employee_name
        self.info_email = employee_email
        self.info_phone = employee_phone
        
        #Ищем ключевые слова
        index_keyword_begin = input_data.find('<a class="tag tag_small" href="/org/persons/?intst=')
        index_keyword_end = input_data.find('</div></div><div class="b-person-data "')
        keywords_base = input_data[index_keyword_begin:index_keyword_end]
        keywords_list = keywords_base.split('<a class="tag tag_small" href="/org/persons/?intst=')
        key = []
        num = []
        for info in keywords_list:
            num_index_end = info.find('">')
            number = ""
            number = info[0:num_index_end]                          
            num.append(number)
            key_index_end = info.find("<")
            key_buf = info[num_index_end + 2:key_index_end]     
            key.append(key_buf)                          
        key_ans = []
        for i in range(1,len(num)):
            key_ans.append((num[i],key[i]))
        self.info_input_data_page = page
        self.info_keywords = key_ans
        
    """Конец конструктора."""
    

    """Далее реализуем методы доступа, обеспечим, чтобы данные были доступны только для чтения:"""
    @property
    def homepage(self):
        return self.info_input_data_page
    
    @property
    def full_name(self):
        return self.info_name

    @property
    def phone(self):
        return self.info_phone

    @property
    def email(self):
        return self.info_email
     
    @property
    def keywords(self):
        return self.info_keywords

TimorinVA = Employee("http://www.hse.ru/staff/vtimorin")
print(TimorinVA.homepage)
print(TimorinVA.full_name)
print(TimorinVA.phone)
print(TimorinVA.email)
print(TimorinVA.keywords)