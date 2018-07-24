def make_prefix_dict(prefix, **kwargs):
    return {
        prefix + key: value for key, value in kwargs.items()
    }


make_prefix_dict('super_', grass=True, fly=False, human=True)
# {'super_grass': True, 'super_fly': False, 'super_human': True}


make_prefix_dict(prefix='super_', grass=True, fly=False, human=True)
# {'super_grass': True, 'super_fly': False, 'super_human': True}


make_prefix_dict('super_')
# {}

