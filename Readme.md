# 160 days geeks for geeks - problem solving
--------------------------------------------
## Arrays
   ------
1. Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/1.Second%20Largest.py)   
2. Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/2.Move%20All%20Zeroes%20to%20End.py)
3. You are given an array of integers arr[]. Your task is to reverse the given array.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/3.Reverse%20an%20Array.py)
4. Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.
[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/4.Rotate%20Array.py)
5. Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/5.Next%20Permutation.py)
6. You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/6.Majority%20Element%20II.py)
7. The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/7.Stock%20Buy%20and%20Sell.py)
8. Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/8.Stock%20Buy%20and%20Sell%20%E2%80%93%20Max%20one%20Transaction%20Allowed.py)
9. Given an array arr[] denoting heights of N towers and a positive integer K.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/9.Minimize%20the%20Heights%20II.py)
10. Given an integer array arr[]. You need to find the maximum sum of a subarray.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/10.Kadane's%20Algorithm.py)
11. Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/11.Maximum%20Product%20Subarray.py)
12. Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/12.Max%20Circular%20Subarray%20Sum.py)
13. You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/13.Smallest%20Positive%20Missing%20Number.py)

## Strings
   -------
14. Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.
    Cases for atoi() conversion:
    Skip any leading whitespaces.
    Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
    Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
    If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/14.Implement%20Atoi.py)
15. Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/15.Add%20Binary%20Strings.py)
16. Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/16.Anagram.py)
17. Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/17.Non%20Repeating%20Character.py)
18. Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/18.Search%20Pattern%20(KMP-Algorithm).py)
19. Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/19.Min%20Chars%20to%20Add%20for%20Palindrome.py)
20. You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/20.Strings%20Rotations%20of%20Each%20Other.py)

## Sorting
   -------
21. Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/21.Sort%200s%2C%201s%20and%202s.py)
22. Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.
H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/22.Find%20H-Index.py)
23. Given an array of integers arr[]. Find the Inversion Count in the array. Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j. Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/23.Count%20Inversions.py)
24. Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/24.Overlapping%20Intervals.py)
25. Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.
 Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/25.Insert%20Interval.py)
26. Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/26.Non-overlapping%20Intervals.py)
27. Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/27.Merge%20Without%20Extra%20Space.py)

## Searching
   ---------
28. Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/28.Number%20of%20occurrence.py)
29. A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/29.Sorted%20and%20Rotated%20Minimum.py)
30. Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/30.Search%20in%20Rotated%20Sorted%20Array.py)
31. Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/31.Peak%20element.py)
32. Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/32.K-th%20element%20of%20two%20Arrays.py)
33. You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/33.Aggressive%20Cows.py)
34. You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:
- Each student receives atleast one book.
- Each student is assigned a contiguous sequence of books.
- No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/34.Allocate%20Minimum%20Pages.py)
35. Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].  [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/35.Kth%20Missing%20Positive%20Number%20in%20a%20Sorted%20Array.py)

## Matrix
   ------
36. You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.[(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/36.Spirally%20traversing%20a%20matrix.py)
37. Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space. [(Solution)](https://github.com/pawang1745/Problem-Solving/blob/main/37.Rotate%20by%2090%20degree.py)
