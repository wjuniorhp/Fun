from itertools import permutations as permt


def i_oposto(p, i_og):
    num_fatias = len(p)
    return int((i_og + (num_fatias / 2)) % num_fatias)

def igualdade_das_somas_opostas(p, i):
    return p[i - 1] + p[i] == p[i_oposto(p, i - 1)] + p[i_oposto(p, i)]

def info_somas(p, i):
    print(f"posicões: {i-1,i} {i_oposto(p, i - 1), i_oposto(p, i)}\n"
          f"{p[i - 1]} + {p[i]} = {p[i - 1] + p[i]}\n"
          f"{p[i_oposto(p, i - 1)]} + {p[i_oposto(p, i)]} = "
          f"{p[i_oposto(p, i - 1)] + p[i_oposto(p, i)]}\n"
          f"{'-'*20}")

if __name__=="__main__":
    fatias = list(range(1,11))
    print(fatias)
    tam = len(fatias)

    num_possibs = 0
    for possibilidade in permt(fatias):
        if possibilidade[0]==1:
            corretas = 0
            for i in range(1,tam):
                if igualdade_das_somas_opostas(possibilidade, i):
                    corretas += 1
                    if corretas >= tam-1:
                        num_possibs +=1
                        print(f"Solução {num_possibs}: {possibilidade}")
                else:
                    break

    # for i in range(1, tam):
    #     info_somas(pizza_final,i)

    print(f"{num_possibs} possíveis pizzas-soluções!")
