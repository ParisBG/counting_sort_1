#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:43:15 2022
@author: parisbg

Comparison Sorting
Quicksort usually has a running time of , but is there an algorithm that can 
sort even faster? In general, this is not possible. Most sorting algorithms are 
comparison sorts, i.e. they sort a list just by comparing the elements to one 
another. A comparison sort algorithm cannot beat  (worst-case) running time, 
since  represents the minimum number of comparisons needed to know where to 
place each element. For more details, you can see these notes (PDF).

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. 
Instead, you create an integer array whose index range covers the entire 
range of values in your array to sort. Each time a value occurs in the original 
array, you increment the counter at that index. At the end, run through your 
counting array, printing the value of each non-zero valued index that number 
of times.

"""

#Instantiate a freq array with 100 zeroes
#Iterate through num array and calculate occurences
#Create dict key = freq and value = num
#Return result arr

arr = [1,1,2,3,45,6]
frequency = [0 for x in range(100)]

frequency[0] = 1
frequency[99] = 1
#print(frequency)
#print(len(frequency))
#print()

for i, val in enumerate(arr):
    frequency[val] += 1
    #print("index", i)
    #print("val", val)
print(frequency)