from emails import Email
from person import Person

class PersonDAO:
    def isValidToInclude(self, p: Person) -> list:
        errors = []

        # Valida o nome
        if len(p.name.split()) < 2 or not all(part.isalpha() for part in p.name.split()):
            errors.append("O nome deve ser composto por ao menos 2 partes e deve possuir apenas letras.")

        # Valida a idade
        if not (1 <= p.age <= 200):
            errors.append("A idade deve estar entre 1 e 200.")

        # Valida se há emails
        if not p.emails or len(p.emails) == 0:
            errors.append("A pessoa deve ter pelo menos um email associado a ela.")
        # Valida se o(s) email(s) existentes estão no formato correto
        else:
            for email in p.emails:
                if not self.isValidEmail(email.name):
                    errors.append(f"O email {email.name} não está no formato válido ____@____.____.")

        return errors

    # Função que faz a validação do formato do email
    def isValidEmail(self, email: str) -> bool:
        if '@' not in email or '.' not in email:
            return False
        local, domain = email.split('@', 1)
        domain_parts = domain.split('.')
        if len(local) < 1 or len(domain_parts) < 2 or any(len(part) < 1 for part in domain_parts):
            return False
        return True
