def charge() ->dict[str,str]:
    user = {"1": "Hourly", "2": "Daily", "3": "Monthly"}
    return user


def charge_hourly()->dict:
    user = {
        "1": ("charge : 20 minuts for one hour ",5400),
        "2": ("charge : 30 minuts for one hour ",10000),
        "3": ("charge : 35 minuts for one houur ",15000),
        "4": ("charge : 45 minuts for one hour ",18000),
    }
    return user


def charge_daily()->dict:
    user = {
        "1": ("charge : 200 minuts for one day ",22400),
        "2": ("charge : 300 minuts for one day ",44200),
        "3": ("charge : 350 minuts for one day ",65000),
        "4": ("charge : 420 minuts for one day ",80430),
    }
    return user


def charge_monthly()->dict:
    user = {
        "1": ("charge : 1000 minuts for one month ",9400),
        "2": ("charge : 2000 minuts for one month ",123930),
        "3": ("charge : 3000 minuts for one month ",150400),
        "4": ("charge : 3500 minuts for one month ",205400),
    }
    return user
