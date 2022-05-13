from user import User

class Admin(User):
    """Represents the special kind of user"""

    def __init__(self, first_name, last_name, age, location):
        """Initialize the different attributes"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


class Privileges():
    """List the following set of privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


ramon_user = Admin('Ramon', 'Montoya', '20', 'USA')
brian_user = User('Brian', 'Morales', '19', 'USA')
karla_user = User('Karla', 'Guzman', '19', 'USA')
eli_user = User('Elizabeth', 'Nava', '19', 'USA')
sabino_user = User('Sabino', 'Mendez', '19', 'USA')

ramon_user.describe_user()
ramon_user.privileges.show_privileges()
print("\nAdding privileges...")
ramon_user_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    'can install updates',
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
ramon_user.privileges.privileges = ramon_user_privileges
ramon_user.privileges.show_privileges()
ramon_user.greet_user()

brian_user.describe_user()
brian_user.greet_user()

karla_user.describe_user()
karla_user.greet_user()

eli_user.describe_user()
eli_user.greet_user()

sabino_user.describe_user()
sabino_user.greet_user()