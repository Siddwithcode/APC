from abc import ABC, abstractmethod
class Authentication(ABC):
    @abstractmethod
    def authenticate(self): pass
class PasswordAuth(Authentication):
    def authenticate(self): print("Checking Password")
class BiometricAuth(Authentication):
    def authenticate(self): print("Checking Fingerprint")
BiometricAuth().authenticate()
