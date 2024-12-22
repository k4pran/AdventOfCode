def calc_secret_number(secret):
    new_secret = secret * 64
    new_secret = new_secret ^ secret
    new_secret %= 16777216

    nb_divided = new_secret // 32
    new_secret = nb_divided ^ new_secret
    new_secret %= 16777216

    nb_mulled = new_secret * 2048
    new_secret = nb_mulled ^ new_secret
    new_secret %= 16777216


    return new_secret

with open("day22.txt", 'r') as f:
    lines = f.read().splitlines()

    iterations = 2000
    secrets = []
    for line in lines:
        secret_number = int(line)
        for i in range(iterations):
            new_secret_number = calc_secret_number(secret_number)
            secret_number = new_secret_number
        secrets.append(secret_number)
        print(secret_number)


    result = sum(secrets)
    print(f"\nDay 22-1: {result}")
