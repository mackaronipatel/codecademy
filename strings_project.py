def username_generator(first_name,last_name):
  if (len(first_name) < 3) or (len(last_name) < 4):
    username = first_name+last_name
    return username
  else:
    username = first_name[:3]+last_name[:4]
    return username

username_test = username_generator("Zi", "Hieli")
print(username_test)

def password_generator(username):
  password = ""
  for i in range(0,len(username)):
    password += username[i-1]
  return password

print(password_generator("NikhilThota"))

