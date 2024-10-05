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
            | nome  | cpf  | email                   | valor | parcelas | seguro |
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


    @integration @put_simulacoes @put_simulacoes_sucessfull
    Scenario: Verifique que é possivel alterar simulacao previamente cadastrada
        Given que eu cadastro uma simulacao
            | nome  | cpf      | email                   | valor | parcelas | seguro |
            | Chico | dinamico | chicotestador@gmail.com | 1200  | 3        | False  |
        When altero os dados de uma simulacao ja cadastrada
            | nome  | cpf      | email                    | valor | parcelas | seguro|
            | Ana | dinamico   | aninha@gmail.com         | 25000 | 5        | True  |
        And submeto simulacao atualizada
        Then valido que a atualizacao da simulacao retornou status code 200


