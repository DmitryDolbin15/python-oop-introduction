from random import randint
import logging
import requests
import config


logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    filemode="w"
)

class Research:
    def __init__(self, put):
        self.put = put
        logging.info(f"Initialized Research with file path: {put}")
    def file_reader(self,has_header=True):
        logging.info("Starting file_reader method.")
        flag = 1
        try:
            with open(self.put, 'r') as f:
                data =  f.read()
            logging.info("File successfully read.")
        except :
            logging.error(f"Не могу открыть файл {self.put}")
            flag = 0

        if flag == 1:  
            start_index = 1 if has_header else 0
            lines = data.split('\n')
            if start_index == 1:
                if len(lines) < 2:
                    logging.error("Файл должен содержать как минимум заголовок и одну строку данных.")
                    flag = 0

                head = lines[0].split(',')
                if len(head) != 2 and flag == 1:
                    logging.error("Некорректный формат заголовка. Должно быть 2 столбца, разделённые запятой.")
                    flag = 0
            else:
                if len(lines) < 1:
                    logging.error("Файл не должен быть пустым.")
                    flag = 0

            if flag != 0:
                data = []
                start_index = 1 if has_header else 0
                for line in lines[start_index:] :
                    part = line.split(',')
                    if len(part) != 2:
                        logging.error("Некорректная строка данных. Должно быть 2 столбца, разделённые запятой.")
                        flag = 0
                    
                    if flag == 1 and not ((part[0]== '1' and part[1]== '0') or (part[0]== '0' and part[1]== '1')):
                        logging.error(f"Некорректная строка данных: {line}. Допустимы только '0,1' или '1,0'.")
                        flag = 0
                    data.append([int(part[0]), int(part[1])])
                if flag == 1:
                    logging.info("Data successfully parsed.")
                    return data
                
    def send_telegram_message(self, message):
        logging.info("Starting send_telegram_message method.")
        try:
            response = requests.post(
                config.TELEGRAM_API_URL,
                json={"chat_id": config.TELEGRAM_CHAT_ID, "text": message},
            )
            if response.status_code == 200:
                logging.info("Telegram message sent successfully.")
            else:
                logging.error(f"Failed to send Telegram message: {response.status_code} {response.text}")
        except:
            logging.error(f"Error sending Telegram message: {e}")

    class Calculations:
        def counts(self,data):
            logging.info("Starting counts method.")
            orel = 0
            reshka = 0
            for line in data:
                if line == [1, 0]:
                    orel = orel  + 1
                elif line == [0, 1]:
                    reshka = reshka + 1
            logging.info(f"Counts calculated: heads={orel}, tails={reshka}")
            return orel, reshka
                    
        def fractions(self,orel, reshka):
            logging.info("Starting fractions method.")
            total = orel + reshka
            if total == 0:
                logging.warning("Total count is zero; returning 0% for both fractions.")
                return 0.0, 0.0
            else:
                logging.info(f"Fractions calculated: heads_percent={orel / total * 100}, tails_percent={reshka / total * 100}")
                return (orel / total * 100, reshka / total * 100)
    
    class Analytics(Calculations):
        def predict_random(self,n):
            logging.info(f"Starting predict_random method with n={n}.")
            predictions = []
            for _ in range(n):
                if randint(0, 1) == 1:
                    predictions.append([1, 0])
                    logging.debug(f"Prediction generated: {[1, 0]}")
                else:
                    predictions.append([0, 1])
                    logging.debug(f"Prediction generated: {[0, 1]}")
            logging.info(f"Generated {n} random predictions.")
            return predictions

        def predict_last(self,data):
            if not data:
                logging.error("Data list is empty. Cannot get the last element.")
            else: 
                logging.info(f"Last prediction retrieved: {data[-1]}")
                return data[-1]
        
        def save_file(self,data, name_of_file, ext):
            logging.info(f"Starting save_file method for {name_of_file}.{ext}.")
            try:
                with open(f"{name_of_file}.{ext}", 'w') as f:
                    f.write(data)
                    logging.info(f"File {name_of_file}.{ext} saved successfully.")
            except:
                logging.error(f"Error saving file {name_of_file}.{ext}")

