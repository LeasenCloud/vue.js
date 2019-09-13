# nano /home/usuario/terraform_example/mysql_create.tf

# Configuracion the MySQL server
provider "mysql" {
  endpoint = "localhost:3306"
  username = "root"
  password = "root"
}

# Crear base de datos
resource "mysql_database" "app" {
  name = "terraformbbdd"
}
