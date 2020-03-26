class ExtClassification:
    def __init__(self, classification_name, previous_term_amount=0,
                 current_period_amount=0, subject_array=None):
        self.classification_name = classification_name
        self.previous_term_amount = previous_term_amount
        self.current_period_amount = current_period_amount
        self.subject_array = subject_array

    def output_classification_data(self):
        result = self._calc_amount()
        print(self.classification_name, result[0], result[1])

    def output_classification_calc_data(self):
        result = self._calc_amount()
        total_amount = result[1] - result[0]
        print(self.classification_name, total_amount)

    def _calc_amount(self):
        total_previous_term_amount = 0
        total_current_period_amount = 0
        for subject in self.subject_array:
            total_previous_term_amount += subject.previous_term_amount
            total_current_period_amount += subject.current_period_amount
        return total_previous_term_amount, total_current_period_amount
