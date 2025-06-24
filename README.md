# Railway Deployment with CI/CD

## Deployment Instructions

1. Push to `main` branch triggers the CI pipeline.
2. After tests and Docker build, deployment is handled by Railway's GitHub integration.

## Environment Configuration

- Environment variables and secrets should be configured in Railway dashboard.
- Use `.env` or Railway secrets UI.

## Health Check

- Application root `/` returns 200 OK if healthy.
