import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from sklearn.ensemble import (RandomForestClassifier, 
                              GradientBoostingClassifier, 
                              AdaBoostClassifier)


#Read in data
conversion_data = pd.read_csv('data/conversion_data.csv')

#Separate labels from data
X = conversion_data.iloc[:,:5]
y = conversion_data.pop('converted')

#Identify categorical vs numerical variables
cat_vars = X.loc[:,['country', 'source']]
num_vars = X.loc[:,['age', 'new_user', 'total_pages_visited']]

#First try logistic reg on num_vars only
#Train test split, leave 20% of data in test 
num_X_train, num_X_test, num_y_train, num_y_test = train_test_split(num_vars, y, test_size=0.2, random_state=20)
num_log_reg = LogisticRegression()
num_log_reg.fit(num_X_train, num_y_train)
num_y_preds = num_log_reg.predict(num_X_test)
log_loss_num = log_loss(num_y_test, num_y_preds) 
print(f"log loss for just numericals and logistic regression: {log_loss_num}") 
#log loss score = 0.5009

#Now try incorporating categoricals
def dummify_cats(df, column_name):
    new_cats = list(df[column_name].unique())
    for i, cat in enumerate(new_cats):
        df['is_' + new_cats[i]] = (df[column_name]==cat).astype(int)
    df.drop([column_name], axis=1, inplace=True)

X_dummied = X.copy()
dummify_cats(X_dummied, 'country')
dummify_cats(X_dummied, 'source')

full_X_train, full_X_test, full_y_train, full_y_test = train_test_split(X_dummied, y, test_size=0.2, random_state=20)
lr = LogisticRegression()
lr.fit(full_X_train, full_y_train)
lr_y_preds = lr.predict(full_X_test)
log_loss_full = log_loss(full_y_test, lr_y_preds) 
print(f"log loss for full logistic regression was {log_loss_full}") 
print(f"accuracy = {lr.score(full_X_test, full_y_test)}")
#log loss score for just numerical vars was .4675


#Try Random Forest Classifier 
rfc = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=20)
rfc.fit(full_X_train, full_y_train)
random_forest_preds = rfc.predict(full_X_test)
print(f"log loss for random forest = {log_loss(full_y_test, random_forest_preds)}")
print(f"accuracy = {rfc.score(full_X_test, full_y_test)}")
#log loss score for RFC was .4850


#Try Gradient Boosting Classifier
N_ESTIMATORS = 1000
gbc = GradientBoostingClassifier(learning_rate=0.01, n_estimators=N_ESTIMATORS)
gbc.fit(full_X_train, full_y_train)
gbc_preds = gbc.predict(full_X_test)
print(f"log loss for gradient boosting = {log_loss(full_y_test, gbc_preds)}")
#log loss score for GBC was .4664

