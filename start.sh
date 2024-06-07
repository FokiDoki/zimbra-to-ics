#!/bin/bash
docker run --network=host --name "zimbra_calendar_exporter" --env-file docker.env -p 4443:4443 -v $(pwd)/certs:/var/certs -v $(pwd)/db.kdbx:/var/db.kdbx -d zimbra_calendar_exporter