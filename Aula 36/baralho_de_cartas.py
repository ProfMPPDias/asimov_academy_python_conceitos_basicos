import random

# ─────────────────────────────────────────────
#  Constantes do baralho
# ─────────────────────────────────────────────
NAIPES = ["♠ Espadas", "♥ Copas", "♦ Ouros", "♣ Paus"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CORINGA = "🃏 Coringa"


# ─────────────────────────────────────────────
#  Funções
# ─────────────────────────────────────────────

def gerar_baralho(copias: int = 1, coringas: bool = False, embaralhar: bool = False) -> list[str]:
    """
    Gera e retorna um baralho de cartas.

    Parâmetros:
        copias     (int)  : quantidade de baralhos completos a incluir (padrão: 1).
        coringas   (bool) : se True, adiciona 2 coringas por cópia (padrão: False).
        embaralhar (bool) : se True, embaralha o baralho antes de retornar (padrão: False).

    Retorna:
        list[str]: lista com todas as cartas do baralho.
    """
    baralho = []
    for _ in range(copias):
        for naipe in NAIPES:
            for valor in VALORES:
                baralho.append(f"{valor} de {naipe}")
        if coringas:
            baralho.extend([CORINGA, CORINGA])

    if embaralhar:
        random.shuffle(baralho)

    return baralho


def mostrar_baralho(baralho: list[str]) -> None:
    """
    Exibe a quantidade de cartas no baralho e lista todas elas.

    Parâmetros:
        baralho (list[str]): o baralho a ser exibido.
    """
    print(f"\n{'═' * 45}")
    print(f"  🃏  BARALHO  —  {len(baralho)} carta(s)")
    print(f"{'═' * 45}")
    for i, carta in enumerate(baralho, start=1):
        print(f"  {i:>3}. {carta}")
    print(f"{'═' * 45}\n")


def dar_as_cartas(baralho: list[str], jogadores: int, cartas_por_jogador: int) -> dict[str, list[str]]:
    """
    Distribui cartas do baralho entre os jogadores.

    Parâmetros:
        baralho             (list[str]): o baralho de onde as cartas serão retiradas.
        jogadores           (int)      : número de jogadores.
        cartas_por_jogador  (int)      : quantidade de cartas que cada jogador recebe.

    Retorna:
        dict[str, list[str]]: dicionário mapeando o nome de cada jogador à sua mão.

    Levanta:
        ValueError: se não houver cartas suficientes no baralho.
    """
    total_necessario = jogadores * cartas_por_jogador
    if total_necessario > len(baralho):
        raise ValueError(
            f"Cartas insuficientes! São necessárias {total_necessario} cartas, "
            f"mas o baralho tem apenas {len(baralho)}."
        )

    maos: dict[str, list[str]] = {f"Jogador {j + 1}": [] for j in range(jogadores)}

    for _ in range(cartas_por_jogador):
        for jogador in maos:
            maos[jogador].append(baralho.pop(0))

    return maos


def mostrar_jogadores(maos: dict[str, list[str]]) -> None:
    """
    Exibe a mão de cada jogador (quantidade e cartas).

    Parâmetros:
        maos (dict[str, list[str]]): dicionário com as mãos dos jogadores.
    """
    print(f"\n{'═' * 45}")
    print("  👥  MÃOS DOS JOGADORES")
    print(f"{'═' * 45}")
    for jogador, cartas in maos.items():
        print(f"\n  {jogador}  ({len(cartas)} carta(s)):")
        for carta in cartas:
            print(f"      • {carta}")
    print(f"\n{'═' * 45}\n")


# ─────────────────────────────────────────────
#  Demonstração
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "═" * 45)
    print("  SIMULADOR DE BARALHO DE CARTAS")
    print("═" * 45)

    # 1. Gerar baralho com 1 cópia, com coringas e embaralhado
    baralho = gerar_baralho(copias=1, coringas=True, embaralhar=True)

    # 2. Mostrar o baralho completo
    mostrar_baralho(baralho)

    # 3. Distribuir cartas para 4 jogadores, 5 cartas cada
    NUM_JOGADORES = 4
    CARTAS_POR_JOGADOR = 5

    print(f"  Distribuindo {CARTAS_POR_JOGADOR} cartas para {NUM_JOGADORES} jogadores...\n")
    maos = dar_as_cartas(baralho, jogadores=NUM_JOGADORES, cartas_por_jogador=CARTAS_POR_JOGADOR)

    # 4. Mostrar as mãos dos jogadores
    mostrar_jogadores(maos)

    # 5. Mostrar o que sobrou no baralho
    print(f"  Cartas restantes no baralho: {len(baralho)}")
    mostrar_baralho(baralho)