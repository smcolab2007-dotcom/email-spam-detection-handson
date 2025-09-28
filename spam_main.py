 # --- model + metrics + image saving ---
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from pptx import Presentation
from pptx.util import Inches

@csquickrevisionshorts
# Example data (replace with real dataset if available)
emails = [
    "Congratulations, you won a free iPhone!",                # Spam
    "Meeting scheduled tomorrow at 10 AM",                   # Ham
    "Claim your free prize now!!!",                           # Spam
    "Please review the attached project report",             # Ham
    "Win cash now, limited offer",                            # Spam
    "Lunch at noon?",                                         # Ham
    "Exclusive deal: buy one get one free",                  # Spam
    "Minutes of today's meeting attached",                   # Ham
    "Get a free gift card by completing this survey!",       # Spam
    "Team outing next Friday, RSVP",                          # Ham
    "Limited-time offer! Earn $5000 per week",               # Spam
    "Can you send me the latest sales figures?",             # Ham
    "Your account has been compromised, reset now",          # Spam
    "Reminder: doctor appointment tomorrow at 9 AM",         # Ham
    "Win a luxury vacation to the Bahamas!",                 # Spam
    "Please find the invoice attached",                      # Ham
    "Earn money fast with this simple trick",                # Spam
    "Family dinner plans for Saturday?",                      # Ham
    "Get free tickets to the concert of your dreams!",       # Spam
    "Notes from today's lecture attached",                   # Ham
]

labels = [
    1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0
]  # 1 = spam, 0 = not spam

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.25, random_state=42)


@csquickrevisionshorts
# Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Print numeric results
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=0)
print("Accuracy:", acc)
print("Classification report:
", report)

@csquickrevisionshorts
# Confusion matrix plot (matplotlib only)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(4,3))
plt.imshow(cm, interpolation='nearest', cmap='Blues')
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, str(cm[i, j]), ha='center', va='center')
plt.xticks([0,1], ['not spam','spam'])
plt.yticks([0,1], ['not spam','spam'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig('/content/confusion.png', bbox_inches='tight')
plt.show()