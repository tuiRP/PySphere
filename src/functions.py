# pysphere/src/functions.py

def calculate_damage(strength, weapon_power):
    """
    Calcula o dano baseado na força e no poder da arma.

    Args:
        strength (int): A força do personagem.
        weapon_power (int): O poder da arma.

    Returns:
        int: O dano calculado.
    """
    return strength * weapon_power

# Testando a função
if __name__ == '__main__':
    print(calculate_damage(10, 5))  # Saída esperada: 50

