Non-engineered prompt

Run 1 - api_output_1.txt
=== Evaluation Summary ===
True Positives: 50
False Negatives: 22
True Negatives: 185
False Positives: 1

Run 2 - api_output_2.txt
=== Evaluation Summary ===
True Positives: 49
False Negatives: 23
True Negatives: 185
False Positives: 1

Run 3 - api_output_3.txt
=== Evaluation Summary ===
True Positives: 51
False Negatives: 21
True Negatives: 185
False Positives: 1

Average Prompt 1
=== Evaluation Summary ===
True Positives: 50
False Negatives: 22
True Negatives: 185
False Positives: 1

Precision
Recall
F score


------------------------------
Engineered prompt with attacks

Run 1 - api_output_4.txt
=== Evaluation Summary ===
True Positives: 55
False Negatives: 17
True Negatives: 186
False Positives: 0

Run 2 - api_output_5.txt
=== Evaluation Summary ===
True Positives: 56
False Negatives: 16
True Negatives: 186
False Positives: 0

Run 3 - api_output_6.txt
=== Evaluation Summary ===
True Positives: 56
False Negatives: 16
True Negatives: 186
False Positives: 0

Average Prompt 2
=== Evaluation Summary ===
True Positives: 56
False Negatives: 16
True Negatives: 186
False Positives: 0


-----------------
Engineered prompt with attacks and misuse rules

Run 1 - api_output_7.txt
=== Evaluation Summary ===
True Positives: 64
False Negatives: 8
True Negatives: 185
False Positives: 1

Run 2 - api_output_8.txt
=== Evaluation Summary ===
True Positives: 65
False Negatives: 7
True Negatives: 186
False Positives: 0

Run 3 - api_output_9.txt
=== Evaluation Summary ===
True Positives: 64
False Negatives: 8
True Negatives: 185
False Positives: 1

Average Prompt 3
=== Evaluation Summary ===
True Positives: 64
False Negatives: 8
True Negatives: 185
False Positives: 1


--------------------
- focused on detection of crypto api misuse, so also for costs, limited the response to a sentence of reasoning, if allowed for more, could have instructed to offer solutions 
- in testing beyond this api calls, llm would offer solutions 


