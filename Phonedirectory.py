class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_world=False
        self.phone_numbers=[]

class Phonedirectory:
    def __init__(self):
        self.root=TrieNode()

    def add_contact(self,name,phone_numbers):
        node=self.root
        for char in name.lower():
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_world=True
        node.phone_numbers.append(phone_numbers)

    def search_contacts(self,query):
        node=self.root
        for char in query.lower():
            if char not in node.children:
                return []
            node=node.children[char]
        
        re=[]
        self._collect_all_contacts(node,query,re)
        return re
    
    def _collect_all_contacts(self,node,prefix,re):
        if node.is_end_of_world:
            for phone_number in node.phone_numbers:
                re.append((prefix,phone_number))
        for char,child_node in node.children.items():
            self._collect_all_contacts(child_node,prefix+char,re)

    def display(self):
        print("\n All Contacts:")
        re=[]
        self._collect_all_contacts(self.root,"",re)
        if re:
            for name,phone in re:
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")
        print()


if __name__=="__main__":
    directory=Phonedirectory()
    while True:
        print("\n Phone directory Menu:")
        print("1.Add contact")
        print("2.Search Contact")
        print("3.Display all contacts")
        print("4.Exit")
        choice=input("Enter your choice (1-4): ")

        if choice=="1":
            name=input("Enter contact name: ").strip()
            phone_number=input("Enter phone number: ").strip()
            directory.add_contact(name,phone_number)
            print(f"Contact '{name}' added succesfully.")

        elif choice=="2":
            query=input("enter character to search: ").strip()
            re=directory.search_contacts(query)
            if re:
                print("\n Search results:")
                for name,phone in re:
                    print(f"{name}:{phone}")
            else:
                print("No Contacts found with the given characters.")
            
        elif choice=="3":
            directory.display()

        elif choice=="4":
            print("Existing phone directory.Goodbye!")
            break
        
        else:
            print("Invalid choice! please enter a number between 1 and 4")