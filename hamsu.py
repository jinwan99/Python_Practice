# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance+money}원 입니다.")
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print(f"출급이 완료되었습니다. 잔액은 {balance-money}원입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원입니다.")
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
print(balance)
# balance = withdraw(balance,2000)
# print(balance)
# balance = withdraw(balance, 500)
# print(balance)
commission, balance = withdraw_night(balance, 500)
print(f"수수료 {commission}원이며, 잔액은 {balance}원입니다.")
