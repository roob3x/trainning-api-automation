from services.restricoes_api import get_restricoes
from hamcrest import assert_that, is_

@given('desejo verificar restricao para o cpf "{cpf}"')
def step_impl(context, cpf):
    url = context.config.userdata['base_url_local'] + 'api/v1/restricoes/'+cpf
    context.get_restricoes_response = get_restricoes(url)

@then('valido que é retornado status code {status_code}')
def step_impl(context, status_code):
    assert_that(context.get_restricoes_response.status_code, is_(int(status_code)))