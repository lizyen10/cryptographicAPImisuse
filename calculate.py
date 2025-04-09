# Recall = TP/(TP + FN)
# Precision = TP / (TP + FP)

# The F1 score is the harmonic mean of precision and recall, providing a balanced measure of a model's performance. 
# A higher F1 score indicates better overall performance in balancing precision and recall. 
# F1 = 2 * (precision * recall) / (precision + recall) 

# The F2 score is a weighted harmonic mean of precision and recall, giving more weight to recall than precision.
# A higher F2 score indicates better performance in terms of recall.  
# F2 = ((1 + 2^2) * precision * recall) / (2^2 * precision + recall) 

# Average Prompt 1
# === Evaluation Summary ===
# True Positives: 50
# False Negatives: 22
# True Negatives: 185
# False Positives: 1
# TP = 50
# FN = 22
# TN = 185
# FP = 1
# Recall:  0.6944
# Precision:  0.9804
# F1:  0.813
# F2:  0.7375

# Average Prompt 2
# === Evaluation Summary ===
# True Positives: 56
# False Negatives: 16
# True Negatives: 186
# False Positives: 0
# TP = 56
# FN = 16
# TN = 186
# FP = 0
# Recall:  0.7778
# Precision:  1.0
# F1:  0.875
# F2:  0.814

# Average Prompt 3
# === Evaluation Summary ===
# True Positives: 64
# False Negatives: 8
# True Negatives: 185
# False Positives: 1
TP = 64
FN = 8
TN = 185
FP = 1
# Recall:  0.8889
# Precision:  0.9846
# F1:  0.9343
# F2:  0.9065

recall = TP/(TP + FN)
precision = TP / (TP + FP)

f1 = 2 * (precision * recall) / (precision + recall) 
f2 = ((1 + pow(2,2)) * precision * recall) / (pow(2,2) * precision + recall) 

print("Recall: ", round(recall, 4))
print("Precision: ", round(precision, 4))
print("F1: ", round(f1, 4))
print("F2: ", round(f2, 4))