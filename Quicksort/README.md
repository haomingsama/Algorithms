The algorithm implementation of programming assignment #2 of Standford Algorithm Design I
The question is:

The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the  row of the file gives you the  entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length , you should simply add  to your running total of comparisons. (This is because the pivot element is compared to each of the other  elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).

Question 1: [Viewcode](Quick_sort2.py)

For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

Question 2: [Viewcode](Quick_sort3.py)

Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element. Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.

Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.

Question 3: [Viewcode](Quick_sort4.py)

![xxx](https://github.com/haomingsama/Algorithms/blob/master/Quicksort/question%233.png)


### One very simple and clear QuickSort Algorithm

Although it might be a litte bit slower, but it is very easy to understand ! [Viewcode](Quick_sort.py)
