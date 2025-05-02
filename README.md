 # AI-Powered Multi-Factor Authentication for Academic Environments

This project implements an intelligent Multi-Factor Authentication (MFA) system specifically designed for academic institutions. It uses behavioral patterns and contextual information to enhance security while maintaining usability.

## Features

- Role-based authentication scenarios (undergraduate, graduate, faculty, admin, research)
- Context-aware authentication (academic calendar periods, time pressure levels)
- Behavioral biometrics analysis (keystroke dynamics, application usage patterns)
- Attack detection and prevention
- Simulated workflow generation for testing and training

## Project Structure

- `index.py`: Main application entry point
- `simulate_workflows.py`: Workflow scenario generator
- `preprocess.py`: Data preprocessing utilities
- `train_models.py`: Model training pipeline
- `evaluate.py`: Model evaluation tools
- `generate_abbd.py`: Academic behavioral biometric data generator
- `generate_uald.py`: User activity log data generator

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python index.py
```

## Data Structure

The project generates and processes data in the following format:
- Workflow scenarios stored in `data/workflow_scenarios.json`
- Behavioral data including keystroke patterns and application transitions
- Authentication events with device and location information

## Security Considerations

- All sensitive data should be properly encrypted
- API keys and credentials should be stored in environment variables
- Regular security audits should be performed
- Follow the principle of least privilege for access control

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.