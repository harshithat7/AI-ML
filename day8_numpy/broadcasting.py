import numpy as np
scores = np.random.randint(50,101,size=(5,3))
print("Original scores: ")
print(scores)
mean_scores = np.mean(scores, axis=0)
print("\nMean scores: ")
print(mean_scores)
centered_scores = scores - mean_scores
print("\nCentered scores: ")
print(centered_scores)