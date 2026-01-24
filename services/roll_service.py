from requests.auth import HTTPBasicAuth


def post_roll_dice(api_client):
    return api_client.post(f"/rollDice", payload=None, headers=None, auth=None)


def get_roll_dice(api_client):
    return api_client.get(f"/rollDice")


def post_roll_die(api_client, die_id):
    return api_client.post(f"/rollDie/{die_id}", payload=None, headers=None, auth=None)


def delete_roll_die(api_client):
    return api_client.delete(f"/rollDie/1")


def get_dice(api_client):
    return api_client.get(f"/dice")


def delete_dice(api_client):
    return api_client.delete(f"/dice")


def get_dice_withid(api_client):
    return api_client.get(f"/dice/1")


def get_die(api_client, die_id, Accept_Header=None):
    headers = {"Accept": Accept_Header}
    return api_client.get(f"/die/{die_id}", headers)


def delete_die(api_client):
    return api_client.delete(f"/die/1")


def get_isyahtzee(api_client):
    return api_client.get(f"/isYahtzee")


def delete_isyahtzee(api_client):
    return api_client.delete(f"/isYahtzee")


def put_dievalue(api_client, die_id, value):
    return api_client.put(f"/die", {"Id": die_id, "value": value}, auth=HTTPBasicAuth("admin", "snakeeyes"))


def put_dievalue_withoutautinput(api_client, die_id, value, auth=None):
    return api_client.put(f"/die", {"Id": die_id, "value": value}, auth)


def put_dievalue_wronguser(api_client, die_id, value, auth=None):
    return api_client.put(f"/die", {"Id": die_id, "value": value}, auth=HTTPBasicAuth("admin1", "snakeeyes"))


def put_dievalue_wrongpassword(api_client, die_id, value, auth=None):
    return api_client.put(f"/die", {"Id": die_id, "value": value}, auth=HTTPBasicAuth("admin", "snakeeyesz"))


def put_dievalue_wronguser_password(api_client, die_id, value, auth=None):
    return api_client.put(f"/die", {"Id": die_id, "value": value}, auth=HTTPBasicAuth("admin1", "snakeeyesz"))


def delete_dievalue(api_client, die_id, value, auth=None):
    return api_client.delete(f"/die", auth=HTTPBasicAuth("admin", "snakeeyes"))
