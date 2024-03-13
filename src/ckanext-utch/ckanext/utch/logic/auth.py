import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def utch_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "utch_get_sum": utch_get_sum,
    }
