raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
id_check = "ID05"
is_present = id_check in unique_users
raw_count = len(raw_logs)
unique_count = len(unique_users)
print("Raw logs:", raw_logs)
print("Unique users:", unique_users)
print(f"Is {id_check} present", is_present)
print(f"Raw count: {raw_count}|Unique count: {unique_count}")
print(f"Duplicates removed: {raw_count - unique_count}")