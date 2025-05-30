steps_for_predict_random = 3

report_template = """Report

We have made {total_observations} observations from tossing a coin: {tails_count} of them were tails and {heads_count} of them were heads. The probabilities are {tails_percent:.2f}% and {heads_percent:.2f}%, respectively. Our forecast is that in the next {num_of_steps} observations we will have: {predicted_tails} tail(s) and {predicted_heads} head(s).
"""