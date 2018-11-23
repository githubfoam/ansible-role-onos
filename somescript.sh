
#!/bin/sh
curl -H "Content-Type: application/json" --data '{"source_type":"Branch", "source_name":"ubuntu-18.04"}' && \ -X POST https://registry.hub.docker.com/u/dockerfoam/onos/trigger/$(DOCKER_TOKEN)/
