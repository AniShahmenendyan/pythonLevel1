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


class Account:
    exch = {'dollar': 485, 'euro': 550, "rubly": 6, 'dram': 1}

    def __init__(self, id, name, balance=0, currency='dram'):
        self._id = id
        self._name = name
        self._balance = balance
        self._currency = currency

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @property
    def currency(self):
        return self._currency

    @name.setter
    def name(self, name):
        raise ValueError("can't change name")

    @balance.setter
    def balance(self, balance):
        raise ValueError("can't change balance")

    @currency.setter
    def currency(self, currency):
        raise ValueError("can't change currency")

    @id.setter
    def id(self, id):
        raise ValueError("can't change id")

    @staticmethod
    def exchange(cur, selfcur, bal):
        if cur != selfcur:
            res = int(Account.exch[cur] / Account.exch[selfcur] * bal)
            return res
        else:
            return bal

    def credit(self, c, ccur='dram'):
        r = self.exchange(ccur, self.currency, c)
        self._balance = self.balance + r
        print(f'{self.name} balance is {self.balance} {self.currency}')
        print('=' * 50)

    def debit(self, d, dcur='dram'):
        r = self.exchange(dcur, self.currency, d)
        if r <= self.balance:
            self._balance = self.balance - r
            print(f'{self.name} balance is {self.balance} {self.currency}')
            print('=' * 50)
            return True
        else:
            print("havn't enough balance")
            print('=' * 50)
            return False

    def transferto(self, t, tcur, another_account):
        debit = self.debit(t, tcur)
        if debit:
            print(f'{self.name} transferted {t} {tcur}, your current balance is {self.balance} {self.currency}')
            print('=' * 50)
            another_account.credit(t, tcur)
        else:
            print("havn't enough balance to transfer")
            print('=' * 50)

    def __str__(self):
        k = int(self.balance * Account.exch[self.currency] / Account.exch['dollar'])
        return f'{self.name} balance is {k} dollars'


class SavingsAccount(Account):
    def __init__(self, id, name, balance, currency, interest=4):
        super().__init__(id, name, balance, currency)
        self.__interest = interest

    @property
    def interest(self):
        return self.__interest

    @interest.setter
    def interest(self, interest):
        raise ValueError("can't change interest")

    def inter(self):
        self.credit(self.balance * (self.interest / 100), self.currency)
        print(f'{self.name} balance is {self.balance} {self.currency}')
        print('=' * 50)


class CurrentAccount(Account):
    def __init__(self, id, name, balance, currency, overdraft_limit=0):
        super().__init__(id, name, balance, currency)
        self.__overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, overdraft_limit):
        raise ValueError("can't change overdraft_limit")

    def debit(self, d, dcur):
        r = self.exchange(dcur, self.currency, d)

        if r <= self.balance + self.overdraft_limit:
            self._balance = self.balance - r
            print(f'{self.name} balance is {self.balance} {self.currency}')
            print('=' * 50)
        else:
            print("Sorry, you have reached you overdraft limit")
            print('=' * 50)

    def __add__(self, other):
        if type(self) == type(other):
            self.credit(other.balance, other.currency)
            print('=' * 50)
            print(f'{self.name} and {other.name} account')
            return self
        else:
            print("accounts can't add")


class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return f'The name of our person is: {self.name}'

    def __hash__(self):
        return hash(self.ssn)


class Bank:
    def __init__(self):
        self.account_dict = {}

    def assign_account(self, account, person):
        person_id = hash(person)
        if person_id in self.account_dict.keys():
            self.account_dict[person_id].append(account)
        else:
            self.account_dict.update({person_id: [account]})

    def inter(self):
        for accounts in self.account_dict.values():
            for account in accounts:
                if isinstance(account, SavingsAccount):
                    account.inter()

    def total_money(self, ssn, currency='dram'):
        bal = 0
        ssn_accounts = self.account_dict[hash(ssn)]
        for ssn_account in ssn_accounts:
            bal += ssn_account.exchange(ssn_account.currency, currency, ssn_account.balance)

        return bal


account = Account('id', 'name', 100000, 'dram')
account.credit(10, 'dollar')
account.debit(20000)
print(account)

account_2 = SavingsAccount('id', 'name', 100000, 'dram')
account_3 = CurrentAccount('id', 'name', 50000, 'dram')
print(account_2)
acba = Bank()
acba.assign_account(account_2, Person('John', 1234567))
acba.assign_account(account_3, Person('John', 1234567))
acba.inter()
print(account_2)
print(account_3)
print(acba.total_money(1234567, 'dollar'))
