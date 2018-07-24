def prefix_dict(prefix, **kwargs):
    print(kwargs)
    return {
        prefix + key: value for key, value in kwargs.items()
    }


prefix_dict('super_', grass=True, fly=False, human=True)
# {'super_grass': True, 'super_fly': False, 'super_human': True}


prefix_dict(prefix='super_', grass=True, fly=False, human=True)
# {'super_grass': True, 'super_fly': False, 'super_human': True}


prefix_dict('super_')
# {}

