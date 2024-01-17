from faker import Faker


def generate_random_cables(amount):
    numbers = []
    faker = Faker()

    while len(numbers) < amount:
        random = faker.random_int(min=1, max=50)
        if random not in numbers:
            numbers.append(random)
    return numbers
