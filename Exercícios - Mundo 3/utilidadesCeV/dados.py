def leiaDinheiro(ss):
    s0 = input(ss).replace(',', '.')
    if s0.isalpha():
        while not s0.isnumeric():
            print(f'ERRO: "{s0}" é um preço inváido!')
            s0 = input(ss)
        return int(s0)
    else:
        return s0
