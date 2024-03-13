import ckan.plugins.toolkit as tk
import ckanext.utch.logic.schema as schema


@tk.side_effect_free
def utch_get_sum(context, data_dict):
    tk.check_access(
        "utch_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.utch_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'utch_get_sum': utch_get_sum,
    }
