# conversion_rate

We have data about users who hit our site: whether they converted or not as well as some of their characteristics such as their country, the marketing channel, their age, whether they are repeat users and the number of pages visited during that session (as a proxy for site activity/time spent on site).

Your project is to:
* Predict conversion rate
* Come up with recommendations for the product team and the marketing team to improve conversion rate

Results:
* Logistic Regression (log-loss: 0.501)
* Random Forest Classifier (log-loss: 0.468)
* Gradient Boosting Classifier (log-loss: 0.485)
* ADA Boosting Classifier (log-loss: 0.466)  <-- Lowest Log-Loss

Feature Importances in ADA model:
![alt text](/Users/gnishimura/Desktop/Screen\ Shot\ 2019-01-15\ at\ 3.36.56\ PM.png raw=true "Title")

