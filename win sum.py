"""
1) Add the file and topic details.
   a) Mention the file name as `03-win-sum.py`.
   b) Mention the topic as "Subarray window, Target sum search".
   c) Introduce the program as a way to find the first window whose sum matches the target.

2) Create the window sum function.
   a) Define a function named `win_sum(n)`.
   b) Create an array with `n` zeros followed by `n` ones.
   c) Store the length of the array in `size`.

3) Move a window across the array.
   a) Use a for loop to choose each starting index.
   b) Make the window length equal to `n`.
   c) Check only valid windows inside the array.

4) Calculate the current window sum.
   a) Start `curr_sum` from 0.
   b) Use an inner loop to add values from index `i` to `i + n`.
   c) Store the total for the current window.

5) Search for the target sum.
   a) Check if `curr_sum` is equal to `n`.
   b) Return the starting index when the target window is found.
   c) Return -1 if no matching window is found.

6) Ask for a number.
   a) Ask the user to enter a value for `n`.
   b) Suggest example values like 5 or 6.
   c) Convert the input into an integer.

7) Ask for a prediction and display the result.
   a) Ask the user to guess the result of `win_sum(n)`.
   b) Call `win_sum(n)` using the user's number.
   c) Print the result and the user's original guess.
"""
def win_sum(n):
   list = [0]*n + [1]*n
   size = len(list)
   for i in range(size-n, 1):
      curr_sum = 0
      for j in range(i, i+n):
         curr_sum += list[j]
         if curr_sum == n:
            return i
   return -1
n = int(input("Enter a number to find the first window whose sum matches the target (e.g., 5, 6): "))
guess = input("What do you think the starting index of the first matching window will be? (Enter a number): ")
input("win_sum(n) press enter")
print("The starting index of the first matching window is:", win_sum(n), "your guess was", guess)