from passlib.hash import pbkdf2_sha256 as cryp

hash = cryp.hash('senhasecreta')
print(hash)


print(cryp.verify('senhasecreta',hash))

print(cryp.verify('outrasenha',hash))
