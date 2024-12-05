
class Auth:
    def __init__(self,idusuario=None, username=None, password=None):
        self.idusuario = idusuario
        self.username = username
        self.password = password
        
    @classmethod
    def from_dict(cls, data):
        # Asumiendo que 'data' es un diccionario con las claves 'username' y 'password'
        return cls(username=data.get('username'), password=data.get('password'))
    

    def __repr__(self):
        return f"<User {self.username}>"
