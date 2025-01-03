from pickle import loads, dumps

class Save_load():
    def save(self, objectData, path):
        buffer = dumps(objectData)

        file = open(path,'wb')
        file.write(buffer)
        file.close()

    def load(self, path):

        file = open(path, 'rb')
        buffer = file.read(buffer)
        file.close()

        loads(buffer)

    def save_as(self, path):
        pass


