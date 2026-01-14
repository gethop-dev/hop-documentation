# Setup for editing and generating the documenation locally with Docker

The documenation uses the ["Read the Docs" documentation toooling and platform]()https://readsthedocs.com/)

## Prerequisites

Make sure you have the following instaled on your system.

- Docker Engine: [Installation Instructions](https://docs.docker.com/engine/install/)
- Docker Compose: [Installation Instructions](https://docs.docker.com/compose/install/)

## Configuration Steps

### 1. Clone the git repository

```bash
git clone https://github.com/gethop-dev/hop-documentation.git
```

### 2. Navigate to the git repotiroy directory


```bash
cd hop-documentaion
```

### 3. Build and Run the Containers

  ```bash
    docker-compose up --build
```

This will build the necessary images and run the containers according to the configuration in `docker-compose.yml`.

### 4. Access Your Application

Open a web browser and visit `http://localhost:8080` (or the port you specified in `docker-compose.yml`) to access the local copy of the generated documentation.

---
