import hashlib
def generar_hash_password(password_usuario):
    hasher=hashlib.sha512()
    hasher.update(password_usuario.encode('utf-8'))
    return hasher.hexdigest()
