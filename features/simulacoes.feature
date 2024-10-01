Feature: Simulacoes de Credito

@integration @simulacoes
Scenario: Valido que é possivel realizar simulacao com dados validos
    Given que preparo os dados da simulacao
            | nome   | cpf         | email                   | valor | parcelas | seguro |
            | Chico | 32101507500 | chicotestador@gmail.com  | 1200  | 3        | False  |
    When submeto a simulacao
    Then valido que a simulacao retornou status code 201

@integration @simulacoes @alternative_scenarios @cpf_incorreto
Scenario: Verifico que nao é possivel criar simulacao cpf fora do padrao
        Given que preparo os dados da simulacao
            | nome  | cpf            | email                   | valor | parcelas | seguro |
            | Chico | None | chicotestador@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que a simulacao retornou status code 400
