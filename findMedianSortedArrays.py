def findMedianSortedArrays(list1, list2):
    combined_list = list1 + list2
    res = [int(x) for x in combined_list]
    combined_sorted = sorted(res)

    if int(len(combined_sorted) % 2) == 0:
        median_check = int(len(combined_sorted) / 2)
        print(sum((combined_sorted[median_check],combined_sorted[median_check-1])) / 2)
    else:
        odd_median_check = int(len(combined_sorted) / 2)
        print(combined_sorted[odd_median_check])

nums1 = str(input("Enter first set of numbers:"))
list1 = nums1.split(",")

nums2 = str(input("Enter second set of numbers:"))
list2 = nums2.split(",")

findMedianSortedArrays(list1,list2)