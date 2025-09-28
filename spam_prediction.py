 #Practice Code -1: Prediction
#---------
#Practical big data. Predict spam/ham
# New data for prediction
new_emails = [
   "Win a brand new car by clicking this link!",
   "Don't forget our lunch meeting tomorrow",
   "Get free coupons instantly!!!"
]

# Predict labels
new_preds = model.predict(new_emails)

# Display results
for email, label in zip(new_emails, new_preds):
   print(f"Email: {email}
Predicted label: {'Spam' if label == 1 else 'Ham'}
")
@csquickrevisionshorts

#***
#Practice Code -2: Practical-Big data. Error #analysis of spam/ham.
#---------
#Practical big data. Predict spam/ham
# New data with true labels
new_emails = [
   "Win a brand new car by clicking this link!",
   "Don't forget our lunch meeting tomorrow",
   "Get free coupons instantly!!!"
]
true_labels = [1, 0, 1]  # Actual spam/ham labels

# Predictions
new_preds = model.predict(new_emails)
#@csquickrevisionshorts
# Error analysis
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(true_labels, new_preds))
print(classification_report(true_labels, new_preds))