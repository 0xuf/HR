import socket
from celery import shared_task
from scan.subfinder import Subfinder
from scan.nuclei import Nuclei
from scan.models import (
    Target, Subdomain
)


@shared_task()
def scan_target(domain: str) -> None:
    """
    Scan target function created for scan received target from user in background within celery
    :param domain: received domain from request
    """

    # Subfinder instance
    subfinder_instance = Subfinder(domain)
    subfinder_output = subfinder_instance.get_subdomains()

    # target object
    target = Target.objects.get(domain=domain)  # noqa

    # Nuclei on subdomains of subfinder works
    if subfinder_output:
        # Loop into subdomains of subfinder output
        for subdomain in subfinder_output:
            # Check target is up or not
            try:
                ip_address = socket.gethostbyname(subdomain)
            except socket.gaierror:
                continue

            # Subdomain instance
            sub_object = Subdomain(
                target=target,
                subdomain=subdomain,
                ip_address=ip_address
            )

            # Nuclei instance
            nuclei_instance = Nuclei(subdomain)
            nuclei_out = nuclei_instance.nuclei()

            # Save nuclei result into subdomain instance if has result
            if nuclei_out:
                sub_object.nuclei_result = nuclei_out
                sub_object.save()

        # Change target status to finished
        target.status = "finished"
        target.save()

    else:
        # Change target status to error
        target.status = "error"
        target.save()
