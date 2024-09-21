Feature: Restricoes CPF

@sanity @e2e @restricoes
Scenario Outline: Obter a lista de cpfs restritos
    Given desejo verificar restricao para o cpf <cpf>
    Then valido que é retornado status code 200
    #And valido que é retornado a lista corretamente

Examples:
    | cpf           |
    | "60094146012" |