def validate_email(email: str) -> bool:
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    import re
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС."""
    import re
    pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$'
    return bool(re.match(pattern, snils))