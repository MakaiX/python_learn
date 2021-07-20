class Father(object):

    def __init__(self, name):
        self.name = name
        print('name: {0}'.format(self.name))

    def getName(self):
        return ('The Name is {0}'.format(self.name))


class Son(Father):
    def __init__(self, name):
        print('Hi')
        self.name = name

    def getName(self):
        print('Name: {0}'.format(self.name))


if __name__ == '__main__':
    son = Son('Runn')

    print(son.getName())
