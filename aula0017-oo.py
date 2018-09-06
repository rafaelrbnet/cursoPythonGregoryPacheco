'''
classe
objeto
construtor
métodos
atributos
herança

sobrecarga
polimorfirsmo
destrutores

'''


class Pessoa(object):
    nome = 'João'
    sobrenome = 'Silva'
    idade = 33


obj = Pessoa()

print('Dados da Pessoa. Nome: {}, Sobrenome: {}, Idade: {}'.format(obj.nome, obj.sobrenome, obj.idade))
