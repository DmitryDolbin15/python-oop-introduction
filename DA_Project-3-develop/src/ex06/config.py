steps_for_predict_random = 3

report_template = """Report

We have made {total_observations} observations from tossing a coin: {tails_count} of them were tails and {heads_count} of them were heads. The probabilities are {tails_percent:.2f}% and {heads_percent:.2f}%, respectively. Our forecast is that in the next {num_of_steps} observations we will have: {predicted_tails} tail(s) and {predicted_heads} head(s).
"""

LOG_FILE = "analytics.log"


# Telegram configuration
TELEGRAM_BOT_TOKEN = "8092922724:AAHgrgAFUBnttPUPhPYQ8ZWcZzABA7qrhfE"
TELEGRAM_CHAT_ID = "447083887"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"