# Cordenation-Crifra_de_Cesar

Desafio proposto para participação na aceleração sobre **React**.

## Enunciado
>O primeiro passo é você salvar o conteúdo do JSON em um arquivo com o nome answer.json, que irá usar no restante do desafio.
>
>Você deve usar o número de casas para decifrar o texto e atualizar o arquivo JSON, no campo decifrado. O próximo passo é gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1 e atualizar novamente o arquivo JSON. OBS: você pode usar qualquer biblioteca de criptografia da sua linguagem de programação favorita para gerar o resumo sha1 do texto decifrado.
>
>Seu programa deve submeter o arquivo atualizado para correção via POST para a API:
>
>>https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN
>
>OBS: a API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML, com um campo do tipo file com o nome answer. Considere isso ao enviar o arquivo.
