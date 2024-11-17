
#Crie uma classe base chamada Veiculo que tenha um método chamado movimentar. Este método deve imprimir a mensagem "Veículo está em movimento." para indicar que qualquer veículo está em movimento. Em seguida, crie duas subclasses chamadas Carro e Moto que herdem de Veiculo. Dentro de cada uma dessas subclasses, sobrescreva o método movimentar para imprimir mensagens específicas para cada tipo de veículo. Na classe Carro, o método movimentar deve imprimir "Carro está dirigindo.", enquanto na classe Moto, o método deve imprimir "Moto está acelerando.

class Veiculo:
    
    def movimentar(self):
        return 'O Veiculo esta em movimento.'

class Carro(Veiculo):
    
    def movimentar(self):
        return 'O Carro Esta sendo dirigido.'

class Moto(Veiculo):
    
    def movimentar(self):
        return 'a Moto esta acelerando.'
    

veicuo_1 = Carro()
veiculo_2 = Moto()
carro = Veiculo()

print(carro.movimentar())

print(veicuo_1.movimentar())
print(veiculo_2.movimentar())