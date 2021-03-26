import random


class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return "{}({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        ataque_efetivo = int((self.ataque * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo

        print("{} perdeu {} pontos de vida".format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print("{} foi derrotado".format(pokemon))
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f"{self} lançou uma bola de fogo na cabeça de {pokemon}")
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print(f"{self} lançou um jato d'água em {pokemon}")
        return super().atacar(pokemon)
        
class PokemonPlanta(Pokemon):
    tipo = "planta"

    def atacar(self, pokemon):
        print(f"{self} lançou Overgrow em {pokemon}")
        return super().atacar(pokemon)

class PokemonInseto(Pokemon):
    tipo = "inseto"

    def atacar(self, pokemon):
        print(f"{self} lançou uma picada em {pokemon}")
        return super().atacar(pokemon)

class PokemonNormal(Pokemon):
    tipo = "normal"

    def atacar(self, pokemon):
        print(f"{self} lançou uma patada em {pokemon}")
        return super().atacar(pokemon)

class PokemonEscuro(Pokemon):
    tipo = "escuro"

    def atacar(self, pokemon):
        print(f"{self} lançou uma magia negra em {pokemon}")
        return super().atacar(pokemon)

class PokemonVenenoso(Pokemon):
    tipo = "venenoso"

    def atacar(self, pokemon):
        print(f"{self} lançou um veneno em {pokemon}")
        return super().atacar(pokemon)

class PokemonChao(Pokemon):
    tipo = "chao"

    def atacar(self, pokemon):
        print(f"{self} lançou um golpe em {pokemon}")
        return super().atacar(pokemon)

class PokemonGelo(Pokemon):
    tipo = "gelo"

    def atacar(self, pokemon):
        print(f"{self} lançou um raio de gelo em {pokemon}")
        return super().atacar(pokemon)

class PokemonFada(Pokemon):
    tipo = "fada"

    def atacar(self, pokemon):
        print(f"{self} lançou um encanto em {pokemon}")
        return super().atacar(pokemon)

class PokemonAco(Pokemon):
    tipo = "aco"

    def atacar(self, pokemon):
        print(f"{self} lançou uma pedra de aço em {pokemon}")
        return super().atacar(pokemon)

class PokemonLutador(Pokemon):
    tipo = "lutador"

    def atacar(self, pokemon):
        print(f"{self} lançou uma rasteira em {pokemon}")
        return super().atacar(pokemon)

class PokemonPsiquico(Pokemon):
    tipo = "psiquico"

    def atacar(self, pokemon):
        print(f"{self} lançou uma confusão em {pokemon}")
        return super().atacar(pokemon)

class PokemonPedra(Pokemon):
    tipo = "pedra"

    def atacar(self, pokemon):
        print(f"{self} lançou um pedregulho em {pokemon}")
        return super().atacar(pokemon)

class PokemonFantasma(Pokemon):
    tipo = "fantasma"

    def atacar(self, pokemon):
        print(f"{self} lançou uma maldição em {pokemon}")
        return super().atacar(pokemon)

class PokemonDragao(Pokemon):
    tipo = "dragão"

    def atacar(self, pokemon):
        print(f"{self} lançou uma chama de fogo em {pokemon}")
        return super().atacar(pokemon)

class PokemonVoador(Pokemon):
    tipo = "voador"

    def atacar(self, pokemon):
        print(f"{self} lançou um golpe aéreo em {pokemon}")
        return super().atacar(pokemon)