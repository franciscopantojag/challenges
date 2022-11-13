def verify_type(cl, obj):
    if not isinstance(obj, cl):
        raise Exception(f'Invalid input: {obj}')
