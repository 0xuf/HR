import subprocess


class Nuclei:

    def __init__(self, domain: str) -> None:
        self.domain = domain

    def nuclei(self) -> list:
        nuclei_command = subprocess.Popen(
            ["nuclei", "-u", self.domain, "-silent", "-nc"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()

        out, err = nuclei_command[0].decode("UTF-8").splitlines(), nuclei_command[1].decode("UTF-8")

        if len(err) != 0:
            return list()

        return out
