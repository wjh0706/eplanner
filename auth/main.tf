provider "aws" {
  region = "us-east-1"  # Replace with your desired AWS region
  access_key = "YOUR KEY"
  secret_key = "YOUR KEY"
}

resource "aws_instance" "example" {
  ami           = "ami-079db87dc4c10ac91"  # Replace with your desired AMI
  instance_type = "t2.micro"               # Replace with your desired instance type
}
