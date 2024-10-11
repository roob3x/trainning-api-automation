Feature: Simulacoes de Credito

@integration @post_simulacoes @smoke
Scenario: Valido que é possivel realizar simulacao com dados validos
    Given que preparo os dados da simulacao
            | nome  | cpf      | email                   | valor | parcelas | seguro |
            | Chico | dinamico | chicotestador@gmail.com  | 1200  | 3        | False  |
    When submeto a simulacao
    Then valido que é retornado status code 201

@integration @post_simulacoes @alternative_scenarios @cpf_incorreto
Scenario: Verifico que nao é possivel criar simulacao cpf fora do padrao
        Given que preparo os dados da simulacao
            | nome  | cpf  | email                   | valor | parcelas | seguro |
            | Chico | None | chicotestador@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que é retornado status code 400

@integration @post_simulacoes @duplicated_personal_id @issue-181
Scenario: Verifico que nao é possivel fazer simulacao para o mesmo cpf duas vezes
        Given que preparo os dados da simulacao
            | nome  | cpf      | email                   | valor | parcelas | seguro |
            | Chico | dinamico | chicotestador@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que é retornado status code 201
        Given que preparo os dados da simulacao
            | nome  | cpf  | email         | valor | parcelas | seguro |
            | Ana   | same | ana@gmail.com | 1200  | 3        | False  |
        When submeto a simulacao
        Then valido que é retornado status code 409


    @integration @put_simulacoes @smoke
    Scenario: Verifique que é possivel alterar simulacao previamente cadastrada
        Given que eu cadastro uma simulacao
            | nome  | cpf      | email                   | valor | parcelas | seguro |
            | Chico | dinamico | chicotestador@gmail.com | 1200  | 3        | False  |
        When altero os dados de uma simulacao ja cadastrada
            | nome  | cpf      | email                    | valor | parcelas | seguro|
            | Ana   | dinamico   | aninha@gmail.com       | 25000 | 5        | True  |
        And submeto simulacao atualizada
        Then valido que é retornado status code 200
    
    @integration @put_simulacoes @put_simulacoes_alternative
    Scenario: Verifique que é retornado erro ao tentar alterar proposta com cpf inexistente
        When altero os dados de uma simulacao ja cadastrada
            | nome        | cpf         | email                | valor | parcelas | seguro |
            | Assulamita  | 01350081663 | assulamita@gmail.com | 40000 | 10       | True |
        And submeto simulacao alterada
        Then valido que é retornado status code 404
        And valido que é retornando mensagem de erro de cpf nao encontrado
    
    @integration @get_simulacoes @smoke
    Scenario: Consulta simulacoes pelo CPF
        Given que eu cadastro uma simulacao
            | nome  | cpf      | email            | valor | parcelas | seguro |
            | Maria | dinamico | mariav@gmail.com | 2500  | 10       | True   |
        When consulto a simulacao previamente cadastrada
        Then valido que é retornado status code 200
    

    @integration @get_simulacoes @unexist_cpf
    Scenario: Valido critica para buscar simulacao para cpf nao cadastrado
        When consulto uma simulacao para cpf inexistente
        Then valido que é retornado status code 404
        And valido na consulta de inexistente, retornando mensagem de erro de cpf nao encontrado


