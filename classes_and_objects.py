#INICIO DO ESTUDO DE ORIENTAÇÃO A OBJETOS EM PYTHON

#estudo de classes e métodos

#classe: definição de um outro tipo de objetos
#método: funções associadas a uma classe

class Televisao:

	#método init será chamado sempre que criar objetos da classe (método construtor)
	#self -> parâmetro, pode ser entendido como o objeto em si
	#todo método em Python tem SELF como primeiro parâmetro
	#atributos de objetos devem ser associados ao SELF
	def __init__(self):	 
		self.ligada = False
		self.canal = 4
	
tv = Televisao()	#tv é um objeto da classe Televisao	(instância de Televisão)


class Carro:

	def criarNome(self, nome):
		self.nome=nome

	def criarAno(self, ano):
		self.ano = ano		

	def obterNome(self):
		return self.nome

	def obterAno(self):
		return self.ano

car = Carro()
car.criarNome('camaro')
car.criarAno(2010)
print(car.nome)
print(car.ano)

#Criar classes
class MyClass:	#classe chamada MyClass
	x=5			#propriedade nomeada x

p1 = MyClass()	#criar um objeto nomeada p1
print(p1.x)		#printa o valor de x

'''
-> os exemplos acima são classes e objeto em sua forma mais simples
-> mas eles não realmente são úteis em aplicações reais da vida
'''

'''
*Todas as classes tem uma função chamada "__init__()"
ela sempre é executada quando uma classe está sendo iniciada
*Use a função __init__() para assinalar valores para propriedas de objeto
ou outras operações que são necessariamente para fazer quando o objeto é criado
*"__init__()" é chamada toda vez que a classe é usada para criar um novo objeto
'''

class Pessoa:
	#atributos (características)
	def __init__ (self, nome, idade):
		self.nome = nome
		self.idade = idade

	#métodos (ações)
	def myfunc (self):
		print("Oi, meu nome é " + self.nome)



p1 = Pessoa("John", 36)
p1.myfunc
print(p1.nome)
print(p1.idade)


'''
as definições de classe não podem estar vazias, 
mas se, por algum motivo, você tiver uma definição 
de classe sem conteúdo, insira a instrução pass 
para evitar erros.
'''
class CabecaDoPresidente:
  pass




'''
HERANÇA EM PYTHON
*A herança nos permite definir uma classe 
que herda todos os métodos e propriedades
de outra classe.

*Classe pai é a classe que está sendo 
herdada, também chamada de classe base.

*Classe filho é a classe que herda de 
outra classe, também chamada classe derivada.
'''

'''
Criar uma classe pai

Qualquer classe pode ser uma classe pai,
portanto, a sintaxe é a mesma que a 
criação de qualquer outra classe:

'''

class Person:

	def __init__ (self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname (self):
		print(self.firstname, self.lastname)

# Use a classe Person para criar um objeto 
# e execute o método printname:

x = Person("John", "Doe")
x.printname()

'''
Criar uma classe filho

Para criar uma classe que herda a 
funcionalidade de outra classe, 
envie a classe pai como parâmetro ao 
criar a classe filha:
'''

class Student(Person):	#classe pai é PARAMETRO da classe filho (herança estabelecida)
	
	def __init__(self, fname, lname):		#A função __init __ () é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.
		#adicionar propriedades etc.
		'''Quando você adiciona a função __init __ (), 
		a classe filho não herdará mais a função __init __ () dos pais.'''

		Person.__init__(self, fname, lname) #Para manter a herança da função __init __ () dos pais, adicione uma chamada à função __init __ () dos pais:


x = Student("Mike", "Olsen")
x.printname() 


class Student(Person):	#classe pai é PARAMETRO da classe filho (herança estabelecida)
	
	def __init__(self, fname, lname):		#A função __init __ () é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.
		super().__init__(fname, lname) 
		#função super() fará a classe filha herdar todos os métodos e propriedades de seu pai:
		#Ao usar a função super (), você não precisa usar o nome do elemento pai, 
		#ele herdará automaticamente os métodos e propriedades do pai.

		self.graduationYear = 2021

		def welcome(self):
    		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationYear) 
    	#Se você adicionar um método na classe filho com o mesmo nome que uma função na classe pai, 
    	#a herança do método pai será substituída.

x = Student("Anderson", "Leandro", 2021)




