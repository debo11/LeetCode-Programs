def addTwoNumbers(list1, list2):
    merged_list1 = [''.join(list1)]
    merged_list2 = [''.join(list2)]

    results1 = [int(i) for i in merged_list1]
    results2 = [int(i) for i in merged_list2]
    reverse_list1 = int(str(results1)[::-1].replace("[", " ").replace("]", " ").strip())
    reverse_list2 = int(str(results2)[::-1].replace("[", " ").replace("]", " ").strip())

    final_list = reverse_list1 + reverse_list2
    res = [int(x) for x in str(final_list)]
    print(res[::-1])


nums1 = str(input("Enter first set of numbers:"))
list1 = nums1.split(",")

nums2 = str(input("Enter second set of numbers:"))
list2 = nums2.split(",")
addTwoNumbers(list1,list2)
