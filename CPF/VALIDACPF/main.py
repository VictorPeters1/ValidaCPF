from valida_cpf import coloca_mascara_cpf, cpf_valido

while True:
    cpf = input("Informe o CPF a ser verificado: ")
    if not cpf:
        break
    if cpf_valido(cpf):
        print("CPF Válido:", coloca_mascara_cpf(cpf))
    else:
        print("CPF Inválido:", cpf)
