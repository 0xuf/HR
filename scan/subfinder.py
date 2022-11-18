import subprocess
from utilities.subdomain_check import is_valid_subdomain


class Subfinder:
    subdomains: list = list()

    def __init__(self, domain: str = None) -> None:
        self.domain = domain

    def get_subdomains(self) -> list:

        # Get all subdomains using subfinder script
        subfinder_command = subprocess.Popen(
            ["/usr/bin/subfinder", "-d", self.domain, "-silent"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()

        out, err = subfinder_command[0].decode("UTF-8").splitlines(), subfinder_command[1].decode("UTF-8")

        if len(err) != 0:
            return list()

        for subdomain in out:
            self.subdomains.append(subdomain) if is_valid_subdomain(self.subdomains, subdomain, self.domain) else ...

        return self.subdomains
