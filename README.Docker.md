# Docker Setup for TimeClock

This directory contains Docker configuration for running the TimeClock application with PostgreSQL.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Build and start the containers:

```bash
docker-compose up -d
```

2. The application will be available at http://localhost:5000

3. Stop the containers:

```bash
docker-compose down
```

## Database Management

The database is automatically initialized when the containers start.

To reset the database:

```bash
docker-compose exec web flask reset_db
```

To create development users:

```bash
docker-compose exec web flask create_dev_users
docker-compose exec web flask create_health_screen_users
```

## Development

Code changes in the local directory will be reflected in the running application due to the volume mount. However, for some changes (like installing new dependencies), you may need to rebuild:

```bash
docker-compose up -d --build
```

## Database Connection

The PostgreSQL database is accessible from host machine at:
- Host: localhost
- Port: 5432
- User: developer
- Password: developer_password
- Database: timeclock_dev