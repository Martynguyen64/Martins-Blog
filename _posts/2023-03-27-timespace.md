---
layout: home
search_exclude: true
categories: [markdown]
title: Timespace Hacks
---

# Hacks
- Record your findings when testing the time elapsed of the different algorithms.
- Although we will go more in depth later, time complexity is a key concept that relates to the different sorting algorithms. Do some basic research on the different types of sorting algorithms and their time complexity.
- Why is time and space complexity important when choosing an algorithm?
- Should you always use a constant time algorithm / Should you never use an exponential time algorithm? Explain? 
- What are some general patterns that you noticed to determine each algorithm's time and space complexity?

Complete the Time and Space Complexity analysis questions linked below.
[Practice](https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/)

1. Record your findings.

2.  There are many types of sorting algorithms, but some of the most common ones include:

    Bubble Sort: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. This algorithm has a time complexity of O(n^2).

    Selection Sort: Selection sort is another simple sorting algorithm that sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning. This algorithm has a time complexity of O(n^2).

    Insertion Sort: Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. This algorithm has a time complexity of O(n^2).

    Merge Sort: Merge sort is a divide-and-conquer algorithm that recursively divides the input array into two halves, sorts each half, and then merges the two sorted halves back together. This algorithm has a time complexity of O(n log n).

    Quick Sort: Quick sort is another divide-and-conquer algorithm that chooses a pivot element and partitions the array around the pivot, recursively sorting the two resulting subarrays. This algorithm has a time complexity of O(n log n).

    Heap Sort: Heap sort is another sorting algorithm that uses a binary heap data structure to sort an array. It sorts the array by repeatedly finding the maximum element and swapping it with the last element, then removing the last element from consideration. This algorithm has a time complexity of O(n log n).

Overall, the time complexity of sorting algorithms varies depending on the algorithm itself and the size of the input array. Some algorithms have a better performance than others, making them more suitable for certain scenarios.

3. Time and space complexity are important factors to consider when choosing an algorithm. They determine the efficiency of the algorithm in terms of how quickly it can solve the problem and how much memory it requires. Time complexity refers to the amount of time an algorithm takes to complete its execution, while space complexity refers to the amount of memory required. Algorithms with better time complexity are able to solve larger problems in less time, making them more efficient and desirable. On the other hand, algorithms with better space complexity use less memory, making them more efficient in memory-constrained environments. Choosing the right algorithm with the optimal time and space complexity can significantly improve the performance and efficiency of the solution. Therefore, it is important to consider the time and space complexity of algorithms when choosing the best one for a particular task.

4. The choice of algorithm depends on the problem and its requirements, and it's not always possible to use constant time algorithms or avoid exponential time algorithms. Constant time algorithms are efficient, but only applicable to certain problems. Exponential time algorithms are generally inefficient, but some problems can only be solved using them. Therefore, it's important to choose the most appropriate algorithm for the task at hand, considering the time and space complexity of algorithms.
Here are some examples:
Constant time algorithm:
    - Accessing an element in an array using its index is a constant time operation. It takes the same amount of time regardless of the size of the array.

Exponential time algorithm:
    - Brute force algorithm to find all possible combinations of a password. For example, if a password has 8 characters and each character can be a letter or a number, there are 62 possible characters for each position, leading to a total of 62^8 possible combinations, which is an exponential number.
In conclusion, the choice of algorithm depends on the specific problem and its requirements, and it's important to choose the most appropriate one, considering the time and space complexity.

5. There are several general patterns that can be used to determine the time and space complexity of an algorithm. One of the most common patterns is to look at the number of operations that the algorithm performs in relation to the input size. For example, if an algorithm performs a single operation for each input element, it would have a linear time complexity. Another pattern is to consider the number of times that the algorithm needs to perform a certain operation. For example, if an algorithm needs to perform a nested loop over the input data, it would have a quadratic time complexity. Another pattern is to look at the amount of memory required by the algorithm. For example, if an algorithm needs to store the input data in a data structure, the space complexity would depend on the size of the data and the space required by the data structure. These patterns provide a useful framework for understanding the time and space complexity of algorithms and can help in choosing the most appropriate algorithm for a particular task.

# Analysis questions
1. The time complexity of the problem is O(N+M) because the first loop is O(N) and the second loop is O(M), with N and M being independent variables. The space complexity is constant or O(1) because variable size does not depend on input size.
2. the answer is option 4 there are two nested loops that both iterate over the same collection, thus the time taken to complete the algorithm grows quadratically with the size of the collection.
3. the answer is option 2 the first for statement is N. The second for statement is logN. pow(2,j) represents the step size so for each iteration of the second for, j increases until 2^j = n which means that j = log(2)n. Then it stops so the time complexity is N*logN.
4. Option 2 is the answer. The worst-case time complexity of an algorithm is the largest amount of time it takes to run for any input size. When one algorithm is asymptotically more efficient than another, it means it has a smaller worst-case time complexity. This implies that as input size grows towards infinity, the faster algorithm will eventually be X. For instance, algorithm X with O(n log n) worst-case time complexity is asymptotically more efficient than algorithm Y with O(n^2) worst-case time complexity. As the input size gets larger, X will eventually become faster than Y for large enough inputs.
5. Option 4 is the answer. The code iterates and assigns the halved and added value of "i" to variable "a." As "i" approaches 0, N decreases in larger quantities initially and then slows down, following a logarithmic pattern.
6. Option 3 is correct. Programmers must consider both time and memory efficiency when evaluating algorithms. It's important to ensure that the algorithm doesn't use too much memory and that the program runs within a reasonable time frame.
7. Option 2 is correct. To calculate the time complexity of an algorithm, programmers typically identify the operations that the algorithm performs and count the number of times each operation is executed as a function of the input size n. This approach helps in determining how the algorithm's performance will scale with an increase in input size.
8. Option 3 is the answer. The time complexity is n*(n-1) because the first for loop runs n times, and the second for loop runs n-1 times.
9. The statement 'Algorithm B always has a worse running time than Algorithm A' is false. Although Algorithm B may have a better asymptotic complexity than A, it does not always run faster for small input sizes. Asymptotic complexity only shows how an algorithm behaves as the input size grows towards infinity, but for small inputs, Algorithm A may still run faster than Algorithm B.

## Notes
- list: use indexing to find specific number
- dictionary has key and values, use the key to find a specific valueigh