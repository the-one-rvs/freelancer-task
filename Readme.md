# DevOps Project: Node.js App Deployment with Jenkins CI/CD

## Overview
This project implements a complete CI/CD pipeline that:
- Creates AWS infrastructure using Terraform
- Builds and scans a Node.js application Docker image
- Deploys the application to an EC2 instance
- Verifies the deployment using a Python script

## Infrastructure (Terraform)

### Prerequisites
- AWS CLI configured
- Terraform installed
- SSH key pair generated (`~/.ssh/k8s-key.pub`)

### Running Terraform
1. Navigate to the infrastructure directory:
```bash
cd infra-ec2
```

2. Initialize Terraform:
```bash
terraform init
```

3. Review the planned changes:
```bash
terraform plan
```

4. Apply the infrastructure:
```bash
terraform validate
terraform apply
```

5. To destroy the infrastructure:
```bash
terraform destroy
```

## CI/CD Pipeline (Jenkins)

### Prerequisites
- Jenkins installed with following plugins:
  - Docker Pipeline
  - GitHub Integration
  - SSH Agent
- Docker Hub credentials configured in Jenkins as 'dockerhubcred'
- SSH private key configured in Jenkins credentials

### Triggering the Pipeline
1. Manual Trigger:
   - Open Jenkins dashboard
   - Navigate to your pipeline
   - Click "Build Now"

2. Automatic Trigger:
   - Push to GitHub repository
   - Pipeline configured to trigger on:
     - GitHub webhooks
     - SCM polling every minute

### Pipeline Stages
1. Source Code Checkout
2. Docker Image Build
3. Security Scan with Trivy
4. Push to Docker Hub
5. Deploy to EC2

## Deployment Verification

### Using the Ping Script
1. Get the EC2 public IP:
```bash
cd infra-ec2
terraform output ec2_public_ip
```

2. Run the verification script:
```bash
python3 ping-script.py
```

3. When prompted, enter the EC2 public IP address

### Expected Output
- Success message if application responds with 200 OK
- Retry mechanism if initial attempts fail
- Detailed error messages for troubleshooting

## Project Structure
```
.
├── infra-ec2/              # Terraform infrastructure
│   ├── main.tf            # EC2 instance configuration
│   ├── vpc.tf             # VPC and networking
│   ├── provider.tf        # AWS provider configuration
│   └── outputs.tf         # Output definitions
├── pipeline/              # CI/CD pipeline
│   ├── Jenkinsfile       # Pipeline definition
│   ├── docker-install.sh # Docker installation script
│   └── app/              # Node.js application
└── ping-script.py        # Deployment verification
```

## Security Notes
- Security group allows inbound traffic on ports 22 (SSH) and 80 (HTTP)
- Using SSH key authentication for EC2 access
- Docker images scanned for vulnerabilities using Trivy