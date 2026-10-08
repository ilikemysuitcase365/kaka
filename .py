import numpy as np
original_arr = np.linspace(0, 9, 10, dtype=int)

print("--- STEP 1 ---")
print("Original Array:")
print(original_arr)
print("\n" + "="*50 + "\n")
modified_arr = np.where(original_arr % 2 != 0, -1, original_arr)

print("--- STEP 2 ---")
print("Modified Array (Odds replaced with -1):")
print(modified_arr)
print("\nVerification - Original Array remains completely untouched:")
print(original_arr)
print("\n" + "="*50 + "\n")
two_d_arr = original_arr.reshape(2, -1)

print("--- STEP 3 ---")
print("New 2D Array (2 Rows):")
print(two_d_arr)
print("\n" + "="*50 + "\n")
even_sum = 0
for val in original_arr:
    if val % 2 == 0:
        even_sum += val

print("--- STEP 4 ---")
print(f"Sum of all even numbers: {even_sum}  (0 + 2 + 4 + 6 + 8)")
print("\n" + "="*50)
