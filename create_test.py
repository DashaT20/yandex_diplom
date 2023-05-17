import sender_stand_request

def get_track():
    return sender_stand_request.post_new_order().json()["track"]

def test_get_orders_track():
    id_track = get_track()
    get_orders_track_response = sender_stand_request.get_orders_track(id_track)

    assert get_orders_track_response.status_code == 200

