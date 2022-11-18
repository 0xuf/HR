import socket
from celery import shared_task
from scan.subfinder import Subfinder
from scan.nuclei import Nuclei
from scan.models import (
    Target, Subdomain
)


@shared_task()
def scan_target(domain: str) -> None:

    subfinder_instance = Subfinder(domain)
    subfinder_output = subfinder_instance.get_subdomains()
    target = Target.objects.get(domain=domain)  # noqa

    if subfinder_output:

        for subdomain in subfinder_output:

            try:
                ip_address = socket.gethostbyname(subdomain)
            except socket.gaierror:
                continue

            sub_object = Subdomain(
                target=target,
                subdomain=subdomain,
                ip_address=ip_address
            )
            nuclei_instance = Nuclei(subdomain)
            nuclei_out = nuclei_instance.nuclei()

            if nuclei_out:
                sub_object.nuclei_result = nuclei_out
                sub_object.save()

        target.status = "finished"
        target.save()

    else:
        target.status = "error"
        target.save()
