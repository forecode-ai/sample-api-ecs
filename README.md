# sample-api-ecs

Part of the ForeCode test estate. Not a real product.

A small Python HTTP API, built as a container image and deployed to Amazon ECS (Fargate): to `staging` on every change
to `main` and on a schedule, and to `production` when run manually (the `production` environment needs an approval).

Deploys are simulated: `.github/simulate.sh` makes the deploy tools print what they would do. The AWS sign-in step
is skipped while the repository variable `AWS_ROLE_ARN` is unset.
