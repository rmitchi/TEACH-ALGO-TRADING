# I want to make a user

# def create_user(name, age):
# 	return {"name": name, "age":age, "gender": "M"}


# if age>18:
# 	user1 = create_user("Parth", 25)
# 	user2 = create_user("Karan", 24)


class User:

	def __init__(self, i_name, i_age):

		self.name = i_name
		self.age = i_age


user1 = User("Parth", 25)
user2 = User("jksdfj", 15)

if user2.age <= 18:
	print("This is can not make account")
print(user1.age)
