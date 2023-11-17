import re

def fix_payments():
    return "Para atualizar os métodos de pagamento, entre em contato com o suporte no número (11)9 7788-4455"

def track_orders():
    return "Para acompanhar o pedido, acesse o email que confirma o envio e copie o código de rastreio. Logo em seguida, acesse o site dos correios e digite o código para rastrear seu pedido"

def main():
    intent_dict = {
        # Intenções para atualizar informações pagamentos 
        r"(pag)|(atuali)": "payments",

        # Intenções para acompanhar pedidos 
        r"(entre)|(rastr)|(pedid)": "tracking",
    }  

    action_dict = {
        "tracking": track_orders(),
        "payments":fix_payments()
    }


    # Esse loop while tem a função de manter o script rodando 
    while True:
        command = input("Digite o seu comando: (Caso deseje sair digite 'sair') ")
        if command == 'sair':
            break
        for key, value in intent_dict.items():
            pattern = re.compile(key)
            groups = pattern.findall(command)
            if groups:
                print(f"{action_dict[value]}", end=" ")

    else:
        print("Comando não reconhecido.")

if __name__ == '__main__':
    main()