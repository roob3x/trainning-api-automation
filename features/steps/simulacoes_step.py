from services.simulacoes_api import *
from services.fac import *
from hamcrest import assert_that, is_

@given('que preparo os dados da simulacao')
def prepare_simulation(context):
    context.payload = get_fixtures('post_restricoes')['V1_SIMULACOES']
    for row in context.table:
        context.payload['nome'] = row['nome']
        if row['cpf']  == 'None':
            del context.payload["cpf"]
        elif row['cpf'] == 'dinamico':
            context.payload['cpf'] = generate_personal_id_br()
        context.payload['email'] = row['email']
        context.payload['parcelas'] = row['parcelas']
        context.payload['seguro'] = row['seguro']


@when('submeto a simulacao')
def simulation_submit(context):
    url = context.config.userdata['base_url_local']+ context.endpoint['simulacoes_endpoint']
    context.post_restricoes_response = post_simulacoes(url, context.payload)

@then('valido que a simulacao retornou status code {status_code}')
def validate_status_code(context, status_code):
    assert_that(context.post_restricoes_response.status_code, is_(int(status_code)))


@given('que eu cadastro uma simulacao')
def register_simulation(context):
    prepare_simulation(context)
    simulation_submit(context)
    validate_status_code(context, 201)


@when('altero os dados de uma simulacao ja cadastrada')
def setup_data_simulation(context):
    context.payload = get_fixtures('post_restricoes')['V1_SIMULACOES']
    for row in context.table:
        context.payload['nome'] = row['nome']
        if row['cpf']  == 'None':
            del context.payload["cpf"]
        elif row['cpf'] == 'dinamico':
            context.payload['cpf'] = generate_personal_id_br()
        context.payload['email'] = row['email']
        context.payload['parcelas'] = row['parcelas']
        context.payload['seguro'] = row['seguro']
    print(context.payload['cpf'])

@when('submeto simulacao atualizada')
def put_simulation(context):
    url = context.config.userdata['base_url_local']+ context.endpoint['simulacoes_endpoint'] + context.post_restricoes_response.json()['cpf']
    context.put_simulation_response = put_simulacoes(url, context.payload)


@then('valido que a atualizacao da simulacao retornou status code {status_code}')
def validate_put_simulacoes_status_code(context, status_code):
    assert_that(context.put_simulation_response.status_code, is_(int(status_code)))