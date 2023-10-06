from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

class Hash():
    def bcrpt(password : str):
        return pwd_context.hash(password)
    
    def verify(hashedpass, plainpass):
        return pwd_context.verify(plainpass, hashedpass)