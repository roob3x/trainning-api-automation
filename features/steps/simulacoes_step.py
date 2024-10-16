from services.simulacoes_api import *
from services.fac import *
from hamcrest import assert_that, is_

@given('que preparo os dados da simulacao')
def prepare_simulation(context):
    context.payload = get_fixtures('post_simulacoes')['V1_SIMULACOES']
    for row in context.table:
        context.payload['nome'] = row['nome']
        if row['cpf']  == 'None':
            del context.payload["cpf"]
        elif row['cpf'] == 'dinamico':
            context.payload['cpf'] = generate_personal_id_br()
        else:
            context.payload['cpf'] = context.payload['cpf']
        context.payload['email'] = row['email']
        context.payload['parcelas'] = row['parcelas']
        context.payload['seguro'] = row['seguro']


@when('submeto a simulacao')
def simulation_submit(context):
    url = context.config.userdata['base_url_local']+ context.endpoint['simulacoes_endpoint']
    context.response = post_simulacoes(url, context.payload)

@given('que eu cadastro uma simulacao')
def register_simulation(context):
    prepare_simulation(context)
    simulation_submit(context)
    validate_status_code(context, 201)


@when('altero os dados de uma simulacao ja cadastrada')
def setup_data_simulation(context):
    context.payload_put = get_fixtures('post_simulacoes')['V1_SIMULACOES']
    for row in context.table:
        context.payload_put['nome'] = row['nome']
        if row['cpf']  == 'None':
            del context.payload_put["cpf"]
        elif row['cpf'] == 'dinamico':
            context.payload_put['cpf'] = generate_personal_id_br()
        else:
            context.payload_put['cpf'] = row['cpf']
        context.payload_put['email'] = row['email']
        context.payload_put['parcelas'] = row['parcelas']
        context.payload_put['seguro'] = row['seguro']

@when('submeto simulacao atualizada')
def put_simulation(context):
    url = context.config.userdata['base_url_local']+ context.endpoint['simulacoes_endpoint'] + str(context.payload['cpf'])
    context.response = put_simulacoes(url, context.payload_put)


@then('valido que é retornando mensagem de erro de cpf nao encontrado')
def valite_msg_erro_of_cpf(context):
    get_msg_payload = load_schema('put_simulacoes')['CPF_NOT_FOUND']
    get_expected_response = str(get_msg_payload).replace("VALUECPF", context.payload_put['cpf'])
    get_msg_from_response = get_message_from_response(get_response(context.response), 'mensagem')
    assert_that(get_msg_from_response, get_expected_response)


@when('submeto simulacao alterada')
def put_simulation(context):
    url = context.config.userdata['base_url_local']+ context.endpoint['simulacoes_endpoint'] + str(context.payload_put['cpf'])
    context.response = put_simulacoes(url, context.payload_put)


@when('consulto a simulacao previamente cadastrada')
def get_simulation_sucessful(context):
    url = context.config.userdata['base_url_local'] + context.endpoint['simulacoes_endpoint'] + str(context.payload['cpf'])
    context.response = get_simulacao(url)

@when('consulto uma simulacao para cpf inexistente')
def get_simulation_unexist_cpf(context):
    context.payload = get_fixtures('post_simulacoes')['V1_SIMULACOES']
    context.payload['cpf'] = generate_personal_id_br()
    get_simulation_sucessful(context)


@then('valido na consulta de inexistente, retornando mensagem de erro de cpf nao encontrado')
def get_simulation_valite_msg_erro_of_cpf(context):
    get_msg_payload = load_schema('get_simulacoes')['CPF_NOT_FOUND']
    get_expected_response = str(get_msg_payload).replace("VALUECPF", context.payload['cpf'])
    get_msg_from_response = get_message_from_response(get_response(context.response), 'mensagem')
    assert_that(get_msg_from_response, is_(get_expected_response))

@when('submeto requisicao para deletar a simulacao')
def delete_simulation(context):
    url = context.config.userdata['base_url_local'] + context.endpoint['simulacoes_endpoint'] + str(context.response.json()['id'])
    context.response = del_simulacao(url)