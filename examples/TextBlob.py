from textblob import TextBlob


text = ('Режисер віднісся до екранізації з повагою, він намагався'
        'якнайбільше підійти до першоджерела. Як людині, котрій не'
        ' сподобалась екранізація Дракули з Ґеррі Олдманом та Кіану Рівзом,'
        ' я можу з впевненістю сказати, що «Воно» — гідна перегляду'
        ' кіноадаптація. Якщо ви прихильник жахів, особливо якісних і'
        ' атмосферних, то у вас залишилося ще 2-3 тижні, щоб сходити і'
        ' переконатися у правдивості цього огляду. ')


analyser = TextBlob(text).translate(to="en")
print(f'Text translated to english:\n {analyser}')
print()
print(f'Subjectivity of the given text: {analyser.subjectivity}')
