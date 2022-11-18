import subprocess
from utilities.subdomain_check import is_valid_subdomain


class Subfinder:
    """
    Subfinder class
    """
    subdomains: list = list()

    def __init__(self, domain: str = None) -> None:
        """
        Initial method of subfinder class
        :param domain: received domain from request
        """
        self.domain = domain

    def get_subdomains(self) -> list:
        """
        get_subdomains will list subdomains within subfinder script
        """

        # Get all subdomains using subfinder script
        subfinder_command = subprocess.Popen(
            ["/usr/bin/subfinder", "-d", self.domain, "-silent"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()

        # define output and error from subfinder output
        out, err = subfinder_command[0].decode("UTF-8").splitlines(), subfinder_command[1].decode("UTF-8")

        # Return an empty list if subfinder has errors
        if len(err) != 0:
            return list()

        # Loop into subfinder output to validate subdomains and make list from them
        for subdomain in out:
            self.subdomains.append(subdomain) if is_valid_subdomain(self.subdomains, subdomain, self.domain) else ...

        return self.subdomains
