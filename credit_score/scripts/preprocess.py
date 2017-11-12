import numpy as np 
import pandas as pd
import sys
from sklearn import preprocessing


FILE_HEADERS = [
    'checking_status', 'duration', 'credit_history', 'purpose', 'credit_amount', 'savings_status', 'employment',
    'installment_commitment', 'personal_status', 'other_parties', 'residence_since', 'property_magnitude',
    'age', 'other_payment_plans', 'housing', 'existing_credits', 'job', 'num_dependents',
    'own_telephone', 'foreign_worker', 'class' 
    ] 

CATEGORICAL_HEADERS = [
    'purpose', 'personal_status', 'other_parties', 'property_magnitude', 'other_payment_plans',
    'housing', 'own_telephone', 'foreign_worker' 
  ]

def preprocess_file(file_name, output='preprocessed_data.csv'):
  df = pd.read_csv(sys.argv[1], header=None, names=FILE_HEADERS)
  #obj_df = df.select_dtypes(include=['object']).copy()

  # preprocess checking status, there is some relation between values
  # so using a replace method
  checking_status = { "'<0'": 1, "'0<=X<200'": 2, "'>=200'": 3, "'no checking'": 0 } 
  credit_history =  { "'no credits/all paid'": 4, "'all paid'": 3,
          "'existing paid'": 2, "'delayed previously'": 1, "'critical/other existing credit'": 0 }
  savings_status = { "'<100'": 1, "'100<=X<500'": 2, "'500<=X<1000'": 3, "'>=1000'": 4, "'no known savings'": 0 }
  employment = { 'unemployed': 0, "'<1'": 1, "'1<=X<4'": 2, "'4<=X<7'": 3, "'>=7'": 4 }
  job = { "'unemp/unskilled non res'": 0, "'unskilled resident'": 1, 'skilled': 2, "'high qualif/self emp/mgmt'": 4 }
  classes = { 'good': 1, 'bad': 0 }
  
  replace = {'checking_status': checking_status, 'credit_history': credit_history,
          'savings_status': savings_status, 'employment': employment, 'job': job, 'class': classes }

  df.replace(replace, inplace=True)

#  for col in CATEGORICAL_HEADERS:
#    df[col] =  df[col].astype('category')

  df = pd.get_dummies(df, columns=CATEGORICAL_HEADERS)
  df.to_csv(output, sep=',', index=False)

if __name__ == '__main__':
  preprocess_file(sys.argv[1])
