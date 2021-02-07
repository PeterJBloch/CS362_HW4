def name(firstname,lastname):
    if firstname == "" or lastname == "":
        raise(ValueError)
    try:
        int(firstname)
        raise(TypeError)
    except:
        pass
    try:
        int(lastname)
        raise(TypeError)
    except:
        pass

    return firstname + " " + lastname