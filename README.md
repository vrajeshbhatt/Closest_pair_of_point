Closest pair of point
----------------------

This is implimentation of finding closest pair of points and distance.
Divide and Conquer approch with O(n log n) time complexity

This problem can be solved by bruteforce method with direct approch of Euclidean Distance.
But it would take O(n²) and that is not acceptable.
   
With Divide and Conquer there is 3 aspascts:
    1) closest one on leftside
    2) closest one on rightside
    3) closest one between this two part
for the first 2 aspacts there is closest_pair function and for third closest_pair_strip function is used.

Algorithm:
----------
1) We sort all points according to x and y coordinates in Pn and Qn.

2) Divide all points in two parts through midPoint Qx and Rx.

3) Recursively find the minimun distances and pair in both subarrays dLeft and dRight .

4) Take the minimum of two smallest distances. Let the minimum be minDistAll.

5) Create an array strip[] that stores all points which are at most minDistAll distance away from the middle line dividing the two sets.
(here function closest_pair_strip will be use)

6) Find the smallest distance in strip[].

7) Return the minimum of d and the smallest distance and pairs calculated in above step 6.



Total running time:
-------------------
• Divide set of points in half each time: O(log n)
• Merge takes O(n) time.
• Recurrence: 2T(n/2) 
• Total O(n log n) time.
 
Refrences:
-----------
https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/closepoints.pdf
https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/
https://github.com/SlavkoPrytula/Find-The-Closest-Pair-Of-Points
