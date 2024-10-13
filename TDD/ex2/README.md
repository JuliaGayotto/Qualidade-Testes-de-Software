<h1>Exercício 2 📝</h1>

O participante deve implementar uma calculadora de salário de funcionários. Um funcionário contem nome, email, salário-base e cargo. De acordo com seu cargo, a regra para cálculo do salário líquido é diferente:

- Caso o cargo seja DESENVOLVEDOR, o funcionário terá desconto de 20% caso o salário seja maior ou igual que 3.000,00, ou apenas 10% caso o salário seja menor que isso;

- Caso o cargo seja DBA ou TESTADOR, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 2.000,00, ou apenas 15% caso o salário seja menor que isso;

- Caso o cargo seja GERENTE, o funcionário terá desconto de 30% caso o salário seja maior ou igual que 5.000,00, ou apenas 20% caso o salário seja menor que isso.
<br>

<h2> ▶️ Manual de execução </h2>

🔗 1. Clone o repositório:
```
    git clone https://github.com/JuliaGayotto/Qualidade-Testes-de-Software
```

🖥️ 2. No cmd, navegue até a pasta do exercício 2 e crie um ambiente virtual:
```
    cd TDD/ex2
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
