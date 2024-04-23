# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

def ranking(vitorias, derrotas):
    saldo_ranking = vitorias - derrotas
    
    if saldo_ranking <= 10:
        return 'Ferro'
    elif saldo_ranking > 11 and saldo_ranking <= 20:
        return 'Bronze'
    elif saldo_ranking > 21 and saldo_ranking <= 50:
        return 'Prata'
    elif saldo_ranking > 51 and saldo_ranking <= 80:
        return 'Ouro'
    elif saldo_ranking > 81 and saldo_ranking <= 90:
        return 'Diamante'
    elif saldo_ranking > 91 and saldo_ranking <= 100:
        return 'Lendario'
    else:
        return 'Imortal'
    

saldo_vitorias = 20 - 5
nivel = ranking(20, 5)
print(f'O heroi tem o saldo de {saldo_vitorias} e está no nível {nivel}')