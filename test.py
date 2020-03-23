import exam1
import exam2
import exam3

print("--- exam1 test ---")
cash_and_deposit = exam1.Subject('現金及び預金', 4564255, 5160507)
cash_and_deposit.output_account_data()
cash_and_deposit.output_account_calc_data()

print("\n--- exam2 test ---")
notes_and_accounts_receivable = exam1.Subject('受け取り手形及び売掛金', 2013110, 2525653)
subject_list = [cash_and_deposit, notes_and_accounts_receivable]
current_assets = exam2.Classification('流動資産', subject_list)
current_assets.output_classification_data()
current_assets.output_classification_calc_data()

print("\n--- exam3 test ---")
current_assets = exam3.ExtClassification('流動資産')
current_assets.previous_term_amount = 7277553
current_assets.current_period_amount = 8398467
fixed_assets = exam3.ExtClassification('固定資産')
fixed_assets.previous_term_amount = 1536737
fixed_assets.current_period_amount = 2016762
asset_division_list = [current_assets, fixed_assets]
asset_division = exam3.ExtClassification('資産の部', asset_division_list)
asset_division.output_classification_data()
asset_division.output_classification_calc_data()
