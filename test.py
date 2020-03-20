import exam1
import exam2

print("--- exam1 test ---")
cash_and_deposit = exam1.Subject('現金及び預金', 4564255, 5160507)
cash_and_deposit.output_account_data()
cash_and_deposit.output_account_calc_data()

print("\n--- exam2 test ---")
notes_and_accounts_receivable = exam1.Subject('受け取り手形及び売掛金', 2013110, 2525653)

subject_list = [cash_and_deposit, notes_and_accounts_receivable]
current_assets = exam2.Classification('流動資産', subject_list)
current_assets.output_classification_data()
