class Subject:
    def __init__(self, subject_name, previous_term_amount,
                 current_period_amount):
        self.subject_name = subject_name
        self.previous_term_amount = previous_term_amount
        self.current_period_amount = current_period_amount

    def output_account_data(self):
        print(self.subject_name, self.previous_term_amount,
              self.current_period_amount)

    def output_account_calc_data(self):
        calc_amount = self.current_period_amount - self.previous_term_amount
        print(self.subject_name, calc_amount)
