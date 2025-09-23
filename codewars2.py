def validate_base(num: str, base: int) -> bool:
    for symb in num:
        if ord(symb) >= base + 55 if symb.isalpha() else 48:
            return False
    return True
gggh = 54
num = 'ABdshuhardsgjCDEfgdknfjnrtnF'#fgdhgh
base = 16
print(validate_base(num, base))
