"""
1) Add the file and topic details.
   a) Mention the file name as `01-eq-mid.py`.
   b) Mention the topic as "Slices and their sums, Left-right balance, Equilibrium point".
   c) Introduce the program as a way to find the index where left and right sums are equal.

2) Create the equilibrium middle function.
   a) Define a function named `eq_mid(n)`.
   b) Create an array with `n` ones, then 0, then `n` more ones.
   c) Store the length of the array in `size`.

3) Check each index.
   a) Use a for loop to visit every index.
   b) Treat the current index as the possible equilibrium point.
   c) Start `left_sum` and `right_sum` from 0.

4) Calculate the left and right sums.
   a) Use an inner loop to add all values before the current index.
   b) Use another inner loop to add all values after the current index.
   c) Compare both sums.

5) Return the equilibrium index.
   a) If `left_sum` equals `right_sum`, return the current index.
   b) Return -1 if no equilibrium point is found.

6) Ask for a number.
   a) Ask the user to enter a value for `n`.
   b) Suggest example values like 5 or 6.
   c) Convert the input into an integer.

7) Ask for a prediction and display the result.
   a) Ask the user to guess the result of `eq_mid(n)`.
   b) Call `eq_mid(n)` using the user's number.
   c) Print the result and the user's original guess.
"""
def eq_mid(n):
   list = [1]*n + [0] + [1]*n
   size = len(list)
   for i in range(size):
      left_sum = 0
      right_sum = 0
      for j in range(i):
         left_sum += list[j]
      for j in range(i + 1, size):
         right_sum += list[j]
      if left_sum == right_sum:
         return i
   return -1
n = int(input("Enter a number to find the equilibrium index (e.g., 5, 6): "))
guess = input("What do you think the equilibrium index will be? (Enter a number): ")
input("eq_mid(n) press enter")
print("The equilibrium index is:", eq_mid(n), "your guess was", guess)