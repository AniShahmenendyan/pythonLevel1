"""decorators"""


# 1. Գրել դեկորատոր և կիրառել number ֆունկցիայի վրա։ Դեկորացված ֆունկցիան պետք է վերադարձնի n-ը բազմապատկած 10-ով։


def number(n):
    return n


# 2. Գրել դեկորատոր type_check անունով։ Այն կստուգի դեկորացված ֆունկցիայի արգումենտների տիպը։ Եթե ֆունկցիային սխալ տիպ
# փոխանցենք, ապա բարձրացնել TypeError exception:
# Օրինակ, ունենք add_integers(a, b) ֆունկցիա, որը պետք է գումարի a, b թվերը։ Այն կարող ենք դեկորացնել
# type_check(int)-ով և եթե add_integers-ին փոխանցենք ոչ int պարամետր, մենք կստանանք TypeError

"""recursion"""

# 3. Write a recursive function to calculate the sum of elements of a list.
# Գրել ռեկուրսիվ ֆունկցիա, որը կվերադարձնի իրեն փոխանցված լիստի տարրերի գումարը։ Չօգտվել sum() կամ նման ֆունկցիաներից։

# 4. Write a recursive function to calculate the geometric sum of n, where r = 2, a = 1.
# Գրել ռեկուսրիվ ֆունկցիա, որը կհաշվի n տարրերի երկրաչափական գումարը, որտեղ r = 2, a = 1:
# Երկրաչափական գումարը՝ SUM(a * (r ** k)), որտեղ k աճում է 1-ից մինչև n:
