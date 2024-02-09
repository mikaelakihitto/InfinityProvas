class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self._tipo_combustivel = tipo_combustivel
        self._valor_litro = valor_litro
        self._quantidade_combustivel = quantidade_combustivel

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    @property
    def valor_litro(self):
        return self._valor_litro

    @property
    def quantidade_combustivel(self):
        return self._quantidade_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, novo_tipo_combustivel):
        self._tipo_combustivel = novo_tipo_combustivel

    @valor_litro.setter
    def valor_litro(self, novo_valor_litro):
        self._valor_litro = novo_valor_litro

    @quantidade_combustivel.setter
    def quantidade_combustivel(self, nova_quantidade_combustivel):
        self._quantidade_combustivel = nova_quantidade_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Abastecidos {litros_abastecidos:.2f} litros. Valor total: R$ {valor_abastecido:.2f}"
        else:
            return "Quantidade de combustível insuficiente."

    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Abastecidos {litros_abastecidos:.2f} litros. Valor total: R$ {valor_pagar:.2f}"
        else:
            return "Quantidade de combustível insuficiente."


# Exemplo de uso
bomba = BombaCombustivel("Gasolina", 5.0, 100.0)
print(bomba.abastecer_por_valor(50))  # Abastecidos 10.00 litros. Valor total: R$ 50.00
print(bomba.abastecer_por_litro(20))  # Quantidade de combustível insuficiente.

# Exemplo de uso dos getters e setters
print(bomba.tipo_combustivel)  # Gasolina
bomba.tipo_combustivel = "Etanol"
print(bomba.tipo_combustivel)  # Etanol

print(bomba.valor_litro)  # 5.0
bomba.valor_litro = 5.5
print(bomba.valor_litro)  # 5.5

print(bomba.quantidade_combustivel)  # 100.0
bomba.quantidade_combustivel = 150.0
print(bomba.quantidade_combustivel)  # 150.0




