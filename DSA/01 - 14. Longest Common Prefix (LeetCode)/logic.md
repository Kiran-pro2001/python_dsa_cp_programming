
````markdown
# Longest Common Prefix - Approach & Explanation

## Problem Example
Input:  

["Flow", "Flower", "Float", "Flight"]
````

## Approach

* **Step 1: Initialize prefix**

  * Take the **first string** (`"Flow"`) as the initial prefix.
  * The longest prefix cannot be longer than the first string.

* **Step 2: Compare prefix with each string**

  * Compare `"Flow"` with `"Flower"`:

    * `"Flow"` is a prefix → keep prefix as `"Flow"`.
  * Compare `"Flow"` with `"Float"`:

    * `"Flow"` is not a prefix.
    * Reduce prefix → `"Flo"`, still not a prefix.
    * Reduce again → `"Fl"`, matches → update prefix to `"Fl"`.
  * Compare `"Fl"` with `"Flight"`:

    * `"Fl"` is a prefix → keep `"Fl"`.

* **Step 3: Handle mismatches**

  * If prefix is not found in a word:

    * Keep removing the last character until it matches or becomes empty.
  * If prefix becomes empty → return `""`.

* **Step 4: Final result**

  * After comparing with all words, return the remaining prefix.
  * Example → Result is `"Fl"`.

## Edge Cases

* If the input array is empty → return `""`.
* If no common prefix exists → return `""`.

## Complexity Analysis

* **Time Complexity:**

  * `O(S)` where `S` = total number of characters across all strings. 
  * In short, `O(n)` where n is the total number of characters 
  * Efficient since only character comparisons are done.
* **Space Complexity:**

  * `O(1)` → only uses a few variables.

---

✅ Simple and efficient approach with **linear time complexity** and **constant space usage**.

