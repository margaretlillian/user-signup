import string

class FormValidator:
    
    @staticmethod
    def is_wrong_length(usr_input, min_l, max_l):
        length = len(usr_input)
        return length < min_l or length > max_l

    @staticmethod
    def has_bad_characters(username):
        allowed_chars = string.ascii_letters + string.digits + "_-"
        for char in username:
            if char not in allowed_chars:
                return True

    @staticmethod
    def is_invalid_email(email):
        if email == "":
            return False
        elif len(email) < 3:
            return True
        if "@" in email:
            for char in email:
                if char in " ":
                    return True
                if email.count("@") > 1:
                    return True
                if "@" in email[0] or "@" in email[-1]:
                    return True
                if "." in char:
                    if email.index("@") > email.index("."):
                        return True
                    if "." in email[0] or "." in email[-1]:
                        return True
        else:
            return True