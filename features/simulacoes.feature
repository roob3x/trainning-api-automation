Feature: Simulacoes de Credito

@integration @post_simulacoes @simulacao_valida
Scenario: Valido que é possivel realizar simulacao com dados validos
    Given que preparo os dados da simulacao
            | nome  | cpf      | email                   | valor | parcelas | seguro |
            | Chico | dinamico | chicotestador@gmail.com  | 1200  | 3        | False  |
    When submeto a simulacao
    Then valido que a simulacao retornou status code 201

@integration @post_simulacoes @alternative_scenarios @cpf_incorreto
Scenario: Verifico que nao é possivel criar simulacao cpf fora do padrao
        Given que preparo os dados da simulacao
            | nome  | cpf            | email                   | valor | parcelas | seguro |
            | Chico | None | chicotestador@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que a simulacao retornou status code 400

@integration @post_simulacoes @duplicated_personal_id @issue-181
Scenario: Verifico que nao é possivel fazer simulacao para o mesmo cpf duas vezes
        Given que preparo os dados da simulacao
            | nome  | cpf            | email                   | valor | parcelas | seguro |
            | Chico | 321.015.075-00 | chicotestador@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que a simulacao retornou status code 201
        Given que preparo os dados da simulacao
            | nome  | cpf            | email                   | valor | parcelas | seguro |
            | Chico | 321.015.075-00 | chicotestador@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que a simulacao retornou status code 409


