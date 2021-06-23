from flask_bcrypt import Bcrypt 
from werkzeug.security import generate_password_hash, check_password_hash

bcrypt = Bcrypt()

password = 'omnish@123'

hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)

check_pass1 = bcrypt.check_password_hash(hashed_password,'wrongpass')
check_pass2 = bcrypt.check_password_hash(hashed_password,'omnish@123')

print(check_pass1,check_pass2)


hashed_password2 = generate_password_hash(hashed_password)

print(hashed_password2)

print(check_password_hash(hashed_password2,hashed_password))
