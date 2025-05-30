import sys
import os

class Research:
    def __init__(self, put):
        self.put = put

    def file_reader(self):
        flag = 1
        try:
            with open(self.put, 'r') as f:
                data =  f.read()
        except :
            print(f"Не могу открыть файл {self.put}")
            flag = 0

        if flag == 1:  
            lines = data.split('\n')
            if len(lines) < 2:
                print("Файл должен содержать как минимум заголовок и одну строку данных.")
                flag = 0

            head = lines[0].split(',')
            if len(head) != 2 and flag == 1:
                print("Некорректный формат заголовка. Должно быть 2 столбца, разделённые запятой.")
                flag = 0

            if flag != 0:
                for line in lines[1:] :
                    part = line.split(',')
                    if len(part) != 2:
                        print("Некорректная строка данных. Должно быть 2 столбца, разделённые запятой.")
                        flag = 0
                    
                    if flag == 1 and not ((part[0]== '1' and part[1]== '0') or (part[0]== '0' and part[1]== '1')):
                        print(f"Некорректная строка данных: {line}. Допустимы только '0,1' или '1,0'.")
                        flag = 0
                if flag == 1:
                    return data




if __name__ == '__main__':
    
    pr_re = Research(sys.argv[1])
    f_data = pr_re.file_reader()
    if f_data != None :
        print(f_data)