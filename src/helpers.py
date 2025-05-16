import faker


def register_new_user_and_return_email_password_name():
    fake = faker.Faker("ru_RU")
    email = fake.email()
    password = fake.password(lower_case=True)
    name = fake.first_name()
    return email, password, name
