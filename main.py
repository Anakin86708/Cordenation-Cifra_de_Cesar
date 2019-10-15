import sys, requests as rq, json as js
from hashlib import sha1

def decifrar(numero_casas, cifrado):
    cifrado = cifrado.lower()
    lst_decifrado = []

    for char in cifrado:
        char = ord(char)
        if char >= 97 and char <= 122:
            # Caracteres do alfabeto
            if char >= 97 and char <= (97 + (numero_casas -1)):
                # Necessário atenção esperial, pois apenas somar irá exceder o limite do alfabeto [b,z]
                lst_decifrado.append(char + (26 - numero_casas))
            else:
                # Caso de não precisar de um tratamento especial [a,u]
                lst_decifrado.append(char-numero_casas)
        else:
            # Qualquer outro caractere, como pontuação
            lst_decifrado.append(char)

    # Transforma todo a lista de volta em carateres e em seguida string
    str_decifrado = list(map(chr,lst_decifrado))
    return ''.join(str_decifrado)


api = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token="+sys.argv[1]
post_ = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token="+sys.argv[1]

request = rq.get(api)
if request.status_code == rq.codes.ok:
    data = request.json()

    with open("answer.json", "r+") as file_out:
        js.dump(data,file_out)
    decifrado = decifrar(data["numero_casas"],data["cifrado"])

    data["decifrado"] = decifrado
    with open("answer.json", "r+") as file_out:
        js.dump(data, file_out)

    data["resumo_criptografico"] = sha1(decifrado.encode('utf-8')).hexdigest()
    with open("answer.json", "r+") as file_out:
        js.dump(data, file_out)

    answer = {"answer":open("answer.json","rb")}
    response = rq.post(post_,files=answer)

    print("Resultado: %d" % response.status_code)
else:
    print("Connection error %d" % rq.status_code)
