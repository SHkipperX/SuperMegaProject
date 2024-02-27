from django.contrib.auth.models import UserManager

__all__ = []


class CustomUserManager(UserManager):
    DOMAIN = {
        "ya.ru": "yandex.ru",
        "yandex.ru": "yandex.ru",
        "gmail.com": "gmail.com",
    }
    DOT_DOMAIN = {
        "yandex.ru": "-",
        "gmail.com": "",
    }

    def create_superuser(
        self,
        username,
        email,
        password,
        **extra_fields,
    ):
        superuser = super().create_user(
            username,
            email,
            password,
            **extra_fields,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save()

    @classmethod
    def normalize_email(
        cls,
        email,
    ):
        email = super().normalize_email(email).lower()
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
            if "+" in email:
                email_name = email.split("+")[0]
            if cls.DOMAIN.get(domain_part):
                domain_part = cls.DOMAIN[domain_part]
                if cls.DOT_DOMAIN.get(domain_part) is not None:
                    email_name = email_name.replace(
                        ".",
                        cls.DOT_DOMAIN[domain_part],
                    )
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email

    def by_mail(
        self,
        mail,
    ):
        email = self.normalize_email(mail)
        return super().get_queryset().get(email=email)
