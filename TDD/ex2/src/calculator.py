from employee import Employee

class Calculator:
    def calculate(self, e: Employee) -> float:
        # Determina o salário líquido caso a cargo seja desenvolvedor
        if e.position == 'DESENVOLVEDOR':
            return e.base_salary * (0.80 if e.base_salary >= 3000 else 0.90)

        # Determina o salário líquido caso a cargo seja DBA ou testador
        elif e.position == 'DBA' or e.position == 'TESTADOR':
            return e.base_salary * (0.75 if e.base_salary >= 2000 else 0.85)

        # Determina o salário líquido caso a cargo seja gerente
        elif e.position == 'GERENTE':
            return e.base_salary * (0.70 if e.base_salary >= 5000 else 0.80)

        # Gera um erro caso o cargo inserido seja desconhecido
        else:
            raise ValueError(f"Cargo desconhecido")
