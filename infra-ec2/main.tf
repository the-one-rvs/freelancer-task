resource "aws_key_pair" "k8s_key" {
  key_name   = "k8s-key"
  public_key = file("~/.ssh/k8s-key.pub")
}

resource aws_instance "example" {
  ami           = "ami-075449515af5df0d1" 
  instance_type = "t3.micro"
  key_name      = aws_key_pair.k8s_key.key_name
  subnet_id     = aws_subnet.public-subnet.id
  vpc_security_group_ids = [aws_security_group.task-sg.id]  

  tags = {
    Name = "Task 1 - EC2 Instance"
  }
}