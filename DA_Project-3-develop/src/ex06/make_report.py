import sys
import config
import analytics
from analytics import Research

if __name__ == '__main__':
    flag = 1
    if len(sys.argv) < 2:
        print("Использование: python3 first_nest.py <путь_к_файлу.csv>")
        flag =0 
    if flag == 1:
        pr_re = Research(sys.argv[1])
        f_data = pr_re.file_reader(has_header=True)
        if f_data != None :

            
            calc = pr_re.Calculations()
            
            orel, reshka = calc.counts(f_data)


            heads_perc, tails_perc = calc.fractions(orel, reshka)


            analytic = pr_re.Analytics()

            random_preds = analytic.predict_random(config.steps_for_predict_random)


            last_item = analytic.predict_last(f_data)

            predicted_heads, predicted_tails = analytic.counts(random_preds)

            report = config.report_template.format(
                total_observations=len(f_data),
                tails_count=orel,
                heads_count=reshka,
                tails_percent=heads_perc,
                heads_percent=tails_perc,
                num_of_steps=config.steps_for_predict_random,
                predicted_tails=predicted_tails,
                predicted_heads=predicted_heads,
            )
            analytic.save_file(report, "report", "txt")
            if f_data:
                pr_re.send_telegram_message("The report has been successfully created.")
            else:
                pr_re.send_telegram_message("The report hasn’t been created due to an error.")

