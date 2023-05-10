def get_header(STRIPE_SECRET_KEY:str) -> dict:
    """ 
    :param STRIPE_SECRET_KEY EdlRFdnlUIi0NqYbak5TyrP3zwB1VO0e6y198vLgIZ4jaquN7aTET6gOYOsVnmoW
    :return {"x-client-key": f"Application {STRIPE_SECRET_KEY}"}
    """
    return {"x-client-key": f"Application {STRIPE_SECRET_KEY}"}
        