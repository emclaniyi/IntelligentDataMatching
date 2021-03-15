from IdMatcherPredictor import IDMatcher

sort = IDMatcher("State", "Provider State")

dfA = sort.read_data('https://github.com/chris1610/pbpython/raw/master/data/hospital_account_info.csv')
#print("dataA--->>>", dfA)
dfB = sort.read_data('https://raw.githubusercontent.com/chris1610/pbpython/master/data/hospital_reimbursement.csv')
#print("dataB-->>>", dfB)

tester = sort.sorter(dfA, dfB)
tester2 = sort.compare_for_matches(dfA, dfB, 0.85)
tester3 = sort.predict_id_matches(dfA, dfB, 0.85)
print(tester3)