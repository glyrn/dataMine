# this is a system for bank managent

# 用户模块
# 用户实体只需要有名字以及密码就行
class user:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.acts = []
  
  def __str__(self):
    return f"username: {self.username}, num of act: {len(self.acts)}"

# 账户模块
class account:
  def __init__(self, userId):
    self.userId = userId
    self.money = 0


# 银行类
# 
# 用户表
# 用户表需要记录用户ID，用户账号，用户密码

# 账户表
# 账户表需要记录账户id， 用户id， 账户金额
# 注意 一个用户可以有多个账户，不同的账户有的金额可以不同

class bank:
  def __init__(self):
    self.userIdList = {}
    self.accountList = {}
    self.uil = 0
    self.atl = 0

  def register(self):
    username = input("请输入用户名")
    password = input("请输入密码")
    self.userIdList[self.uil] = user(username, password)
    self.uil+=1

  def login(self):
    username = input("请输入用户名")
    password = input("请输入密码")
    # 这里使用循环遍历字典，后期优化可以考虑使用hashcode
    for userid, userObj in self.userIdList.items():
      if user.username == username and user.password == password:
        print("登录成功！")
        return userid
    print("账户不存在！")
    return None
  # 创建账户，注意一个用户可以有多个账户
  def creatAccount(self, userId):
    self.accountList[self.atl] = account(userId)
    self.userIdList[userId].acts.append(self.atl)
    self.atl += 1

  # 根据用户id查找这个用户的账户id的集合
  def searchAccountByUserId(self, userId):
    accountIds = []
    for accountId, accountObj in self.accountList.items():
      if accountObj.userId == userId:
         accountIds.append(accountId)
    return accountIds

  # 从一个账户转账到另一个账户
    # 如果账户余额为负数则撤销这次交易，并输出交易非法
  def transferMoney(self, fromId, toId, amount):
    
    fromAccount = self.accountList.get(fromId)
    toAccount = self.accountList.get(toId)

    
    if fromAccount and toAccount:
      
      if fromAccount.money >= amount:
        fromAccount.money -= amount
        toAccount.money += amount
        print("转账成功！")
      else:
        print("账户余额不足，转账失败！")
        
    else:
      print("账户不存在，转账失败！")


def main():
    myBank = bank()

    while True:
        print("欢迎来到银行管理系统")
        print("1. 注册新用户")
        print("2. 用户登录")
        print("3. 退出系统")

        choice = input("请选择服务：")

        if choice == "1":
            myBank.register()
        elif choice == "2":
            userId = myBank.login()
            if userId is not None:
                userMenu(myBank, userId)
        elif choice == "3":
            print("谢谢使用，再见！")
            break
        else:
            print("无效的选择，请重新输入。")


def userMenu(myBank, userId):
    while True:
        print("用户菜单")
        print("1. 创建账户")
        print("2. 转账")
        print("3. 返回上级菜单")

        choice = input("请选择服务：")

        if choice == "1":
            myBank.createAccount(userId)
        elif choice == "2":
            fromId = int(input("请输入转出账户ID："))
            toId = int(input("请输入转入账户ID："))
            amount = float(input("请输入转账金额："))
            myBank.transferMoney(fromId, toId, amount)
        elif choice == "3":
            break
        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()




