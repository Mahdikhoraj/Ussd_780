def internet()->dict[str,str]:
    user = {"1": "Daily", "2": "Weekly", "3": "Monthly", "4": "Yearly"}
    return user

def internet_daily()->dict:
    user = {
        "1": ("1 GB Internet for per day : ",12700),
        "2": (" 2 GB for three days Internet :",23200),
        "3": (" 3 GB for five days Internet :", 29800),
    }
    return user


def internet_weekly()->dict:
    user = {
        "1": ("1 GB for a week Internet :",18000),
        "2": ("2.5 GB for a week Internet :",23000),
        "3": ("3 GB for a week Internet :",28000),
        "4": ("5 GB for two week Internet :",32000),
        "5": ("7 GB for two week Internet : ",36000),
    }
    return user


def internet_monthly()->dict:
    user = {
        "1": ("1 GB for a month Internet : ",22000),
        "2": ("2 GB for a mounth Internet : ",32000),
        "3": ("3 gig for a mounth Internet : ",48000),
        "4": ("5 GB for two mounth Internet :",63000),
        "5": ("10 GB for two mounth Internet :",70000),
        "6": ("3 GB for three mounth Internet : ",12000),
    }
    return user


def internet_yearly()->dict:
    user = {
        "1": (" 30 GB for a year Internet :", 649000),
        "2": (" 55 GB for a year Internet : ", 740000),
        "3": ("70 GB for a year  Internet : ", 820000),
        "4": ("100 GB for a year Internet : ", 950000),
        "5": ("150 GB for a year Internet :", 1000000),
        "6": ("300 GB for a year Internet : ", 1700000),
    }
    return user
