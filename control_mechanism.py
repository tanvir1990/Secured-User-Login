import warnings

def can_access(role):
    role1 = {
        "role_type": "Regular_Client",
        "operations": "View Account Balance, View Investment Portfolio, View Contact Details"
    }
    role2 = {
        "role_type": "Premium_Client",
        "operations": "View Account Balance, Modify Investment Portfolio, View Contact Details"
    }
    role3 = {
        "role_type": "Financial_Advisor",
        "operations": "Modify Client's Investment Portfolio, View Private Consumer instruments"
    }
    role4 = {
        "role_type": "Financial_Planner",
        "operations": "Modify Client's Investment Portfolio,View Private Consumer instruments,View Money Market instruments"
    }
    role5 = {
        "role_type": "Investment_analyst",
        "operations": "Modify Client's Investment Portfolio,View Private Consumer instruments,View Money Market instruments,View Derivatives trading,View interests instruments"
    }
    role6 = {
        "role_type": "Compliance_Officer",
        "operations": "Validation of Client's investment portfolio"
    }
    role7 = {
        "role_type": "Teller",
        "operations": "Can access system only during 9am to 5pm"
    }
    role8 = {
        "role_type": "Technical_Support",
        "operations": "View Client Information,Request Client's account access"
    }
    if role == role1.get("role_type"):
        return role1
    elif role == role2.get("role_type"):
        return role2
    elif role == role3.get("role_type"):
        return role3
    elif role == role4.get("role_type"):
        return role4
    elif role == role5.get("role_type"):
        return role5
    elif role == role6.get("role_type"):
        return role6
    elif role == role7.get("role_type"):
        return role7
    elif role == role8.get("role_type"):
        return role8
    else:
        warnings.warn("role " + role + " Not Found")






