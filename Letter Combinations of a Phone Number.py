import itertools


def letterCombinations(list1):
    contact = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    combined_array = []
    for i in list1:
        for j in i:
            concat_value = ''
            for k, v in contact.items():
                if j in k:
                    combined_array.append(v)
                    for i in range(0, len(combined_array) + 1):
                        output = str(list(itertools.product(*combined_array)))
                        final_output = output.replace("', '", "").replace("(", "").replace(")", "").replace(",, ",",").replace(",]", "]")
                        print(final_output)


nums1 = str(input("Enter your numbers:"))
list1 = nums1.split()

letterCombinations(list1)
