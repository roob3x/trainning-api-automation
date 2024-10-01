from services.simulacoes_api import *
from services.fac import *
from hamcrest import assert_that, is_

@given('que preparo os dados da simulacao')
def step_impl(context):
    context.payload = get_fixtures('post_restricoes')['V1_SIMULACOES']
    for row in context.table:
        context.payload['nome'] = row['nome']
        context.payload['cpf'] = row['cpf']
        if context.payload['cpf']  == 'None':
            del context.payload["cpf"]
        context.payload['email'] = row['email']
        context.payload['parcelas'] = row['parcelas']
        context.payload['seguro'] = row['seguro']

        print(context.payload)

@when('submeto a simulacao')
def step_impl(context):
    url = context.config.userdata['base_url_local']+ context.endpoint['simulacoes_endpoint']
    context.post_restricoes_response = post_simulacoes(url, context.payload)

@then('valido que a simulacao retornou status code {status_code}')
def step_impl(context, status_code):
    assert_that(context.post_restricoes_response.status_code, is_(int(status_code)))