from services.restricoes_api import *
from services.fac import *
from hamcrest import assert_that, is_

@given('desejo verificar restricao para o cpf "{cpf}"')
def step_impl(context, cpf):
    context.cpf = cpf
    url = context.config.userdata['base_url_local'] + context.endpoint['restricoes_endpoint']+cpf
    context.get_restricoes_response = get_restricoes(url)

@then('valido que é retornado status code {status_code}')
def step_impl(context, status_code):
    assert_that(context.get_restricoes_response.status_code, is_(int(status_code)))

@then('valido que é retornado a lista corretamente')
def step_impl(context):
    get_msg_payload = load_schema('restricoes')['SUCCESS_MSG']
    restrict_payload = str(get_msg_payload).replace("VALUECPF", context.cpf)
    assert_that(context.get_restricoes_response.json()['mensagem'], restrict_payload)