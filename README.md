# Code Challenge: DevSecOps and Site Reliability Engineers

**Important: Please read through all of this before starting.**

Overjet Confidential. It is prohibited to distribute or share this test without explicit permission from Overjet.

This is a Site Reliability, DevOps, and Security assignment as part of the Overjet interview process.

This test has 2 tasks, each designed to test a different set of skills required for the position.

## Tasks

1. Build Terraform infrastructure for a local kubernetes cluster.
2. Setup a local CI/CD pipeline to build and deploy the provided Docker image.

## Instructions

Our goal is to understand your experience and thought process, so please complete as many of these steps as possible, and be prepared to talk about what you were or were not able to complete:

1. Clone this repository to local machine.
2. Set up tools/environment.
3. Develop the Terraform configs.
4. Develop the CI/CD pipeline.
5. Ensure that the cluster and pipeline are secure.
6. Commit and push changes to this repository.
7. Update `README.md` with instructions for setting up this repo locally, installing tools, provisioning infrastructure, and running the CI/CD pipeline.

### Terraform/Kubernetes Requirements

You **must** use Terraform and Kubernetes for this task, but may use any tool for a local Kubernetes cluster.

Suggested Tools for Kubernetes: Minikube

- Write Terraform configs to provision infrastructure on a local k8s cluster.
  - The deployed service should be able to scale to **10 parallel instances**
  - The deployed service should be able to handle at least **100 requests/second** (per cluster)
- This cluster should be as secure possible (within reason), a penetration test will be done on the cluster.

### Continuous Integration/Delivery Requirements

You may use any CI/CD tool that you are comfortable with, but please ensure that it is runnable locally.

Suggested Tools: Bash, GitHub Actions, Skaffold

1. Build the Docker image.
    - You may modify the `Dockerfile` as needed, but don't modify the Python code.
2. Tag the built image with `latest` and the latest commit hash.
    - Use the full hash, _e.g._: `88e10c1ec42c794ea91851de059ddeaac28683cb` instead of `88e10c1`
3. Write and run a simple integration test:
    1. Start a new container instance from the built image
    2. Query the endpoint `/hash/abc123`
    3. Check that the returned value equals `6367c48dd193d56ea7b0baad25b19455e529f5ee`
4. On passing the test, deploy it to the local kubernetes cluster.

## Evaluation Criteria

Our goal is to understand your experience and thought process, these are not hard-and-fast "points" or achievements, but please be prepared to speak to these topics:

- Terraform/Kubernetes:
  - Reliability
  - Ease of Use
  - Scalability
- CI/CD pipeline:
  - Automation
  - Monitoring/Alerting
  - Successful Testing/Deployment
- Security of the entire infrastructure and pipeline should use industry best practices.
- Git usage will be taken into consideration but is not a requirement.

Also, please consider that the provided code/configs are not necessarily ideal. How would you suggest they be improved? Did you notice any issues with them while working on this challenge?

## Notes

- You may use any language/tool for the integration test.
- There is no requirement to upload the Docker image to a container registry.
- There is no requirement to deploy this on a Cloud Service (AWS/GCP), although please ensure that it can run in a local development environment.
