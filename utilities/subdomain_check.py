def is_valid_subdomain(subdomain_list: list, subdomain: str, domain: str) -> bool:
    """
    This function will check subdomain is valid or not
    """
    return True if subdomain not in subdomain_list and not subdomain.startswith("www.") \
                   and subdomain != domain else False
