# conversion_rate

We have data about users who hit our site: whether they converted or not as well as some of their characteristics such as their country, the marketing channel, their age, whether they are repeat users and the number of pages visited during that session (as a proxy for site activity/time spent on site).

Your project is to:
* Predict conversion rate
* Come up with recommendations for the product team and the marketing team to improve conversion rate

Results:
* Logistic Regression (log-loss: 0.468)
* Random Forest Classifier (log-loss: 0.485)
* Gradient Boosting Classifier (log-loss: 0.466) <-- Lowest Log-Loss
* ADA Boosting Classifier (log-loss: 0.477)  

Interpreting Feature Importance 
![Feature Importances in Gradient Boosting model](data/feature_importances.png?raw=true "Feature Importances in Gradient Boosting Model")

These feature importances, from the Gradient Boosting model, can ONLY tell us how often the GB model chose to split on those features.  The model sees the biggest drop in entropy by splitting on 'total_pages_visited', but that should NOT immediately interpreted to mean that total pages visited is the most important feature for the business to focus on.  To get more interpretable results, let's look at the Beta coefficients of the logistic regression. 


![Beta Coefficients in Logistic Regression Model](data/betas.png?raw=true "Beta Coefficients in Logistic Regression Model")


Features:
* country : user country based on the IP address
* age : user age. Self-reported at sign-in step
* new_user : whether the user created the account during this session or had already an
account and simply came back to the site
* source : marketing channel source
  * Ads: came to the site by clicking on an advertisement
  * Seo: came to the site by clicking on search results
  * Direct: came to the site by directly typing the URL on the browser
* total_pages_visited: number of total pages visited during the session. This is a proxy for
time spent on site and engagement during the session.
* converted: this is our label. 1 means they converted within the session, 0 means they left
without buying anything. The company goal is to increase conversion rate: # conversions
/ total sessions.

