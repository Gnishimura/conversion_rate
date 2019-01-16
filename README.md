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

Interpreting Feature Importance in Gradient Boosting Classifier
![Feature Importances in Gradient Boosting model](data/feature_importances.png?raw=true "Feature Importances in Gradient Boosting Model")

These feature importances, tell us how often the Gradient Boosting model chose to split on those features.  We gain the most information by splitting on 'total_pages_visited', so a business recommendation may include focusing resources on getting users to visit more pages. 

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

