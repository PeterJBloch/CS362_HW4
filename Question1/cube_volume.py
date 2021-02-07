def cube_volume(length, width, height):
    try:
        int(length)
        int(width)
        int(height)
    except:
        raise(TypeError)
    return length*width*height