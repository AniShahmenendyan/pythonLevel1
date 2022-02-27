#
# 1. Եկեք ստեղծենք հաճախորդի բանկային հաշվի կլաս.
#     - ունի 4 instance attribute-ներ՝ id, name, balance, currency, որոնք read-only են (հնարավոր չլինի ուղիղ ձևով փոխել)
#     - որպես class attribute տարբեր դրամային արժույթների համար ունենալ փոխանակման գործակիցներ
#     - ունի երեք մեթոդներ, credit, debit և transferTo
#     - credit - ավելացնել բալանսը տրված չափով
#     - debit - եթե հաշվի վրա բավարար գումար կա, նվազեցնել հաշվի գումարը տրված չափով
#     - transferTo - տրված չափով գումարը փոխանցել մեկ այլ բանկային հաշվի, հաշվի առնել currency-ն
#     - սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա հաշվի մնացորդը դոլարով

# 1. Let's create a customer bank account class.
# - has 4 instance attributes: id, name, balance, currency, which are read-only (can not be changed directly)
# - have exchange rates for different currencies as a class attribute
# - has three methods: credit, debit և transferTo
# - credit - increase the balance by the given amount
# - debit - if there is enough money in the account, reduce the amount of the account by the given amount
# - transferTo - transfer the given amount to another bank account, take into account the currency
# - define the __str__ method. This method will show us the account balance in dollars



# 2. Օգտագործելով Account կլասը, ստեղծել SavingsAccount(ավանդային հաշիվ) և CurrentAccount(ընթացիկ հաշիվ) կլասներ։
#     - ավանդային հաշիվը բանկային հաշվի ատրիբուտներից բացի պետք է ունենա նաև interest(տոկոսադրույք) և մեթոդ որով
#     կավելանա հաճախորդի հաշիվը տոկոսադրույքի չափով։
#     - ընթացիկ հաշիվը բանկային հաշվի ատրիբուտներից բացի պետք է ունենա overdraft limit ատրիբուտ
#     - ընթացիկ հաշվի բալասը կարող է մինուս արժեքներ ընդունել overdraft limit-ի չափով
#     - կարիքի դեպքում սուպերկլասի մեթոդները կարող են override արվել
#     - սահմանել հաշիվների իրար գումարումը, եթե նրանք նույն տիպի են
# 2. Using the Account class, create SavingsAccount and CurrentAccount classes.
# - deposit account in addition to bank account attributes must also have և interest (interest rate) և method by which
# will increase the customer's account by the interest rate.
# - The current account must have an overdraft limit attribute in addition to the bank account attributes
# - The current account balance can accept minus values in the amount of overdraft limit
# - Superclass methods can be override if needed
# - set the sum of accounts if they are of the same type


# 3. Ստեղծել Person կլաս, որը կունենա երկու instance attribute՝ name և ssn(հանրային ծառայությունների համարանիշ) int տիպի
#     - սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա մարդու անունը
#     - սահմանել __hash__ մեթոդը։ Այս մեթոդը պետք է վերադարձնի մարդու հանրային ծառայությունների համարանիշը
# 3. Create a Person class that will have two instance attributes: name and ssn (social service number) int type
# - define the __str__ method. This method will show us the name of the person
# - define the __hash__ method. This method should return the person a public service number


# 4. Ստեղծել Bank կլաս, որի instance-ը իր մեջ կարող է պարունակել տարբեր տիպի բանկային հաշիվներ և որոնք կապված են որոշակի
#     անձանց հետ։ Մեկ անձը կարող է ունենալ մեկից ավելի հաշիվներ։
#     - հաշիվների ցուցակը կարող ենք պահել dictionary-ի մեջ
#     - բանկը պետք է ունենա մեթոդներ փոփոխելու համար հաշիվների բալանսը, օգտագործելով բանկային հաշիվների մեթոդները
#     - եթե հաշիվը overdraft-ում է, բանկը կարող է նամակ գրել հաշվին հապակցված անձին։
#     - բանկը պետք է հնարավորություն ունենա ssn-ի միջոցով ստուգել անձի բոլոր հաշիվների ընդհանուր գումարը՝
#     դոլարային արժույթով
# 4. Create a Bank class, the instance of which may contain different types of bank accounts և which are linked
# with persons. One person can have more than one account.
# - We can save the list of accounts in the dictionary
# - the bank must have methods to change the balance of the accounts using the bank account methods
# - if the account is overdraft, the bank can write a letter to the person associated with the account.
# - the bank should be able to check the total amount of the person's accounts via ssn in dollar currency
