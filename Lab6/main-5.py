
#LAB 6 Linus Wallin & Arvid Gussarsson

from songClassFile import Song
import timeit
from hashTableFile import HashTable

def read_tracks(file_name = "unique_tracks.txt"):
  """
  Creates a tracklist and a artist list
  :param file_name: a file
  :return: a list with (track_id, track time, artist, song title) and a list of artists
  """
  with open(file_name, "r", encoding="utf-8") as track_file:
    track_list = track_file.readlines()
    artist_list = []
    for i in range(len(track_list)):
      new_track = track_list[i].split("<SEP>")
      track_list[i] = Song(new_track[0], new_track[1], new_track[2], new_track[3])
      artist_list.append(new_track[2])
  return track_list, artist_list

"""
stmt - The statement you want to measure, it defaults to pass
number - The number of executions you would like to run the statement
What does timeit measure time on? - Runs the code millions of times and gives an average runtime
Timeit return - Returns the number of seconds it took to execute the code on average
"""

def lin_search(list, artist):
  """
  Function does a linear search algorithm to see if the artist exists in the list.
  :param list: a list with objects
  :param artist: a string
  :return: a boolean
  """
  for item in list:
    if item == artist:
      return True
  return False

def bin_search(list, artist):
  # Chapter 6.4 - https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBinarySearch.html
  """
  Function does a binary search algorithm to see if the artist exists in the list

  :param list: a list with objects
  :param artist: a string
  :return: a boolean
  """
  n_min = 0
  n_max = len(list) - 1

  while n_min <= n_max:
    midpoint = (n_min + n_max) // 2
    if list[midpoint] == artist:
      return True
    else:
      if artist < list[midpoint]:
        n_max = midpoint - 1
      else:
        n_min = midpoint + 1
  return False

def hash_search(hash_table, artist):
  """
  Function checks if the artist exists in the hash_table

  :param hash_table: a hash table
  :param artist: a string
  :return: a boolean
  """
  if artist in hash_table:
    return True
  else:
    return False

def quick_sort(data):
  #F8 Sortering
  """

  :param data: list of strings
  :return: null
  """
  last = len(data) - 1
  qsort(data, 0, last)


def qsort(data, low, high):
  """
  Using quick sort and the last element in the list as the pivot elemment.

  :param data: list of strings
  :param low: the first index
  :param high: the last index
  :return: null
  """
  pivotindex = (low + high) // 2
  # move pivot to the edge
  data[pivotindex], data[high] = data[high], data[pivotindex]

  # damerna först med avseende på pivotdata
  pivotmid = partition(data, low - 1, high, data[high])

  # move the pivot back
  data[pivotmid], data[high] = data[high], data[pivotmid]

  if pivotmid - low > 1:
    qsort(data, low, pivotmid - 1)
  if high - pivotmid > 1:
    qsort(data, pivotmid + 1, high)


def partition(data, left, right, pivot):
  """
  Function searches for the pivot point

  :param data: a list of strings
  :param left: the left limit
  :param right: the right limit
  :param pivot: the index to start sorting from
  :return: returns the index to the left of the pivot point
  """
  while True:
    left += 1
    while data[left] < pivot:
      left += 1
    right -= 1
    while right != 0 and data[right] > pivot:
      right -= 1
    data[left], data[right] = data[right], data[left]
    if left >= right:
      break
  data[left], data[right] = data[right], data[left]
  return left

def bubble_sort(data):
  """
  Sorts a list using the bubble sort algorithm

  :param data: a list with strings
  :return: null
  """
  #F8 Sortering
  n = len(data)
  swapped = True
  while swapped:
    swapped = False
    for i in range(n - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        swapped = True

def main():
  filename = "unique_tracks.txt"

  list, new_list = read_tracks(filename)
  list_sort = new_list.copy()
  list_sorted = sorted(list_sort)
  new_list = new_list[0:25000]
  new_list_2 = new_list.copy()
  n = len(list)
  print("Amount of elements = ", n)

  last = list[n - 1]
  test_artist = last.artist


  binary_time = timeit.timeit(stmt=lambda: bin_search(list_sorted, test_artist), number=10000)
  print("The binary search took ", round(binary_time, 4), " seconds")
  hash_table = HashTable(list)
  hash_time = timeit.timeit(stmt=lambda: hash_search(hash_table, test_artist), number=10000)
  print("The hash search took ", round(hash_time, 4), " seconds")

  #linear sort takes alot of time as we are searching after the last element / will take approx. 10 minutes for
  #1000000 artists
  linear_time = timeit.timeit(stmt=lambda: lin_search(list_sorted, test_artist), number=10000)
  print("The linear search took ", round(linear_time, 4), " seconds")

  bubble_time = timeit.timeit(stmt=lambda: bubble_sort(new_list_2), number=10)
  print("The bubble sort took ", round(bubble_time, 4), " seconds")
  quick_time = timeit.timeit(stmt=lambda: quick_sort(new_list), number=10)
  print("The quick sort took ", round(quick_time, 4), " seconds")


main()


"""
Tidtagning:

Linear Time:
When you search for the last artist in the file the linear search will have to go
through all artists in the list which will take alot of time.
This also shows the worst case scenario for the linear search.

Binary Time:
For binary time it wont be the optimal element as it will have to do log(n) searches.

Hash Table:
It doesn't matter where the element is in list, it will take a static amount of time to find it.

The last artist in the list can also show up earlier in the list which means that the linear function will not go
to the end of the list to find the artist, which will make the test inconclusive as it depends on if the artist
appears earlier in the list.

When we tried an artist 'Tha Alkaholiks featuring King Tee' that appears in the end of the list the linear function
took 463.8079  seconds to finish.

The linear search took  463.8079  seconds
The binary search took  0.0249  seconds
The hash search took  0.0023  seconds
"""

"""
Timecomplexity:

Bubblesort: O(n^2). The bubblesort algorithm has an exponential increase in time, 
so when we use much larger datasets the bubble sort takes alot longer time than 
the quicksort algorithm. They are approximately the same when we use 10 data elements.

Quicksort: O(n*log(n))

Hash - O(1)
Linear - O(n)
Binary - O(log n)



"""


