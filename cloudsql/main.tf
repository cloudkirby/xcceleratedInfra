resource "google_sql_database_instance" "main" {
  name             = "main-instance-v2"
  database_version = "POSTGRES_15"
  region           = "europe-west4"

  timeouts {
    create = "40m"
    update = "40m"
    delete = "40m"
  }

  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "database" {
  name     = "my-database"
  instance = google_sql_database_instance.main.name
}
