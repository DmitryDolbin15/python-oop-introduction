class Research:
    def file_reader(self):
        with open('../ex00/data.csv', 'r') as f:
            return f.read()

if __name__ == '__main__':
    pr_re = Research()
    f_data = pr_re.file_reader()
    print(f_data)