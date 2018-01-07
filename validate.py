import string

class FormValidator:
    def __init__(self, usr_input, min_l, max_l):
        self.usr_input = usr_input
        self.min_l = min_l
        self.max_l = max_l

    def is_wrong_length(self):
        length = len(self.usr_input)
        return length < self.min_l or length > self.max_l

    def has_bad_characters(self):
        allowed_chars = string.ascii_letters + string.digits + "_-"
        for char in self.usr_input:
            if char not in allowed_chars:
                return True

    def is_invalid_email(self):
        email = self.usr_input
        if email == "":
            return False
        elif len(email) < 3:
            return True
        if "@" in email:
            if "@" in email:
                for char in email:
                    if char in " " \
                    or email.count("@") > 1 \
                    or "@" in email[0] \
                    or "@" in email[-1]:
                        return True
                    if "." in char:
                        if "." in email[0] or "." in email[-1]:
                            return True
                        return True
        else:
            return True

    def __str__(self):
        return self.usr_input