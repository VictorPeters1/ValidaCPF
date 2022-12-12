from random import randint, random


def dv1_p1(cpf):
    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))


def dv1_p2(cpf):
    resultado = dv1_p1(cpf) * 10 % 11
    return resultado if resultado < 10 else 0


def dv2_p1(cpf):
    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))


def dv2_p2(cpf):
    resultado = (dv2_p1(cpf) + dv1_p2(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0


def dv_final(cpf):
    return str(dv1_p2(cpf)) + str(dv2_p2(cpf))


def filtra_mascara(cpf):
    return ''.join([n for n in cpf if n.isdigit()])


def dv_original(cpf):
    return cpf[-2:]


def retira_dv(cpf):
    return cpf[:-2]

def verifica_tamanho(cpf):
    cpf = filtra_mascara(cpf)
    return len(cpf) == 11


def cpf_valido(cpf):
    cpf = filtra_mascara(cpf)
    return dv_original(cpf) == dv_final(retira_dv(cpf)) and verifica_tamanho(
        cpf
    )

def coloca_mascara_cpf(cpf):
    cpf = filtra_mascara(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def gera_cpf(formatado=False):
    cpf = "".join([str(randint(0, 9)) for i in range(9)])
    cpf += dv_final(cpf)
    return cpf if not formatado else coloca_mascara_cpf(cpf)


def gera_cpf_2():
    cpf = str(random())[2:11]
    return cpf


def gera_lista_cpfs(qtd=10, formatado=False):
    return [gera_cpf(formatado) for i in range(qtd)]