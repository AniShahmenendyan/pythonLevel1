# 1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# Տրված է ամբողջ թվերի զանգված/լիստ և նպատակային արժեք (target)։ Վերադարձնել լիստի միջի այն երկու թվերի ինդեքսները
# որոնց գումարը հավասար է նպատակին։
# Կարող ենք համարել, որ լուծում միշտ գոյություն ունի և միայն մի հատ է։

def two_sum(arr, target):
    pass


# 2․ You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Տրված է տարբեր օրերին որոշակի ապրանքի արժեքները պարունակող լիստ։ Համարել, որ ինդեքսները օրերն են։ Ընտրելով մեկ
# օր և գնելով ապրանքը ապա վաճառելով մեկ այլ օր՝ մենք ենք ուզում ստանալ առավելագույն շահույթ։
# Եթե շահույթ ստանալ հնարավոր չէ, վերադարձնել 0։

def profit(prices):
    pass


# 3. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Տրված է ամբողջ թվերի զանգված/լիստ։ Վերադարձնել նոր answer լիստ, որտեղ answer[i]-ն հավասար կլինի օրիգինալ լիստի
# բոլոր տարրերի արտադրյալին բացի i-րդ տարրից։
# Գրել կոդ, որը կաշխատի O(n) ժամանակային բարդությամբ։

# Օրինակ՝
# Input: [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# 4. You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Դուք աստիճաններ եք բարձրանում։ Ընդհանուր կա n աստիճան:
# Կարող եք աստիճանները բարձրանալ կամ մեկ քայլով կամ երկու։ Քանի՞ հնարավոր տարբերակ կա ամենավերևը հասնելու։

# Example:
#   Input: n = 3
#   Output: 3
#   Explanation: There are three ways to climb to the top.
#     1. 1 step + 1 step + 1 step
#     2. 1 step + 2 steps
#     3. 2 steps + 1 step

# 5. You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.
# Դուք պրոֆեսիոնալ գող եք և պատրաստվում եք մի գիշերվա ընթացքում որոշակի փողոցի տները թալանել։ Ամեն տուն պարունակում է
# որոշակի քանակությամբ գումար։ Միակ սահմանափակումն այն է, որ իրար կողք գտնվող տները ունեն միասնական անվտանգության
# համակարգ, որը ակտիվանում է, եթե մի գիշերվա ընթացքում այդ կապակցված տները մտնեն։
#
# Տրված է ամբողջ թվերի լիստ։ Թվերը իրենցից ներկայացնում են ամեն տան մեջ գտնվող գումարը։ Վերադարձնել առավելագույն
# գումարը, որը կարող ենք թալանել մի գիշերվա ընթացքում առանց անվտանգության համակարգն ակտիվացնելու։

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
