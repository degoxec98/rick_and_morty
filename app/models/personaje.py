class Personaje:
    def __init__(self, id, name,status,gender,image):
        self.id = id
        self.name = name
        self.status = status
        self.gender = gender
        self.image = image

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'status' : self.status,
            'gender' : self.gender,
            'image' : self.image
            }