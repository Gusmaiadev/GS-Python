import re


def menu_principal():
    print("Bem vindo ao Meu Pedria ON")
    print("Digite a opção que desejar:")
    print("1. Quem somos")
    print("2. Cadastro")
    print("3. Login")
    print("4. Encerrar Programa")
    opcao = input("Digite a opção escolhida:")
    return opcao


def quem_somos():
    print("O Meu Pediatra ON é um site que oferece um serviço de acompanhamento infantil na área da saúde.")
    print("Ele permite que os pais cadastrem os perfis de seus filhos e tenham acesso a diversas funcionalidades")
    print("que podem ajudar a cuidar da saúde e do bem-estar dos pequenos. Uma das funcionalidades é o ")
    print("cadastro das vacinas que seus filhos já tomaram e o recebimento de lembretes das próximas doses, para que")
    print("eles não percam o calendário vacinal. Outra funcionalidade é a consulta das medicações que seus filhos ")
    print("podem tomar de acordo com a idade deles e as orientações médicas, para que eles não corram o risco de tomar")
    print("remédios inadequados ou em doses erradas. Além disso, o site também ajuda os pais a localizar os hospitais")
    print("que estão próximos a eles que sejam do SUS e a ver as avaliações de outros usuários, para que eles possam")
    print("escolher o melhor atendimento para seus filhos em caso de emergência. O site também oferece um perfil")
    print("completo da criança com documentos como RG e dados sobres históricos médicos e familiares, para que")
    print("os pais tenham todas as informações importantes sobre seus filhos em um só lugar. O Meu Pediatra ON é")
    print("um site que visa facilitar a vida dos pais e garantir a saúde e o desenvolvimento dos filhos.")

    print("Digite a opção que desejar:")
    print("1. Voltar ao menu principal")
    opcao = input("Digite a opção escolhida:")
    return opcao


def cadastro():
    nome = input("Digite seu nome completo (máximo 40 caracteres):")
    while len(nome) > 40 or not all(x.isalpha() or x.isspace() for x in nome):
        nome = input("Nome inválido. Digite novamente:")
    data_nascimento = input("Digite sua data de nascimento (xx/xx/xxxx):")
    while not re.match(r'\d{2}/\d{2}/\d{4}', data_nascimento):
        data_nascimento = input("Data de nascimento inválida. Digite novamente:")
    sexo = input("Digite seu sexo (máximo 15 caracteres):")
    while len(sexo) > 15 or not sexo.isalpha():
        sexo = input("Sexo inválido. Digite novamente:")
    email = input("Digite seu melhor e-mail:")
    while not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        email = input("E-mail inválido. Digite novamente:")
    senha = input("Crie sua senha:")
    senha = '*' * len(senha)
    confirma_senha = input("Confirme sua senha:")
    confirma_senha = '*' * len(confirma_senha)
    while senha != confirma_senha:
        confirma_senha = input("As senhas não coincidem. Digite novamente:")
        confirma_senha = '*' * len(confirma_senha)
    dados = [nome, data_nascimento, sexo, email, senha, confirma_senha]
    print("Cadastro concluído com sucesso")
    print("1. Ir para o menu de login")
    print("2. Voltar ao menu principal")
    opcao = input("Digite a opção escolhida:")
    if opcao == '1':
        return '3', dados
    else:
        return opcao, dados


def meu_perfil(dados, filhos):
    print("Meu Perfil")
    print("Nome: ", dados[0])
    print("Data de Nascimento: ", dados[1])
    print("Sexo: ", dados[2])
    print("Email: ", dados[3])
    for i, filho in enumerate(filhos):
        print("Dependente ", i + 1, ": ", filho['nome'])
    print("1. Voltar ao menu anterior")
    print("2. Deslogar de minha conta")
    opcao = input("Digite a opção escolhida:")
    return opcao



def cadastrar_filho():
    print("Cadastro de Filho(a)")
    nome = input("Digite o nome completo da criança:")
    while len(nome) > 40 or not all(x.isalpha() or x.isspace() for x in nome):
        nome = input("Nome inválido. Digite novamente:")
    sexo = input("Digite o sexo da criança:")
    while len(sexo) > 15 or not sexo.isalpha():
        sexo = input("Sexo inválido. Digite novamente:")
    data_nascimento = input("Digite a data de nascimento da criança (xx/xx/xxx):")
    while not re.match(r'\d{2}/\d{2}/\d{4}', data_nascimento):
        data_nascimento = input("Data de nascimento inválida. Digite novamente:")
    nome_pai = input("Nome completo do pai:")
    while len(nome_pai) > 40 or not all(x.isalpha() or x.isspace() for x in nome_pai):
        nome_pai = input("Nome inválido. Digite novamente:")
    nome_mae = input("Nome completo da mãe:")
    while len(nome_mae) > 40 or not all(x.isalpha() or x.isspace() for x in nome_mae):
        nome_mae = input("Nome inválido. Digite novamente:")
    historico_doenca = input("A familia da criança possui algum histórico de doença? Se sim, especifique:")
    alergia = input("A criança tem alergia a algum medicamento ou alimento? Se sim, especifique:")
    doenca_cronica = input("A criança possui alguma doença cronica? Se sim, especifique:")
    cirurgia = input("A criança ja fez alguma cirurgia? Se sim, especifique:")
    doenca_especifica = input(
        "Seu filho ja pegou alguma doença especifica (varicela, sarampo, caxumba, rubéola)? Se sim, especifique:")
    hospitalizacao = input("A criança ja ficou hospitalizada? Se sim, especifique o porque:")
    altura = input("Digite a altura da criança:")
    while not re.match(r'\d+(\.\d{1,2})?', altura):
        altura = input("Altura inválida. Digite novamente:")
    peso = input("Digite o peso da criança, apenas numeros inteiros: ")
    while not re.match(r'\d+(\.\d{1,2})?', peso):
        peso = input("Peso inválido. Digite novamente:")
    rg = input("Digite o RG da criança (xx.xxx.xxx-x:")
    while not re.match(r'\d{1,2}\.\d{3}\.\d{3}-\d{1,2}', rg):
        rg = input("RG inválido. Digite novamente:")
    filho = {
        'nome': nome, 'sexo': sexo, 'data_nascimento': data_nascimento,
        'nome_pai': nome_pai, 'nome_mae': nome_mae, 'historico_doenca': historico_doenca,
        'alergia': alergia, 'doenca_cronica': doenca_cronica, 'cirurgia': cirurgia,
        'doenca_especifica': doenca_especifica, 'hospitalizacao': hospitalizacao,
        'altura': altura, 'peso': peso, 'rg': rg, 'vacinas': []
    }
    print("Criança cadastrada com sucesso")
    print("1. Voltar ao menu principal")
    opcao = input("Digite a opção escolhida:")
    return opcao, filho


def perfil_crianca(filhos):
    if not filhos:
        print("Nenhuma criança cadastrada")
        print("1.Retornar para cadastrar criança")
        print("2. Voltar ao menu principal")
        opcao = input("Digite a opção escolhida:")
        return opcao
    else:
        for i, filho in enumerate(filhos):
            print(i + 1, ". ", filho['nome'])
        opcao = input("Digite o número da criança:")
        if 1 <= int(opcao) <= len(filhos):
            filho = filhos[int(opcao) - 1]
            print("Nome: ", filho['nome'])
            print("Sexo: ", filho['sexo'])
            print("Data de Nascimento: ", filho['data_nascimento'])
            print("Nome do Pai: ", filho['nome_pai'])
            print("Nome da Mãe: ", filho['nome_mae'])
            print("Histórico de Doença: ", filho['historico_doenca'])
            print("Alergia: ", filho['alergia'])
            print("Doença Crônica: ", filho['doenca_cronica'])
            print("Cirurgia: ", filho['cirurgia'])
            print("Doença Específica: ", filho['doenca_especifica'])
            print("Hospitalização: ", filho['hospitalizacao'])
            print("Altura: ", filho['altura'])
            print("Peso: ", filho['peso'])
            print("RG: ", filho['rg'])
            print("Vacinas: ", filho['vacinas'])
            print("1. Cadastrar novo dependente")
            print("2. Voltar ao menu principal")
            opcao = input("Digite a opção escolhida:")
            return opcao
        else:
            print("Número inválido. Tente novamente.")
            return '2'

def cadastrar_vacina(filhos):
    if not filhos:
        return '1'

    print("Cadastre a vacina que seu filho tomou")

    print("Escolha a criança:")
    for i, filho in enumerate(filhos):
        print(f"{i + 1}. {filho['nome']}")

    opcao_crianca = input("Digite o número da criança:")
    if 1 <= int(opcao_crianca) <= len(filhos):
        filho = filhos[int(opcao_crianca) - 1]

        nome_vacina = input("Digite o nome da vacina:")
        data_aplicacao = input("Digite a data que a vacina foi aplicada (xx/xx/xxxx):")
        while not re.match(r'\d{2}/\d{2}/\d{4}', data_aplicacao):
            data_aplicacao = input("Data de aplicação inválida. Digite novamente:")

        vacina = {'nome': nome_vacina, 'data_aplicacao': data_aplicacao}
        filho['vacinas'].append(vacina)

        print("Vacina em analise...")
        print("Precisamos que confirme o dependente que deseja cadastrar a vácina")
        print("Digite 1 para continuar que enviaremos os nome dos depentes")
        print("1. Continuar")
        opcao = input("Digite a opção escolhida:")
        return opcao
    else:
        print("Número inválido. Tente novamente.")



def login(dados):
    if len(dados) < 5:
        print("Por favor, cadastre-se primeiro.")
        return '2'  # Retorna para o menu de cadastro

    filhos = []
    while True:  # Adicione este loop
        email = input("Digite seu e-mail:")
        senha = input("Digite sua senha:")
        senha = '*' * len(senha)
        if email == dados[3] and senha == dados[4]:
            while True:
                print("Você está Logado e Online")
                print("1. Meu Perfil")
                print("2. Perfil da criança")
                print("3. Cadastrar filhos(a)")
                print("4. Medicamentos")
                print("5. Vacinas")
                print("6. IMC infântil")
                print("7. Encerrar programa")
                opcao = input("Digite a opção escolhida:")
                if opcao == '1':
                    opcao = meu_perfil(dados, filhos)
                    if opcao == '2':
                        break
                elif opcao == '2':
                    opcao = perfil_crianca(filhos)
                    if opcao == '1':
                        opcao, filho = cadastrar_filho()
                        filhos.append(filho)
                elif opcao == '3':
                    opcao, filho = cadastrar_filho()
                    filhos.append(filho)
                elif opcao == '5':
                    cadastrar_vacina(filhos)
                    opcao = perfil_crianca(filhos)
                elif opcao == '7':
                    return '4'
                elif opcao == '6':
                     opcao = calcular_imc(filhos)
                elif opcao == '4':
                    opcao = medicamentos()
            break  # Adicione esta linha para sair do loop quando o login for bem-sucedido
        else:
            print("E-mail ou senha inválidos.")
            print("1. Voltar ao menu principal")
            opcao = input("Digite a opção escolhida:")
            if opcao == '1':
                return '1'  # Retorna para o menu principal

def calcular_imc(filhos):
    if not filhos:
        print("Nenhum dependente cadastrado")
        return '1'

    print("Calcular IMC Infantil")
    print("Escolha a criança:")
    for i, filho in enumerate(filhos):
        print(f"{i + 1}. {filho['nome']}")

    opcao_crianca = input("Digite o número da criança:")
    if 1 <= int(opcao_crianca) <= len(filhos):
        filho = filhos[int(opcao_crianca) - 1]

        altura = float(filho['altura'])
        peso = float(filho['peso'])
        imc = peso / (altura ** 2)

        print(f"O IMC de {filho['nome']} é {imc:.2f}")

        if imc < 18.5:
            print(f"{filho['nome']} está abaixo do peso.")
        elif imc <= 24.9:
            print(f"{filho['nome']} está com peso normal.")
        else:
            print(f"{filho['nome']} está acima do peso.")

    print("1. Voltar ao menu principal")
    opcao = input("Digite a opção escolhida:")
    return opcao

def medicamentos():
    print("Bem vindo à área de medicamentos")
    print("REMEDIOS INDICADOS DE 0 A 3 ANOS: ")
    print("\nDOR DE BARRIGA")
    print("PARACETAMOL: O paracetamol é um analgésico e antitérmico que pode ser utilizado para aliviar a dor de barriga infantil.")
    print("\nBUSCOPAN: Na versão em gotas, o butilbrometo de escopolamina pode ser pingado em uma colher e engolido diretamente ou ser")
    print("dissolvido em um pouco de água para disfarçar o gosto. Essa é a versão mais indicada para recém-nascidos,")
    print("crianças de até 6 anos, grávidas e lactantes.")
    print("\nFEBRE")
    print("PARACETAMOL TYLENOL: : Indicado para crianças de até três anos de idade para a redução da febre e para o alívio temporário")
    print("de dores leves a moderadas associadas a gripes e resfriados comuns, dor de cabeça, dor de dente e dor de garganta.")
    print("\nDIPIRONA (NOVALGINA): A dipirona também é indicada para baixar a febre das crianças, mas se comparado com o paracetamol,")
    print("os efeitos colaterais da dipirona são maiores. Menores de 3 meses de idade ou pesando menos de 5 kg não devem ser tratadas")
    print("com NOVALGINA. É recomendada supervisão médica quando se administra dipirona a crianças pequenas.")
    print("TYLENOL® Bebê: Pode ser usado desde o 1º dia de vida para a redução da febre e alívio das dores comuns da infância, como o "
    "nascimento dos dentes, cólicas e algumas reações pós-vacina.")
    print("\nDORES MUSCULARES")
    print("BUSCOPAN: Na versão em gotas, o butilbrometo de escopolamina pode ser pingado em uma colher e engolido diretamente ou ser"
    "dissolvido em um pouco de água para disfarçar o gosto. Essa é a versão mais indicada para recém-nascidos, crianças de até 6 anos.")
    print("\n Cetofenid (gel): O Cetofenid Gel é um medicamento indicado para o tratamento da dor.")
    print("\nGRIPE")
    print("PARACETAMOL TYLENOL: O paracetamol é um analgésico e antitérmico que pode ser utilizado para aliviar a gripe e a dor no corpo.")
    print("\nDIPIRONA (NOVALGINA): A dipirona também é indicada para gripe, mas se comparado com o paracetamol,")
    print("os efeitos colaterais da dipirona são maiores. Menores de 3 meses de idade ou pesando menos de 5 kg não devem ser tratadas")
    print("com NOVALGINA.")


    print("REMEDIOS INDICADOS DE 0 A 3 ANOS:")
    print("\nDOR DE BARRIGA")
    print("PARACETAMOL: O paracetamol é um analgésico e antitérmico que pode ser utilizado para aliviar a dor de barriga infantil.")
    print("\nBUSCOPAN: Na versão em gotas, o butilbrometo de escopolamina pode ser pingado em uma colher e engolido diretamente ou ser")
    print("dissolvido em um pouco de água para disfarçar o gosto. Essa é a versão mais indicada para recém-nascidos,")
    print("crianças de até 6 anos, grávidas e lactantes.")
    print("\nFEBRE")
    print("PARACETAMOL TYLENOL: : Indicado para crianças de até três anos de idade para a redução da febre e para o alívio temporário")
    print("de dores leves a moderadas associadas a gripes e resfriados comuns, dor de cabeça, dor de dente e dor de garganta.")
    print("\nDIPIRONA (NOVALGINA): A dipirona também é indicada para baixar a febre das crianças, mas se comparado com o paracetamol,")
    print("os efeitos colaterais da dipirona são maiores. Menores de 3 meses de idade ou pesando menos de 5 kg não devem ser tratadas")
    print("com NOVALGINA. É recomendada supervisão médica quando se administra dipirona a crianças pequenas.")
    print("\nDORES MUSCULARES")
    print("BUSCOPAN: Na versão em gotas, o butilbrometo de escopolamina pode ser pingado em uma colher e engolido diretamente ou ser")
    print("dissolvido em um pouco de água para disfarçar o gosto. Essa é a versão mais indicada para recém-nascidos, crianças")
    print("\n Cetofenid (gel): O Cetofenid Gel é um medicamento indicado para o tratamento da dor.")
    print("\nGRIPE")
    print("de até 6 anos.")
    print("\nIBRUFENO ALIVIUM: O Ibuprofeno também é um remédio indicado para aliviar a febre, dor no corpo e de cabeça.")
    print("\nCARBINOXAMINA: A carbinoxamina é um antialérgico que ajuda a aliviar a coriza.")
    print("\nOSELTAMIVIR: O Oseltamivir é um antiviral que inibe a replicação do vírus e encurta o período de atividade")
    print("no organismo.")
    print("\nATENÇÃO: Lembre-se, é sempre importante consultar um profissional de saúde antes de administrar qualquer")
    print("medicamento a uma criança.")




    print("\n1. Voltar ao menu principal")
    opcao = input("Digite a opção escolhida:")
    return opcao


def main():
    dados = []
    filhos = []
    while True:
        opcao = menu_principal()
        if opcao == '1':
            opcao = quem_somos()
            if opcao == '1':
                continue  # Volta ao menu principal
        elif opcao == '2':
            opcao, dados = cadastro()
            if opcao == '3':
                opcao = login(dados)
        elif opcao == '3':
            opcao = login(dados)
        elif opcao == '4':
            break
        elif opcao == '5':
            opcao = cadastrar_vacina(filhos)
            if opcao == '1':
                continue
        # Volta ao menu principal

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()