import json


def test_adicionar_usuario(test_app, teste_database):
    client = test_app.test_client()
    resp = client.post(
        '/usuarios',
        data=json.dumps({
            'usuario': 'mceolin',
            'email': 'mceolin@unidavi.edu.br'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'mceolin@unidavi.edu.br foi adicionado com sucesso!' in data['mensagem']