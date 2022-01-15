from faker import Faker
fake_data= Faker()
profile = fake_data.simple_profile()
for m,v in profile.items():
    print('{}: {}'.format(m,v))