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

def get_die(api_client,die_id):
    return api_client.get(f"/die/{die_id}")

def delete_die(api_client):
    return api_client.delete(f"/die/1")