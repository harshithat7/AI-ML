friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b
unique_to_b = friend_b - friend_a
print("Shared interests: ",shared_interests)
print("All interests: ",all_interests)
print("Unique to A: ",unique_to_a)
print("Unique to B: ",unique_to_b)

