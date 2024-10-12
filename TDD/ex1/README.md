<h1>Exercício 1 📝</h1>

O objetivo desta atividade é implementar uma validação para o objeto Person, considerando algumas regras de negócios, e realizar essa implementação usando a técnica de Test-Driven Development (TDD). 

O sistema deve validar os seguintes aspectos de um objeto Person:

- <strong> Nome: </strong> deve ser composto por pelo menos duas partes e cada parte deve ser composta apenas por letras.

- <strong> Idade: </strong> deve estar dentro do intervalo de 1 a 200 anos.

- <strong> E-mail: </strong> a pessoa deve ter pelo menos um e-mail associado a ela, e o nome do e-mail deve seguir o formato: inicio@meio.fim (onde cada parte tem pelo menos um caractere).
<div align="center">

![image](https://github.com/user-attachments/assets/c318c10a-8a85-438e-a12b-7c9f4a0bc429)

</div>
<h2> ▶️ Manual de execução </h2>

🔗 1. Clone o repositório:
```
    git clone https://github.com/JuliaGayotto/Qualidade-Testes-de-Software
```

🖥️ 2. No cmd, navegue até a pasta do exercício 1 e crie um ambiente virtual:
```
    cd TDD/ex1
    pyton -m venv nome_da_venv
    nome_da_venv\Scripts\activate
```

📥 3. Instale as dependências necessárias para executar o código:
```
    pip install -r requirements.txt 
```

▶️ 4. Execute os testes:
```
    pytest
```
