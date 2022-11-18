import subprocess


class Nuclei:
    """
    Nuclei class
    """
    def __init__(self, domain: str) -> None:
        """
        Initial method of Nuclei class
        :param domain: received domain from request
        """
        self.domain = domain

    def nuclei(self) -> list:

        # Get data from nuclei script
        nuclei_command = subprocess.Popen(
            ["nuclei", "-u", self.domain, "-silent", "-nc"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()

        # define output and error from nuclei output
        out, err = nuclei_command[0].decode("UTF-8").splitlines(), nuclei_command[1].decode("UTF-8")

        # Return an empty list if nuclei has errors
        if len(err) != 0:
            return list()

        return out
