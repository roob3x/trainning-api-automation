Feature: Consulta Restricao

@sanity @integration @restricoes
Scenario Outline: Obter a lista de cpfs restritos
    Given desejo verificar restricao para o cpf <cpf>
    Then valido que é retornado status code 200
    And valido que é retornado a lista corretamente

Examples:
    | cpf           |
    | "60094146012" |
    | "97093236014" |

@integration @sem_restricoes
Scenario: Verifico cpfs sem restricao
    Given desejo verificar restricao para o cpf "321.015.075-44"
    Then valido que é retornado status code 204