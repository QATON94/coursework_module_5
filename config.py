from configparser import ConfigParser

HH_URL = 'https://api.hh.ru/vacancies'

db_name = 'hh'

company_list = [{'employer_id': '68587'}, {'employer_id': '9498120'}, {'employer_id': '3529'}, {'employer_id': '67611'},
                {'employer_id': '5441625'}, {'employer_id': '78638'}, {'employer_id': '5744540'},
                {'employer_id': '2730053'}, {'employer_id': '1008541'}, {'employer_id': '9623098'}]

db_company = [{'company_id': '68587', 'company_name': 'ОЭЗ «АЛАБУГА»'},
              {'company_id': '9498120', 'company_name': 'Яндекс Команда для бизнеса'},
              {'company_id': '3529', 'company_name': 'СБЕР'}, {'company_id': '67611', 'company_name': 'Тензор'},
              {'company_id': '5441625', 'company_name': 'ООО Инновационный центр КАМАЗ'},
              {'company_id': '78638', 'company_name': 'Тинькофф'},
              {'company_id': '5744540', 'company_name': 'ООО Онлайн-школа Фоксфорд'},
              {'company_id': '2730053', 'company_name': 'ООО Парус электро'},
              {'company_id': '1008541', 'company_name': 'МФТИ'},
              {'company_id': '9623098', 'company_name': 'ООО Бриф'}, ]


def config(filename='database.ini', section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
