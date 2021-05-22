from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib
import os

def generar_llave_aes_from_password(password):
    password = password.encode('utf-8')
    derived_key = HKDF(algorithm=hashes.SHA256(),length=32,salt=None,info=b'handshake data ',backend=default_backend()).derive(password)
    return derived_key

def cifrar(texto, llave_aes, iv):
    aesCipher = Cipher(algorithms.AES(llave_aes), modes.CTR(iv),backend=default_backend())
    cifrador = aesCipher.encryptor()
    cifrado = cifrador.update(texto)
    cifrador.finalize()
    return cifrado

def descifrar(cifrado, llave_aes, iv):
    aesCipher = Cipher(algorithms.AES(llave_aes), modes.CTR(iv),backend=default_backend())
    descifrador = aesCipher.decryptor()
    plano = descifrador.update(cifrado)
    descifrador.finalize()
    return plano
    
def generar_iv():
    iv=os.urandom(16)
    return iv


#Funciones para validar el numero de intentos.

def generar_hash_password(password_usuario):
    hasher=hashlib.sha512()
    hasher.update(password_usuario.encode('utf-8'))
    return hasher.hexdigest()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def diferencia_segundos_ahora(tiempo):
    ahora = datetime.datetime.now(timezone.utc)
    diferencia = ahora - tiempo
    return diferencia.seconds

def puede_intentar(ip):
    """
    """
    #Primer caso la ip es nueva
    registro_guardado  = models.Intentos_por_IP.objects.filter(pk=ip)
    if not registro_guardado:
        registro = models.Intentos_por_IP(ip=ip, contador=1, ultima_peticion=datetime.datetime.now())
        registro.save()
        return True
    registro_guardado = registro_guardado[0]
    diferencia_tiempo = diferencia_segundos_ahora(registro_guardado.ultima_peticion)
    if diferencia_tiempo > 60:
        registro_guardado.ultima_peticion = datetime.datetime.now()
        registro_guardado.contador = 1
        registro_guardado.save()
        return True
    else:
        if registro_guardado.contador < 3:
            registro_guardado.ultima_peticion = datetime.datetime.now()
            registro_guardado.contador += 1
            registro_guardado.save()
            return True
        else:
            registro_guardado.ultima_peticion =  datetime.datetime.now()
