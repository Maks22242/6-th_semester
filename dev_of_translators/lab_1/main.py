def get_table_of_service_words ():
    dict = {}
    dict["if"] = 1
    dict["print"] = 2
    dict["else"] = 3
    dict["c"] = 4
    dict["ifelse"] = 5
    dict["for"] = 6
    dict ["in"] = 7
    dict["while"] = 8
    dict["repeat"] = 9
    dict["sum"] = 10
    dict["len","length"] = 11
    dict["min"] = 12
    dict["max"] = 13
    dict["prod"] = 14
    dict["sort"] = 15
    dict["scan"] = 16


def get_table_of_operations():
    dict = {}
    dict["="] = 1
    dict["<-"] = 2
    dict["-"] = 3
    dict["+"] = 4
    dict["*"] = 5
    dict["/"] = 6
    dict["<"] = 7
    dict[">"] = 8
    dict["=="] = 9
    dict["!="] = 10
    dict["<="] = 11
    dict[">="] = 12
    dict["{"] = 13
    dict["}"] = 14


def get_table_of_separators():
    dict = []
    dict[","] = 1
    dict["("] = 2
    dict[")"] = 3
    dict[" "] = 4
    dict["\\n"] = 5


if __name__ == '__main__':
    table_a = get_table_of_service_words()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
