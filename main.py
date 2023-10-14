from telebot import types
import telebot

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    first = (f'Привет! Мой бот поможет тебе найти фильм и купить на него билет, '
             f'увидеть рецензию на него и узнать информацию о актерах, которые снимались в этих фильмах.'
             f'\nВ моем боте есть такие команды как:\n/films - Поиск фильмов')
    bot.send_message(message.chat.id, first, parse_mode='html')


@bot.message_handler(commands=['films'])
def films(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    a1 = types.InlineKeyboardButton('Вызов', callback_data='vov')
    a2 = types.InlineKeyboardButton('Джон Уик 4', callback_data='jon')
    a3 = types.InlineKeyboardButton('Крушение', callback_data='krysh')
    a4 = types.InlineKeyboardButton('Кунг-фу жеребец', callback_data='kynf')
    a5 = types.InlineKeyboardButton('Три мушкетера: Д’Артаньян', callback_data='three')
    a6 = types.InlineKeyboardButton('Переводчик', callback_data='translator')
    a7 = types.InlineKeyboardButton('Поехавшая', callback_data='gone')
    a8 = types.InlineKeyboardButton('Яга и книга заклинаний', callback_data='book')
    markup.add(a1, a2, a3, a5, a4, a6, a7, a8)
    bot.send_message(message.chat.id, text='Выберите фильм который хотите посмотреть:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'mainMen':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            a1 = types.InlineKeyboardButton('Вызов', callback_data='vov')
            a2 = types.InlineKeyboardButton('Джон Уик 4', callback_data='jon')
            a3 = types.InlineKeyboardButton('Крушение', callback_data='krysh')
            a4 = types.InlineKeyboardButton('Кунг-фу жеребец', callback_data='kynf')
            a5 = types.InlineKeyboardButton('Три мушкетера: Д’Артаньян', callback_data='three')
            a6 = types.InlineKeyboardButton('Переводчик', callback_data='translator')
            a7 = types.InlineKeyboardButton('Поехавшая', callback_data='gone')
            a8 = types.InlineKeyboardButton('Яга и книга заклинаний', callback_data='book')
            markup.add(a1, a2, a3, a5, a4, a6, a7, a8)
            bot.send_message(call.message.chat.id, text='Выберите фильм который хотите посмотреть:',
                             reply_markup=markup)

        if call.data == 'pay_vov':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='vov')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_jon':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='jon')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_krysh':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='krysh')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_kynf':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='kynf')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_three':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='three')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_translator':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='translator')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_gone':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='gone')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'pay_book':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="https://www.tinkoff.ru/rm/vodopyanov.ignat1/FKeJf34545")
            b3 = types.InlineKeyboardButton('Назад', callback_data='book')
            markup.add(url_button, b3)
            bot.send_message(call.message.chat.id, "Для того чтобы купить фильм перейдите на сайт:", reply_markup=markup)

        if call.data == 'vov':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('vov.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            vov = (f' Жанр: драма\nСтрана: Россия\nРежиссер: Клим Шипенко\nАктеры: Юлия Пересильд, '
                   f'Милош Бикович, Владимир Машков, Олег Новицкий'
                   f'\nРейтинг «Кинопоиска»: 7,5\nРейтинг IMDb: 6,7\nЦена: 330р.\nВо время выхода в открытый космос, совершая '
                   f'экстренный маневр, '
                   f'космонавт Олег Богданов получает тяжелую травму. Ему может помочь '
                   f'только торакальный хирург — Евгения Беляева, у которой хватает своих проблем на Земле.'
                   f'Это первый в мире фильм, сцены для которого были сняты в космосе — '
                   f'на Международной космической станции. Работа на орбите заняла около двух недель. '
                   f'Критики отмечают отличную игру актрисы Юлии Пересильд, '
                   f'а также визуальную сторону фильма в целом: операторскую работу и постановку тех самых сцен '
                   f'в космосе.')
            b1 = types.InlineKeyboardButton('Купить', callback_data='pay_vov')
            b2 = types.InlineKeyboardButton('Актеры', callback_data='vov_actors1')
            b3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(b1, b2, b3)
            bot.send_message(call.message.chat.id, vov, reply_markup=markup)

        if call.data == 'jon':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('jon.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            jon = (f' Жанр: боевик, триллер\nСтрана: США, Германия\nРежиссер: Чад Стахелски\nАктеры: Киану Ривз, '
                   f'Донни Йен, Билл Скарсгард, Шамир Андерсон\nРейтинг «Кинопоиска»: 7,6\n'
                   f'Рейтинг IMDb: 7,9\nё\n'
                   f'Продолжение истории о легендарном герое. Джон Уик готовится отомстить Правлению Кланов. Два '
                   f'управляющих отелями «Континенталь» — в Нью-Йорке и Осаке — не могут помочь герою. Но он находит '
                   f'выход из ситуации, которая казалась безвыходной. Те, кто следил за историей главного героя '
                   f'в предыдущих фильмах франшизы, наконец узнают, чем закончится история (хотя авторы и не исключают '
                   f'продолжения) А еще познакомятся с новыми персонажами — незрячим киллером Кейном и загадочным '
                   f'убийцей по прозвищу Никто. Фильм хвалят за красивые локации, зрелищные сцены сражений и '
                   f'атмосферную музыку. В новой части '
                   f'появилось еще больше орудий убийства — нунчаки, мечи и даже пушка со взрывными патронами.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_jon')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='jon_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, jon, reply_markup=markup)

        if call.data == 'krysh':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('krysh.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            krysh = (f' Жанр: боевик, триллер\nСтрана: Великобритания\nРежиссер: Жан-Франсуа Рише\nАктеры: '
                     f'Джерард Батлер, Майк Колтер, Тони Голдуин, Йосон Ань\nРейтинг '
                     f'«Кинопоиска»:7,1\nРейтинг IMDb: 6,5\nЦена: 400р.\nГлавную роль в фильме исполняет Джерард Батлер '
                     f'— он играет пилота Броуди Торранса. Тому удается успешно посадить поврежденный стихией '
                     f'самолет на острове. Вскоре становится известно, что пассажирам грозят местные мятежники: '
                     f'они собираются захватить выживших в заложники. Фильм для любителей боевиков 80-х: персонажи '
                     f'здесь настоящие герои, которые ввязываются в зрелищные схватки с «плохими парнями», '
                     f'только снято все это гораздо красочнее и динамичнее благодаря современным технологиям.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_krysh')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='krysh_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, krysh, reply_markup=markup)

        if call.data == 'kynf':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('kynf.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            kynf = (f' Жанр: комедия\nСтрана: США, Китай\nРежиссер: Ларри Ян\nАктеры: Джеки Чан, Лю Хаоцюнь, Го '
                    f'Цилинь, Джеки У\nРейтинг «Кинопоиска»: 8,1\nРейтинг IMDb: 6,3\nЦена: 600р.\nДжеки Чан — снова '
                    f'герой. Точнее, он играет старого каскадера по имени Лу. Герой защищает своего коня — тоже '
                    f'каскадера — от коллекторов и, так как на дворе XXI век, быстро становится звездой в сети, '
                    f'но, помимо фанатов, у него тут же появляются и враги. Джеки Чан уже не так молод, чтобы делать '
                    f'типичное «каскадерское» кино, как раньше — с трюками и сломанными костями. Поэтому он делает '
                    f'кино… о старом каскадере. Это фильм-рассуждение на тему «Нужно ли сейчас так рисковать здоровьем '
                    f'ради зрелищных сцен, если все можно нарисовать с помощью CGI?».')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_kynf')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='kynf_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, kynf, reply_markup=markup)

        if call.data == 'three':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            three = (f'Жанр: боевик, приключения\nСтрана: Франция\nРежиссер: Мартин Бурбулон\nАктеры: Франсуа Сивиль, '
                     f' Венсан Кассель, Ромен Дюрис, Пио Мармай, Ева Грин\nРейтинг «Кинопоиска»: 7,0\nРейтинг IMDb: 7,1'
                     f' \nЦена: 299р.\nСюжет вам наверняка знаком: Франция, 1627 год, молодой гасконец Д’Артаньян хочет стать мушкетером'
                     f' и для этого отправляется в Париж, где знакомится с Атосом, Портосом и Арамисом, мушкетерами короля.'
                     f' Но новые «Мушкетеры» — новый взгляд на произведение Дюма: здесь Париж больше похож на город тех годов:'
                     f' мрачный и грязный, а не блестящий и яркий. При этом кино не так уж отклоняется от текста книги.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_three')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='three_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, three, reply_markup=markup)

        if call.data == 'translator':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('spn.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            spn = (f'Жанр: боевик, триллер\nСтрана: Великобритания\nРежиссер: Гай Ричи\nАктеры: Джейк Джилленхол, Дар '
                   f'Салим, Джонни Ли Миллер, Александр Людвиг\nРейтинг «Кинопоиска»: 7,9\nРейтинг IMDb: 7,5\nЦена: 440р.\nМарт 2018'
                   f', в Афганистане идет спецоперация по поиску оружия талибов. В ходе нее отряд сержанта армии США '
                   f'Джона Кинли (Джилленхол) попадает в засаду — но Джон выживает благодаря местному переводчику '
                   f'Ахмеду. Теперь Ахмеда и его семью ищут талибы, а Джон должен ему помочь. «Переводчик» — смесь '
                   f'военного фильма, боевика и драмы о дружбе двух мужчин. А еще это нетипичный фильм для Гая Ричи'
                   f' — он очень серьезный, без типичных для режиссера шуток. Картину сравнивают по зрелищности с '
                   f'миссией из культовой игры Call of Duty.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_translator')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='spn_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, spn, reply_markup=markup)

        if call.data == 'gone':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('gone.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            gone = (f'Жанр: комедия, мелодрама\nСтрана: Россия\nРежиссер: Антон Маслов\nАктеры: Ольга Лерман, такса '
                    f'Таисия, Виктор Хориняк, Дмитрий Чеботарев\nРейтинг «Кинопоиска»: 7,8\nРейтинг IMDb: 6,7\nЦена: 250р.\nГлавная '
                    f'героиня — Аня Смолина — остается одна в свой 30-й день рождения. Кажется, это становится '
                    f'последней каплей для героини — и вот она уже едет через всю Россию на велосипеде с таксой в '
                    f'прицепе. Конечная точка путешествия — Магадан, где героиня планирует помириться с мамой. Этот '
                    f'фильм основан на реальных событиях — точнее, на книге «А чего дома сидеть?» российской '
                    f'велопутешественницы Анны Смолиной. «Поехавшая» — легкое и веселое кино, которое в то же время '
                    f'рассказывает о том, как нелегко даются перемены, которые иногда всем нам нужны.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_gone')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='gone_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, gone, reply_markup=markup)

        if call.data == 'book':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('book.jpg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            book = (f'Жанр: мультфильм, семейный\nСтрана: Россия\nРежиссер: Владимир Саков\nАктеры: Юлия Хлынина, '
                    f'Федор Бондарчук, Лидия Чистякова-Ионова, Илья Бледный\nРейтинг «Кинопоиска»: '
                    f'7,8\nРейтинг IMDb: 6,1\nЦена: 300р.\nВедьма Яга — еще не баба — живет с котом-изобретателем и домовыми в '
                    f'избушке на болотах Тридевятого царства. Пока что она только учится колдовать — для этого ей не '
                    f'хватает Книги заклинаний, которую у Яги украли. Зрители увидят Ягу сначала маленькой девочкой, '
                    f'потом — молодой женщиной, и поймут, почему она стала злой ведьмой, '
                    f'какой ее описывают в славянском фольклоре.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_book')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='book_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, book, reply_markup=markup)

        if call.data == 'vovV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('vov.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            vov = (f' Жанр: драма\nСтрана: Россия\nРежиссер: Клим Шипенко\nАктеры: Юлия Пересильд, '
                   f'Милош Бикович, Владимир Машков, Олег Новицкий'
                   f'\nРейтинг «Кинопоиска»: 7,5\nРейтинг IMDb: 6,7\nЦена: 330р.\nВо время выхода в открытый космос, совершая '
                   f'экстренный маневр, '
                   f'космонавт Олег Богданов получает тяжелую травму. Ему может помочь '
                   f'только торакальный хирург — Евгения Беляева, у которой хватает своих проблем на Земле.'
                   f'Это первый в мире фильм, сцены для которого были сняты в космосе — '
                   f'на Международной космической станции. Работа на орбите заняла около двух недель. '
                   f'Критики отмечают отличную игру актрисы Юлии Пересильд, '
                   f'а также визуальную сторону фильма в целом: операторскую работу и постановку тех самых сцен '
                   f'в космосе.')
            b1 = types.InlineKeyboardButton('Купить', callback_data='pay_vov')
            b2 = types.InlineKeyboardButton('Актеры', callback_data='vov_actors1')
            b3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(b1, b2, b3)
            bot.send_message(call.message.chat.id, vov, reply_markup=markup)

        if call.data == 'jonV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('jon.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            jon = (f' Жанр: боевик, триллер\nСтрана: США, Германия\nРежиссер: Чад Стахелски\nАктеры: Киану Ривз, '
                   f'Донни Йен, Билл Скарсгард, Шамир Андерсон\nРейтинг «Кинопоиска»: 7,6\n'
                   f'Рейтинг IMDb: 7,9\nЦена: 540р.'
                   f'Продолжение истории о легендарном герое. Джон Уик готовится отомстить Правлению Кланов. Два '
                   f'управляющих отелями «Континенталь» — в Нью-Йорке и Осаке — не могут помочь герою. Но он находит '
                   f'выход из ситуации, которая казалась безвыходной. Те, кто следил за историей главного героя '
                   f'в предыдущих фильмах франшизы, наконец узнают, чем закончится история (хотя авторы и не исключают '
                   f'продолжения) А еще познакомятся с новыми персонажами — незрячим киллером Кейном и загадочным '
                   f'убийцей по прозвищу Никто. Фильм хвалят за красивые локации, зрелищные сцены сражений и '
                   f'атмосферную музыку. В новой части '
                   f'появилось еще больше орудий убийства — нунчаки, мечи и даже пушка со взрывными патронами.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_jon')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='jon_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, jon, reply_markup=markup)

        if call.data == 'kryshV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('krysh.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            krysh = (f' Жанр: боевик, триллер\nСтрана: Великобритания\nРежиссер: Жан-Франсуа Рише\nАктеры: '
                     f'Джерард Батлер, Майк Колтер, Тони Голдуин, Йосон Ань\nРейтинг '
                     f'«Кинопоиска»:7,1\nРейтинг IMDb: 6,5\nЦена: 400р.Главную роль в фильме исполняет Джерард Батлер '
                     f'— он играет пилота Броуди Торранса. Тому удается успешно посадить поврежденный стихией '
                     f'самолет на острове. Вскоре становится известно, что пассажирам грозят местные мятежники: '
                     f'они собираются захватить выживших в заложники. Фильм для любителей боевиков 80-х: персонажи '
                     f'здесь настоящие герои, которые ввязываются в зрелищные схватки с «плохими парнями», '
                     f'только снято все это гораздо красочнее и динамичнее благодаря современным технологиям.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_krysh')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='krysh_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, krysh, reply_markup=markup)

        if call.data == 'kynfV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('kynf.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            kynf = (f' Жанр: комедия\nСтрана: США, Китай\nРежиссер: Ларри Ян\nАктеры: Джеки Чан, Лю Хаоцюнь, Го '
                    f'Цилинь, Джеки У\nРейтинг «Кинопоиска»: 8,1\nРейтинг IMDb: 6,3\nЦена: 600р.Джеки Чан — снова '
                    f'герой. Точнее, он играет старого каскадера по имени Лу. Герой защищает своего коня — тоже '
                    f'каскадера — от коллекторов и, так как на дворе XXI век, быстро становится звездой в сети, '
                    f'но, помимо фанатов, у него тут же появляются и враги. Джеки Чан уже не так молод, чтобы делать '
                    f'типичное «каскадерское» кино, как раньше — с трюками и сломанными костями. Поэтому он делает '
                    f'кино… о старом каскадере. Это фильм-рассуждение на тему «Нужно ли сейчас так рисковать здоровьем '
                    f'ради зрелищных сцен, если все можно нарисовать с помощью CGI?».')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_kynf')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='kynf_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, kynf, reply_markup=markup)

        if call.data == 'threeV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            three = (
                f'Жанр: боевик, приключения\nСтрана: Франция\nРежиссер: Мартин Бурбулон\nАктеры: Франсуа Сивиль, '
                f' Венсан Кассель, Ромен Дюрис, Пио Мармай, Ева Грин\nРейтинг «Кинопоиска»: 7,0\nРейтинг IMDb: 7,1'
                f' \nЦена: 299р.Сюжет вам наверняка знаком: Франция, 1627 год, молодой гасконец Д’Артаньян хочет стать мушкетером'
                f' и для этого отправляется в Париж, где знакомится с Атосом, Портосом и Арамисом, мушкетерами короля.'
                f' Но новые «Мушкетеры» — новый взгляд на произведение Дюма: здесь Париж больше похож на город тех годов:'
                f' мрачный и грязный, а не блестящий и яркий. При этом кино не так уж отклоняется от текста книги.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_three')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='three_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, three, reply_markup=markup)

        if call.data == 'spnV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('spn.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            spn = (
                f'Жанр: боевик, триллер\nСтрана: Великобритания\nРежиссер: Гай Ричи\nАктеры: Джейк Джилленхол, Дар '
                f'Салим, Джонни Ли Миллер, Александр Людвиг\nРейтинг «Кинопоиска»: 7,9\nРейтинг IMDb: 7,5\nЦена: 440р.Март 2018'
                f', в Афганистане идет спецоперация по поиску оружия талибов. В ходе нее отряд сержанта армии США '
                f'Джона Кинли (Джилленхол) попадает в засаду — но Джон выживает благодаря местному переводчику '
                f'Ахмеду. Теперь Ахмеда и его семью ищут талибы, а Джон должен ему помочь. «Переводчик» — смесь '
                f'военного фильма, боевика и драмы о дружбе двух мужчин. А еще это нетипичный фильм для Гая Ричи'
                f' — он очень серьезный, без типичных для режиссера шуток. Картину сравнивают по зрелищности с '
                f'миссией из культовой игры Call of Duty.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_translator')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='spn_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, spn, reply_markup=markup)

        if call.data == 'goneV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('gone.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            gone = (
                f'Жанр: комедия, мелодрама\nСтрана: Россия\nРежиссер: Антон Маслов\nАктеры: Ольга Лерман, такса '
                f'Таисия, Виктор Хориняк, Дмитрий Чеботарев\nРейтинг «Кинопоиска»: 7,8\nРейтинг IMDb: 6,7\nЦена: 250р.Главная '
                f'героиня — Аня Смолина — остается одна в свой 30-й день рождения. Кажется, это становится '
                f'последней каплей для героини — и вот она уже едет через всю Россию на велосипеде с таксой в '
                f'прицепе. Конечная точка путешествия — Магадан, где героиня планирует помириться с мамой. Этот '
                f'фильм основан на реальных событиях — точнее, на книге «А чего дома сидеть?» российской '
                f'велопутешественницы Анны Смолиной. «Поехавшая» — легкое и веселое кино, которое в то же время '
                f'рассказывает о том, как нелегко даются перемены, которые иногда всем нам нужны.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_gone')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='gone_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, gone, reply_markup=markup)

        if call.data == 'bookV2':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('book.jpg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            book = (f'Жанр: мультфильм, семейный\nСтрана: Россия\nРежиссер: Владимир Саков\nАктеры: Юлия Хлынина, '
                    f'Федор Бондарчук, Лидия Чистякова-Ионова, Илья Бледный\nРейтинг «Кинопоиска»: '
                    f'7,8\nРейтинг IMDb: 6,1\nЦена: 300р.Ведьма Яга — еще не баба — живет с котом-изобретателем и домовыми в '
                    f'избушке на болотах Тридевятого царства. Пока что она только учится колдовать — для этого ей не '
                    f'хватает Книги заклинаний, которую у Яги украли. Зрители увидят Ягу сначала маленькой девочкой, '
                    f'потом — молодой женщиной, и поймут, почему она стала злой ведьмой, '
                    f'какой ее описывают в славянском фольклоре.')
            c1 = types.InlineKeyboardButton('Купить', callback_data='pay_book')
            c2 = types.InlineKeyboardButton('Актеры', callback_data='book_actors1')
            c3 = types.InlineKeyboardButton('Назад', callback_data='mainMen')
            markup.add(c1, c2, c3)
            bot.send_message(call.message.chat.id, book, reply_markup=markup)

        if call.data == 'vov_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('actor1_vov.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='vov_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='vovV2')
            markup.add(button3)
            bob1 = (f'Юлия Пересильд\nКарьера: Актриса\nРост: 1.68 м\nДата рождения: 5 сентября, '
                    f'1984 • Дева • 39 лет\nМесто рождения: Псков, СССР\nЖанры: Драма, мелодрама, комедия\nВсего фильмов: 86, 2003 — 2025')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "vov_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_vov.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='vov_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='vov_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='vovV2')
            markup.add(button3)
            bob2 = (f'Милош Бикович\nКарьера: Актер, Продюсер, Режиссер, Актер дубляжа\nРост: 1.88 м\nДата рождения: '
                    f'13 января, 1988 • Козерог • 35 лет\nМесто рождения: Белград, Югославия\nЖанры: Драма, комедия, мелодрама\nВсего фильмов: 59, 2004 — 2024')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "vov_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_vov.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='vov_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='vov_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='vovV2')
            markup.add(button3)
            bob2 = (
                f'Владимир Машков\nКарьера: Актер, Режиссер, Продюсер, Сценарист, Актер дубляжа\nРост: 1.78 м\nДата рождения: 27 ноября, 1963 • '
                f'Стрелец • 59 лет\nМесто рождения: Тула, СССР\nЖанры: Драма, триллер, комедия\nВсего фильмов: 70, 1984 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "vov_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_vov.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='vov_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='vovV2')
            markup.add(button3)
            bob2 = (
                f'Олег Новицкий\nКарьера: Актер\nДата рождения: 12 октября, 1971 • Весы • 51 год\nМесто рождения: Червень, '
                f'Минская область, СССР\nЖанры: Документальный, драма\nВсего фильмов: 6, 2017 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'jon_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('actor1_jon.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='jon_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='jonV2')
            markup.add(button3)
            bob1 = (
                f'Киану Ривз\nКарьера: Актер, Продюсер, Сценарист, Режиссер\nРост: 1.86 м\nДата рождения: 2 сентября, 1964 • '
                f'Дева • 59 лет\nМесто рождения: Бейрут, Ливан\nЖанры: Драма, комедия, боевик\nВсего фильмов: 251, 1981 — 2024')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "jon_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_jon.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='jon_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='jon_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='jonV2')
            markup.add(button3)
            bob2 = (
                f'Донни Йен\nКарьера: Актер, Продюсер, Режиссер, Сценарист, Монтажер\nРост: 1.73 м\nДата рождения: 27 июля, 1963 • Лев • '
                f'60 лет\nМесто рождения: Гуанчжоу, Китай\nЖанры: Боевик, драма, комедия\nВсего фильмов: 97, 1984 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "jon_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_jon.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='jon_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='jon_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='jonV2')
            markup.add(button3)
            bob2 = (
                f'Билл Скарсгард\nКарьера: Актер, Продюсер, Режиссер, Сценарист\nРост: 1.92 м\nДата рождения: 9 августа, 1990 • Лев • '
                f'33 года\nМесто рождения: Стокгольм, Швеция\nЖанры: Драма, триллер, боевик\nВсего фильмов: 58, 2000 — 2024')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "jon_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_jon.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='jon_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='jonV2')
            markup.add(button3)
            bob2 = (
                f'Шамир Андерсон\nКарьера: Актер, Продюсер, Сценарист\nРост: 1.88 м\nДата рождения: 6 мая, 1991 • Телец • 32 года\nМесто '
                f'рождения: Торонто, Онтарио, Канада\nЖанры: Драма, триллер, боевик\nВсего фильмов: 53, 2001 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'krysh_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor1_krysh.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='krysh_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kryshV2')
            markup.add(button3)
            bob1 = (
                f'Джерард Батлер\nКарьера: Актер, Продюсер\nРост: 1.88 м\nДата рождения: 13 ноября, 1969 • Скорпион • 53 года\n'
                f'Место рождения: Пейсли, Шотландия, Великобритания\nЖанры: Драма, боевик, триллер\nВсего фильмов: 147, 1997 — 2025')

            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "krysh_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_krysh.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='krysh_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='krysh_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kryshV2')
            markup.add(button3)
            bob2 = (
                f'Майк Колтер\nКарьера: Актер, Продюсер\nРост: 1.91 м\nДата рождения: 26 августа, 1976 • Дева • 47 лет\n'
                f'Место рождения: Колумбия, Южная Каролина, США\nЖанры: Драма, триллер, криминал\nВсего фильмов: 76, 1994 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "krysh_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_krysh.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='krysh_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='krysh_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kryshV2')
            markup.add(button3)
            bob2 = (
                f'Тони Голдуин\nКарьера: Актер, Режиссер, Продюсер, Сценарист\nРост: 1.88 м\nДата рождения: 20 мая, 1960 • Телец • 63 года\n'
                f'Место рождения: Лос-Анджелес, Калифорния, США\nЖанры: Драма, триллер, комедия\nВсего фильмов: 142, 1982 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "krysh_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_krysh.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='krysh_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kryshV2')
            markup.add(button3)
            bob2 = (
                f'Йосон Ань\nКарьера: Актер, Продюсер, Режиссер, Сценарист, Монтажер\nДата рождения: 23 июня, 1992 • Рак • 31 год\n'
                f'Место рождения: Макао\nЖанры: Триллер, драма, боевик\nВсего фильмов: 23, 2013 — 2022')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'kynf_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor1_kynf.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='kynf_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kynfV2')
            markup.add(button3)
            bob1 = (
                f'Джеки Чан\nКарьера: Актер, Продюсер, Режиссер, Сценарист, Оператор, Художник\nРост: 1.74 м\nДата рождения: 7 апреля, 1954 • Овен • 69 лет\n'
                f'Место рождения: Гонконг\nЖанры: Боевик, комедия, драма\nВсего фильмов: 309, 1962 — 2024')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "kynf_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_kynf.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='kynf_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='kynf_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kynfV2')
            markup.add(button3)
            bob2 = (f'Лю Хаоцюнь\nКарьера: Актриса\nДата рождения: 20 мая, 2000 • Телец • 23 года\n'
                    f'Место рождения: Чанчунь, Гирин, Китай\nЖанры: Драма, история, боевик\nВсего фильмов: 7, 2019 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "kynf_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_kynf.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='kynf_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='kynf_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kynfV2')
            markup.add(button3)
            bob2 = (f'Го Цилинь\nКарьера: Актер\nДата рождения: 8 февраля, 1996 • Водолей • 27 лет\n'
                    f'Место рождения: Тяньцзинь, Китай\nЖанры: Драма, комедия, боевик\nВсего фильмов: 6, 2018 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "kynf_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_kynf.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='kynf_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='kynfV2')
            markup.add(button3)
            bob2 = (
                f'Джеки У\nКарьера: Актер, Продюсер, Режиссер, Сценарист\nРост: 1.75 м\nДата рождения: 3 апреля, 1974 • Овен • 49 лет\n'
                f'Место рождения: Пекин, Китай\nЖанры: Боевик, драма, комедия\nВсего фильмов: 53, 1995 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'three_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor1_three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='three_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='threeV2')
            markup.add(button3)
            bob1 = (
                f'Франсуа Сивиль\nКарьера: Актер\nРост: 1.75 м\nДата рождения: 29 января, 1990 • Водолей • 33 года\n'
                f'Место рождения: Париж, Франция\nЖанры: Драма, комедия, мелодрама\nВсего фильмов: 57, 1997 — 2023')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "three_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='three_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='three_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='threeV2')
            markup.add(button3)
            bob2 = (
                f'Венсан Кассель\nКарьера: Актер, Продюсер, Режиссер, Сценарист\nРост: 1.87 м\nДата рождения: 23 ноября, 1966 • Стрелец • 56 лет\n'
                f'Место рождения: Париж, Франция\nЖанры: Драма, триллер, комедия\nВсего фильмов: 138, 1988 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "three_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='three_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='three_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='threeV2')
            markup.add(button3)
            bob2 = (f'Ромен Дюрис\nКарьера: Актер\nРост: 1.79 м\nДата рождения: 28 мая, 1974 • Близнецы • 49 лет\n'
                    f'Место рождения: Париж, Франция\nЖанры: Драма, комедия, мелодрама\nВсего фильмов: 84, 1993 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "three_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='three_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='threeV2')
            markup.add(button3)
            bob2 = (f'Ева Грин\nКарьера: Актриса, Продюсер\nРост: 1.7 м\nДата рождения: 6 июля, 1980 • Рак • 43 года\n'
                    f'Место рождения: Париж, Франция\nЖанры: Драма, триллер, приключения\nВсего фильмов: 77, 2001 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'spn_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor1_spn.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='spn_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='spnV2')
            markup.add(button3)
            bob1 = (
                f'Джейк Джилленхол\nКарьера: Актер, Продюсер\nРост: 1.81 м\nДата рождения: 19 декабря, 1980 • Стрелец • 42 года\n'
                f'Место рождения: Лос-Анджелес, Калифорния, США\nЖанры: Драма, триллер, комедия\nВсего фильмов: 192, 1991 — 2022')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "spn_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_three.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='spn_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='spn_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='spnV2')
            markup.add(button3)
            bob2 = (
                f'Дар Салим\nКарьера: Актер, Продюсер\nРост: 1.8 м\nДата рождения: 18 августа, 1977 • Лев • 46 лет\n'
                f'Место рождения: Багдад, Ирак\nЖанры: Драма, триллер, криминал\nВсего фильмов: 57, 2006 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "spn_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_spn.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='spn_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='spn_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='spnV2')
            markup.add(button3)
            bob2 = (
                f'Джонни Ли Миллер\nКарьера: Актер, Режиссер, Продюсер\nРост: 1.77 м\nДата рождения: 15 ноября, 1972 • Скорпион • 50 лет\n'
                f'Место рождения: Кингстон-на-Темзе, Лондон, Англия, Великобритания\nЖанры: Драма, криминал, триллер\nВсего фильмов: 84, 1979 — 2022')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "spn_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_spn.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='spn_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='spnV2')
            markup.add(button3)
            bob2 = (
                f'Александр Людвиг\nКарьера: Актер, Продюсер\nРост: 1.89 м\nДата рождения: 7 мая, 1992 • Телец • 31 год\n'
                f'Место рождения: Ванкувер, Британская Колумбия, Канада\nЖанры: Триллер, драма, комедия\nВсего фильмов: 55, 2000 — 2024')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'gone_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor1_gone.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='gone_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='goneV2')
            markup.add(button3)
            bob1 = (f'Ольга Лерман\nКарьера: Актриса\nДата рождения: 25 марта, 1988 • Овен • 35 лет\n'
                    f'Место рождения: Баку, СССР\nЖанры: Драма, мелодрама, комедия\nВсего фильмов: 37, 2009 — 2023')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "gone_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_gone.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='gone_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='gone_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='goneV2')
            markup.add(button3)
            bob2 = (
                f'Виктор Хориняк\nКарьера: Актер, Актер дубляжа\nРост: 1.84 м\nДата рождения: 22 марта, 1990 • Овен • 33 года\n'
                f'Место рождения: Минусинск, СССР\nЖанры: Комедия, драма, приключения\nВсего фильмов: 48, 2008 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "gone_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_gone.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='gone_actors2')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='goneV2')
            markup.add(button3)
            bob2 = (
                f'Дмитрий Чеботарев\nКарьера: Актер\nРост: 1.82 м\nДата рождения: 15 декабря, 1986 • Стрелец • 36 лет\n'
                f'Место рождения: Хабаровск, СССР\nЖанры: Драма, комедия, детектив\nВсего фильмов: 52, 2013 — 2024')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == 'book_actors1':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup(row_width=1)
            file = open('actor1_book.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='book_actors2')
            markup.add(button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='bookV2')
            markup.add(button3)
            bob1 = (f'Юлия Хлынина\nКарьера: Актриса, Актриса дубляжа\nРост: 1.69 м\nДата рождения: 11 января, 1992 • Козерог • 31 год\n'
                    f'Место рождения: Москва, Россия\nЖанры: Драма, комедия, мелодрама\nВсего фильмов: 42, 2010 — 2023')
            bot.send_message(call.message.chat.id, bob1, reply_markup=markup)

        if call.data == "book_actors2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor2_book.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='book_actors3')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='book_actors1')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='bookV2')
            markup.add(button3)
            bob2 = (f'Федор Бондарчук\nКарьера: Продюсер, Актер, Режиссер, Актер дубляжа, Сценарист\nРост: 1.82 м\nДата рождения: 9 мая, 1967 • Телец • 56 лет\n'
                    f'Место рождения: Москва, СССР\nЖанры: Драма, комедия, мелодрама\nВсего фильмов: 240, 1986 — 2024')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "book_actors3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor3_book.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button2 = types.InlineKeyboardButton("Следующий", callback_data='book_actors4')
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='book_actors2')
            markup.add(button1, button2)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='bookV2')
            markup.add(button3)
            bob2 = (f'Лидия Чистякова-Ионова\nКарьера: Актриса\nДата рождения: 8 мая, 2007 • Телец • 16 лет\nЖанры: '
                    f'Мультфильм, приключения, семейный\nВсего фильмов: 2, 2015 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)

        if call.data == "book_actors4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
            markup = types.InlineKeyboardMarkup()
            file = open('actor4_book.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, file, reply_markup=markup)
            button1 = types.InlineKeyboardButton("Предыдущий", callback_data='book_actors3')
            markup.add(button1)
            button3 = types.InlineKeyboardButton("К фильму", callback_data='bookV2')
            markup.add(button3)
            bob2 = (f'Илья Бледный\nКарьера: Актер дубляжа, Актер\nРост: 1.85 м\nДата рождения: 9 июня, 1976 • Близнецы • 47 лет\n'
                    f'Место рождения: Оренбург, СССР\nЖанры: Драма, комедия, мелодрама\nВсего фильмов: 499, 1976 — 2023')
            bot.send_message(call.message.chat.id, bob2, reply_markup=markup)


bot.polling(none_stop=True)
