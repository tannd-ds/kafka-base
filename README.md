# Camera Stream Processing System

A production-ready Kafka-based system for processing camera streams using PyTorch for deep learning tasks.

## Features

- Kafka-based streaming infrastructure
- Camera stream producers
- Data processing consumers
- PyTorch integration for deep learning tasks
- Docker support for easy deployment
- Configurable through YAML files
- Robust error handling and logging

## Project Structure

```
.
├── config/
│   └── config.yaml
├── src/
│   ├── producers/
│   │   └── camera_producer.py
│   ├── consumers/
│   │   └── stream_processor.py
│   ├── models/
│   │   └── base_model.py
│   └── utils/
│       ├── config.py
│       └── logger.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your environment:
- Copy `.env.example` to `.env`
- Update the configuration in `config/config.yaml`

3. Run with Docker:
```bash
docker-compose up
```

## Usage

### Non-Docker

1. Start the Kafka cluster:
```bash
docker-compose up -d kafka zookeeper
```

2. Run the camera producer:
```bash
python src/producers/camera_producer.py
```

3. Run the stream processor:
```bash
python src/consumers/stream_processor.py
```

### Docker

1. Build the Docker image:
```bash
cd docker
docker-compose up --build
```

2. To run Flask app:
```bash
docker exec -it <container_id> /bin/bash
python src/app.py
```


## Configuration

The system can be configured through:
- Environment variables (`.env` file)
- YAML configuration (`config/config.yaml`)

## Development

- Follow PEP 8 style guide
- Use type hints
- Write docstrings for all functions and classes
- Add unit tests for new features

## License

MIT License 