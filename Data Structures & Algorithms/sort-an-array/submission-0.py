# Merge sort is nlogn time, but O(n) space. Quicksort doesnt change this. 
# I don't know heapsort well enough to implement from memory, revisit
# TODO: Change to heapsort to optimize space complexity to O(1) 
class Solution:
    def merge(self,arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        tempL = [0] * n1
        tempR = [0] * n2

        for i in range(n1):
            tempL[i] = arr[left + i]
        for j in range(n2):
            tempR[j] = arr[mid + 1 + j]
            
        i = 0  
        j = 0  
        k = left  

        while i < n1 and j < n2:
            if tempL[i] <= tempR[j]:
                arr[k] = tempL[i]
                i += 1
            else:
                arr[k] = tempR[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = tempL[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = tempR[j]
            j += 1
            k += 1
    def mergeSort(self,arr, left, right):
        if left < right:
            mid = (left + right) // 2

            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) -1)
        return nums
        