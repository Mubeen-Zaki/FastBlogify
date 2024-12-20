from passlib.context import CryptContext

class Hash():
    pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')
    @staticmethod
    def bcrypt(password : str):
        hashed_password = Hash.pwd_cxt.hash(password)
        return hashed_password
    @staticmethod
    def verify(request_password, user_password):
        return Hash.pwd_cxt.verify(request_password, user_password)