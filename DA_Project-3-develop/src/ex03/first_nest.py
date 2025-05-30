import sys
import os

class Research:
    def __init__(self, put):
        self.put = put

    def file_reader(self,has_header=True):
        flag = 1
        try:
            with open(self.put, 'r') as f:
                data =  f.read()
        except :
            print(f"Не могу открыть файл {self.put}")
            flag = 0

        if flag == 1:  
            start_index = 1 if has_header else 0
            lines = data.split('\n')
            if start_index == 1:
                if len(lines) < 2:
                    print("Файл должен содержать как минимум заголовок и одну строку данных.")
                    flag = 0

                head = lines[0].split(',')
                if len(head) != 2 and flag == 1:
                    print("Некорректный формат заголовка. Должно быть 2 столбца, разделённые запятой.")
                    flag = 0
            else:
                if len(lines) < 1:
                    print("Файл не должен быть пустым.")
                    flag = 0

            if flag != 0:
                data = []
                start_index = 1 if has_header else 0
                for line in lines[start_index:] :
                    part = line.split(',')
                    if len(part) != 2:
                        print("Некорректная строка данных. Должно быть 2 столбца, разделённые запятой.")
                        flag = 0
                    
                    if flag == 1 and not ((part[0]== '1' and part[1]== '0') or (part[0]== '0' and part[1]== '1')):
                        print(f"Некорректная строка данных: {line}. Допустимы только '0,1' или '1,0'.")
                        flag = 0
                    data.append([int(part[0]), int(part[1])])
                if flag == 1:
                    return data

    class Calculations:
        def counts(self,data):
            orel = 0
            reshka = 0
            for line in data:
                if line == [1, 0]:
                    orel = orel  + 1
                elif line == [0, 1]:
                    reshka = reshka + 1
            return orel, reshka
                    
        def fractions(self,orel, reshka):
            total = orel + reshka
            if total == 0:
                return 0.0, 0.0
            else:
                return (orel / total * 100, reshka / total * 100)

if __name__ == '__main__':
    flag = 1
    if len(sys.argv) < 2:
        print("Использование: python3 first_nest.py <путь_к_файлу.csv>")
        flag =0 
    if flag == 1:
        pr_re = Research(sys.argv[1])
        f_data = pr_re.file_reader(has_header=True)
        if f_data != None :
            print(f_data)
            
            calc = pr_re.Calculations()
            orel, reshka = calc.counts(f_data)
            print(orel, reshka)

            heads_perc, tails_perc = calc.fractions(orel, reshka)
            print(heads_perc, tails_perc)