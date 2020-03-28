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
current_subject1 = exam1.Subject('流動資産1', 7000000, 8000000)
current_subject2 = exam1.Subject('流動資産2', 277553, 398467)
current_subject_list = [current_subject1, current_subject2]
current_assets = exam3.ExtClassification('流動資産', current_subject_list)
current_assets.output_classification_data()
current_assets.output_classification_calc_data()
fixed_subject1 = exam1.Subject('固定資産1', 1000000, 2000000)
fixed_subject2 = exam1.Subject('固定資産2', 536737, 16762)
fixed_subject_list = [fixed_subject1, fixed_subject2]
fixed_assets = exam3.ExtClassification('固定資産', fixed_subject_list)
fixed_assets.output_classification_data()
fixed_assets.output_classification_calc_data()
print('')
asset_division_list = [current_assets, fixed_assets]
asset_division = exam3.ExtClassification('資産の部', asset_division_list)
asset_division.ext_output_classification_data()
asset_division.ext_output_classification_calc_data()
