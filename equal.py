"""
1) Add the file and topic details.
   a) Mention the file name as `02-eq-val.py`.
   b) Mention the topic as "Slices and their sums, Equilibrium point".
   c) Introduce the program as a way to find the value at the balance point.

2) Create the equilibrium value function.
   a) Define a function named `eq_val(n)`.
   b) Create an array with `n` ones, then `n`, then `n` more ones.
   c) Store the length of the array in `size`.

3) Check each position.
   a) Use a for loop to visit every index.
   b) Treat each index as a possible equilibrium point.
   c) Start `left_sum` and `right_sum` from 0.

4) Calculate sums on both sides.
   a) Use one inner loop to add all values on the left side.
   b) Use another inner loop to add all values on the right side.
   c) Compare the two sums after each position.

5) Return the equilibrium value.
   a) If both sums are equal, return `arr[i]`.
   b) Return -1 if no matching balance point is found.

6) Ask for a number.
   a) Ask the user to enter a value for `n`.
   b) Suggest example values like 5 or 6.
   c) Convert the input into an integer.

7) Ask for a prediction and display the result.
   a) Ask the user to guess the result of `eq_val(n)`.
   b) Call `eq_val(n)` using the user's number.
   c) Print the result and the user's original guess.
"""
def eq_val(n):
   list = [1]*n  + [n] + [1]*n
   size = len(list)
   for i in range(size):
      left_sum = 0
      right_sum = 0
      for i in range(i):
         left_sum += list[i]
      for i in range(i + 1, size):
         right_sum += list[i]
      if left_sum == right_sum:
         return list[i]
   return -1
n = int(input("Enter a number to find the equilibrium value (e.g., 5, 6): "))
guess = input("What do you think the equilibrium value will be? (Enter a number): ")
input("eq_val(n) press enter")
print("The equilibrium value is:", eq_val(n), "your guess was", guess)  