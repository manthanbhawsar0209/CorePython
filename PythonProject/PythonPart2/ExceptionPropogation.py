def son():
    raise Exception("Money is lost")

def mom():
    son()

def dad():
    try:
        mom()
    except Exception as e:
        print(e, "Money given")

dad()
