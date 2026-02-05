contacts = {
    "David": 1234567890,
    "Alice": 9876543210,
    "Bob": 9567843210 
}
contacts["John"] = 1122334455
print("Look up - Alice:", contacts.get("Alice"))
print("Look up - Susan:", contacts.get("Susan", "Contact not found"))
print("\nContacts: ")
for name, phone in contacts.items():
    print(f"Contact: {name}|Phone: {phone}")
