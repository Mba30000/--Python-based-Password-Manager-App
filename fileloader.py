from pickle import loads, dumps


def save(objectData, path):
        buffer = dumps(objectData)

        file = open(path,'wb')
        file.write(buffer)
        file.close()

def open(path):

        file = open(path, 'rb')
        buffer = file.read()
        file.close()
        data = loads(buffer)

        return data
