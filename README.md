# ML-code-fairness
### Implementations for detecting and understanding biases in ML libraries
### Requirements
Python 3.6 and standard packages such as Numpy, Scikit-learn.

Run the random search for adult credit dataset with gender as sensitive feature:
```
python main_random.py --dataset=census --algorithm=LogisticRegression --sensitive_index=9 --max_iter=100000  2>&1 | tee LogisticRegression_census_gender_random_output.txt &
python main_random.py --dataset=credit --algorithm=TreeRegressor --sensitive_index=9 --max_iter=100000 2>&1 | tee TreeRegressor_credit_gender_random_output.txt &
python main_random.py --dataset=credit --algorithm=Decision_Tree_Classifier --sensitive_index=9 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_credit_random_random_output.txt &
python main_random.py --dataset=credit --algorithm=Discriminant_Analysis --sensitive_index=9 --max_iter=100000 2>&1 | tee Discriminant_Analysis_credit_gender_random_output.txt &
```
This will result into two files: .csv file shows inputs and outcome of training; .txt file writes extra details (not essential part of the analysis).    

Run the mutation search for adult credit dataset with gender as sensitive feature:
```
python main_mutation.py --dataset=census --algorithm=LogisticRegression --sensitive_index=9 --max_iter=100000 2>&1 | tee LogisticRegression_census_gender_mutation_output.txt &
python main_mutation.py --dataset=census --algorithm=TreeRegressor --sensitive_index=9 --max_iter=100000 2>&1 | tee TreeRegressor_census_gender_mutation_output.txt &
python main_mutation.py --dataset=census --algorithm=Decision_Tree_Classifier --sensitive_index=9 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_census_gender_mutation_output.txt &
python main_mutation.py --dataset=census --algorithm=Discriminant_Analysis --sensitive_index=9 --max_iter=100000 2>&1 | tee Discriminant_Analysis_census_gender_mutation_output.txt &
```
Run the coverage search for adult credit dataset with gender as sensitive feature:
```
python main_coverage.py --dataset=census --algorithm=LogisticRegression --sensitive_index=9 --max_iter=100000  2>&1 | tee LogisticRegression_census_gender_coverage_output.txt &
python main_coverage.py --dataset=census --algorithm=TreeRegressor --sensitive_index=9 --max_iter=100000 2>&1 | tee TreeRegressor_census_gender_coverage_output.txt &
python main_coverage.py --dataset=census --algorithm=Decision_Tree_Classifier --sensitive_index=9 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_census_gender_coverage_output.txt &
python main_coverage.py --dataset=census --algorithm=Discriminant_Analysis --sensitive_index=9 --max_iter=100000 2>&1 | tee Discriminant_Analysis_census_gender_coverage_output.txt &
```
Commands for other datasets:
```
python main_random.py --dataset=census --algorithm=LogisticRegression --sensitive_index=8 --max_iter=100000 | tee LogisticRegression_census_race_random_output.txt &
python main_random.py --dataset=census --algorithm=TreeRegressor --sensitive_index=8 --max_iter=100000 | tee TreeRegressor_census_race_random_output.txt &
python main_random.py --dataset=census --algorithm=Decision_Tree_Classifier --sensitive_index=8 --max_iter=100000  2>&1 | tee Decision_Tree_Classifier_census_race_random_output.txt &
python main_random.py --dataset=census --algorithm=Discriminant_Analysis --sensitive_index=8 --max_iter=100000 2>&1 | tee Discriminant_Analysis_census_race_random_output.txt &
```
```
python main_mutation.py --dataset=census --algorithm=LogisticRegression --sensitive_index=8 --max_iter=100000 2>&1 | tee LogisticRegression_census_race_mutation_output.txt &
python main_mutation.py --dataset=census --algorithm=TreeRegressor --sensitive_index=8 --max_iter=100000 2>&1 | tee TreeRegressor_census_race_mutation_output.txt &
python main_mutation.py --dataset=census --algorithm=Decision_Tree_Classifier --sensitive_index=8 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_census_race_mutation_output.txt &
python main_mutation.py --dataset=census --algorithm=Discriminant_Analysis --sensitive_index=8 --max_iter=100000 2>&1 | tee Discriminant_Analysis_census_race_mutation_output.txt &
```
```
python main_coverage.py --dataset=census --algorithm=LogisticRegression --sensitive_index=8 --max_iter=100000  2>&1 | tee LogisticRegression_census_race_coverage_output.txt &
python main_coverage.py --dataset=census --algorithm=TreeRegressor --sensitive_index=8 --max_iter=100000 2>&1 | tee TreeRegressor_census_race_coverage_output.txt &
python main_coverage.py --dataset=census --algorithm=Decision_Tree_Classifier --sensitive_index=8 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_census_race_coverage_output.txt &
python main_coverage.py --dataset=census --algorithm=Discriminant_Analysis --sensitive_index=8 --max_iter=100000 2>&1 | tee Discriminant_Analysis_census_race_coverage_output.txt &
```
```
python main_random.py --dataset=credit --algorithm=LogisticRegression --sensitive_index=9 --max_iter=100000 2>&1 | tee LogisticRegression_credit_gender_random_output.txt &
python main_random.py --dataset=credit --algorithm=TreeRegressor --sensitive_index=9 --max_iter=100000 2>&1 | tee TreeRegressor_credit_gender_random_output.txt &
python main_random.py --dataset=credit --algorithm=Decision_Tree_Classifier --sensitive_index=9 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_credit_random_random_output.txt &
python main_random.py --dataset=credit --algorithm=Discriminant_Analysis --sensitive_index=9 --max_iter=100000 2>&1 | tee Discriminant_Analysis_credit_gender_random_output.txt &
```
```
python main_mutation.py --dataset=credit --algorithm=LogisticRegression --sensitive_index=9 --max_iter=100000 2>&1 | tee LogisticRegression_credit_gender_mutation_output.txt &
python main_mutation.py --dataset=credit --algorithm=TreeRegressor --sensitive_index=9 --max_iter=100000 2>&1 | tee TreeRegressor_credit_gender_mutation_output.txt &
python main_mutation.py --dataset=credit --algorithm=Decision_Tree_Classifier --sensitive_index=9 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_credit_gender_mutation_output.txt &
python main_mutation.py --dataset=credit --algorithm=Discriminant_Analysis --sensitive_index=9 --max_iter=100000 2>&1 | tee Discriminant_Analysis_credit_gender_mutation_output.txt &
```
```
python main_coverage.py --dataset=credit --algorithm=LogisticRegression --sensitive_index=9 --max_iter=100000 2>&1 | tee LogisticRegression_credit_gender_coverage_output.txt &
python main_coverage.py --dataset=credit --algorithm=TreeRegressor --sensitive_index=9 --max_iter=100000 2>&1 | tee TreeRegressor_credit_gender_coverage_output.txt &
python main_coverage.py --dataset=credit --algorithm=Decision_Tree_Classifier --sensitive_index=9 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_credit_gender_coverage_output.txt &
python main_coverage.py --dataset=credit --algorithm=Discriminant_Analysis --sensitive_index=9 --max_iter=100000 2>&1 | tee Discriminant_Analysis_credit_gender_coverage_output.txt &
```
```
python main_random.py --dataset=bank --algorithm=LogisticRegression --sensitive_index=1 --max_iter=100000 2>&1 | tee LogisticRegression_bank_random_output.txt &
python main_random.py --dataset=bank --algorithm=TreeRegressor --sensitive_index=1 --max_iter=100000 2>&1 | tee TreeRegressor_bank_random_output.txt &
python main_random.py --dataset=bank --algorithm=Decision_Tree_Classifier --sensitive_index=1 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_bank_random_output.txt &
python main_random.py --dataset=bank --algorithm=Discriminant_Analysis --sensitive_index=1 --max_iter=100000 2>&1 | tee Discriminant_Analysis_bank_random_output.txt &
```
```
python main_mutation.py --dataset=bank --algorithm=LogisticRegression --sensitive_index=1 --max_iter=100000 2>&1 | tee LogisticRegression_bank_mutation_output.txt &
python main_mutation.py --dataset=bank --algorithm=TreeRegressor --sensitive_index=1 --max_iter=100000 2>&1 | tee TreeRegressor_bank_mutation_output.txt &
python main_mutation.py --dataset=bank --algorithm=Decision_Tree_Classifier --sensitive_index=1 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_bank_mutation_output.txt &
python main_mutation.py --dataset=bank --algorithm=Discriminant_Analysis --sensitive_index=1 --max_iter=100000 2>&1 | tee Discriminant_Analysis_bank_mutation_output.txt &
```
```
python main_coverage.py --dataset=bank --algorithm=LogisticRegression --sensitive_index=1 --max_iter=100000 2>&1 | tee LogisticRegression_bank_coverage_output.txt &
python main_coverage.py --dataset=bank --algorithm=TreeRegressor --sensitive_index=1 --max_iter=100000 2>&1 | tee TreeRegressor_bank_coverage_output.txt &
python main_coverage.py --dataset=bank --algorithm=Decision_Tree_Classifier --sensitive_index=1 --max_iter=100000 2>&1 | tee Decision_Tree_Classifier_bank_coverage_output.txt &
python main_coverage.py --dataset=bank --algorithm=Discriminant_Analysis --sensitive_index=1 --max_iter=100000 2>&1 | tee Discriminant_Analysis_bank_coverage_output.txt &
```

