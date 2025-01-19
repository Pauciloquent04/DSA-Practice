# DSA Practice

This repository contains solutions to foundational data structure and algorithm problems implemented in Python.

## Problems Solved

### 1. Move Zeroes
- **Problem**: Move all zeroes in an array to the end while maintaining the relative order of non-zero elements.
- **Approach**: Two-pointer technique for O(n) time complexity.

#### Example Input and Output
- Input: `[0, 1, 0, 3, 12]`
- Output: `[1, 3, 12, 0, 0]`

---

### 2. Two Sum
- **Problem**: Find two numbers in an array that add up to a given target. Return their indices.
- **Approach**: Optimized solution using a hashmap for O(n) time complexity.

#### Example Input and Output
- Input: `nums = [2, 7, 11, 15], target = 9`
- Output: `[0, 1]`

---

### 3. First Non-Repeating Character in String
- **Problem**: Find the first character in a string that does not repeat.
- **Approach**: Use a hashmap to store character counts and identify the first non-repeating character in O(n) time.

#### Example Input and Output
- Input: `"swiss"`
- Output: `"w"`

---

### 4. Find Majority Element (Boyer-Moore Algorithm)
- **Problem**: Find the element that appears more than n/2 times in an array.
- **Approach**: Boyer-Moore Voting Algorithm for O(n) time complexity and O(1) space.

#### Example Input and Output
- Input: `[3, 3, 4, 2, 4, 4, 2, 4, 4]`
- Output: `4`

---

### 5. Maximum Sum of Contiguous Array (Kadane's Algorithm)
- **Problem**: Find the maximum sum of a contiguous subarray in an array.
- **Approach**: Kadane's Algorithm for O(n) time complexity.

#### Example Input and Output
- Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6` (subarray: `[4, -1, 2, 1]`)

---

### 6. Rotate Array by K Spaces
- **Problem**: Rotate an array to the right by k steps.
- **Approach**: Reverse the array in three steps for O(n) time complexity and O(1) space.

#### Example Input and Output
- Input: `nums = [1, 2, 3, 4, 5, 6, 7], k = 3`
- Output: `[5, 6, 7, 1, 2, 3, 4]`

---

### 7. Remove Duplicates from Sorted Array In-Place
- **Problem**: Remove duplicates from a sorted array such that each element appears only once, modifying the array in-place.
- **Approach**: Two-pointer technique for O(n) time complexity.

#### Example Input and Output
- Input: `[1, 1, 2]`
- Output: `[1, 2]`

---

### 8. Find the Intersection of Two Arrays
- **Problem**: Compute the intersection of two arrays, ensuring each element in the result is unique.
- **Approach**: Use sets to find the intersection in O(n) time complexity.

#### Example Input and Output
- Input: `nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]`
- Output: `[9, 4]`

---

### 9. Maximum Sum of Subarrays
- **Problem**: Find the maximum sum of all possible subarrays of an array.
- **Approach**: Use prefix sums or divide-and-conquer for O(n log n) or O(n²) time complexity.

#### Example Input and Output
- Input: `[1, 2, 3, -2, 5]`
- Output: `9` (subarray: `[1, 2, 3, -2, 5]`)
