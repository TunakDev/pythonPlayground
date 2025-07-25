import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

# load data from csv
df = pd.read_csv('../data/delaney_solubility_with_descriptors.csv')
print(df)

# data separation as x,y
y = df['logS']
x = df.drop('logS', axis=1)

print(y)
print(x)

#split data in training and testing set
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=100)

# training set has 80% of the data
print(x_train)
# test set has 20% of the data
print(x_test)

# build the model with linear regression
lr = LinearRegression()
# train the model
lr.fit(x_train, y_train)

# let model predict values
y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)

# evaluate model performance
lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

# create dataframe to show results
lr_results = pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
print(lr_results)

# build the model with random forest
rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train, y_train)

# let model predict values
y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)

# evaluate model performance
rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

# create dataframe to show results
rf_results = pd.DataFrame(['Random Forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
print(rf_results)

# combine tables
df_models = pd.concat([lr_results, rf_results], axis=0).reset_index(drop=True)
print(df_models)

# data visualization of prediction results
plt.figure(figsize=(5,5))
plt.scatter(x=y_train, y=y_lr_train_pred,c="#7CAE00", alpha=0.3)
# add trend-line to plot
z = np.polyfit(y_train, y_lr_train_pred, 1)
p = np.poly1d(z)
plt.plot(y_train, p(y_train), '#F8766D')
plt.ylabel('Predict LogS')
plt.ylabel('Experimental LogS')
plt.show()