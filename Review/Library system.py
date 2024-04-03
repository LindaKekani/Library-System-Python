# Storage lists
users = []
resources = []


# To add users
class User:
    def __init__(self, user_id, name, email, cellNumber, checked_out=None):
        user = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "cellNumber": cellNumber,
            "checked_out": checked_out if checked_out is not None else [],
        }


# To add users
def add_user(user_id, name, email, cellNumber):
    user = User(user_id, name, email, cellNumber)
    users.append(user)
    print("User id ", user_id, "added.")
    return user


# To add resources


class Resource:
    def __init__(self, resource_id, title, author, genre):
        resource = {
            "resource_id": resource_id,
            "title": title,
            "author": author,
            "genre": genre,
            "status": "available",
        }


def add_resource(resource_id, title, author, genre):
    new_resource = Resource(resource_id, title, author, genre)
    resources.append(Resource)
    print("Resource", resource_id, "added.")
    return new_resource


# To check-in resources


def check_in(resource_id, user_id):
    resource = None
    user = None

    # identify resources
    for res in resources:
        if res["resource_id"] == resource_id:
            resource = res
            break

    # to identify users
    for usr in users:
        if usr["user_id"] == user_id:
            user = usr
            break

    if resource is None:
        print("resource with ID ", resource_id, "is not added.")
        return False

    # Find user
    if user is None:
        print("User ID ", user_id, "is not found")
        return False

    if resource["status"] == "available":
        user["check_out"].remove(resource)
        print("Resource ", resource_id, "is availlable.")
        return True
    else:
        print("Resource ", resource_id, "is not available for check-in")
        return False


# To check-out resources


def check_out(resource_id, user_id):  # info needed to check in and out resource
    resource = None
    user = None

    # To find user with user id
    for usr in users:
        if usr["user_id"] == user_id:
            user = usr
            break

    # Find resource with resource id
    for res in resources:
        if res["resource_id"] == resource_id:
            resource = res
            break

    if resource is None:
        print("Resource ", resource_id, "is not available.")
        return False

    if user is None:
        print("User with ID ", user_id, "is not found.")
        return False

    if resource["status"] == "available":
        user["checked_out"].append(resource)
        print("Resource ", resource_id, "is available")
        return True
    else:
        print("Resource ", resource_id, "is already checked out.")


def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Add Resource")
        print("3. Check Out Resource")
        print("4. Check In Resource")
        print("5. Exit")

        choice = str(input("Enter your choice: "))

        if choice == "1":
            user_id = input("Enter user ID: ")
            name = input("Enter user's name: ")
            email = input("Enter email: ")
            cellNumber = input("Enter cell number (10 digits): ")

            print("User added")
            add_user(user_id, name, email, cellNumber)

        elif choice == "2":
            resource_id = input("Enter resource ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            add_resource(resource_id, title, author, genre)

        elif choice == "3":
            resource_id = input("Enter resource ID: ")
            user_id = input("Enter user ID: ")

            if check_out(resource_id, user_id):
                print("Check out successful.")
            else:
                print("Unable to checkout")

        elif choice == "4":
            resource_id = input("Enter resource ID: ")
            user_id = input("Enter user Id: ")

            if check_in(resource_id, user_id):
                print("Check in successful.")
            else:
                print("Not successful.")
                break

        elif choice == "5":
            print("Leaving the Library system....")
            break


if __name__ == "__main__":
    main()
