# Workflow templates

## Automerge

Emulates the `auto-merge` behavior many are used to in BitBucket.
You can include this in your project to always attempt to merge changes
made on one branch (`source`) with another branch (`target`). If the merge
fails then a pull request is created.

## Create Release (.NET)

This workflow demonstrates how you can create a GitHub Release. It targets the 
`linux-x64` and `windows-x64` platforms and creates a release for each one.

## Container CI

This workflow demonstrates how to build a Linux Docker container. 
Additionally it lints the Dockerfile, scans for vulnerabilities and pushes 
the container if built of specific branches or a tag was pushed.

## Debug GitHub Actions

Logs various objects in the GitHub context, i.e. github, job, steps, runner, 
strategy and matrix. Useful for troubleshooting workflows that are not running
as expected.

## psake CI

This workflow demonstrates how you can use a self-hosted Windows runner
to migrate a legacy build process that relies on internal tooling and `psake`.

> This workflow should only be used as a temporary solution for build processes
that still rely on legacy build tools and cannot migrate to cloud runners 

## psake release

This workflow demonstrates how you can use a self-hosted Windows runner
to migrate a legacy build process that relies on internal tooling and `psake`.

It only runs when a git `tag` is pushed and creates a GitHub release that is
linked to that `tag`.

## psake TryCI

Same as psake CI, except for running `psake tryci`

## Publish NuGet Packages (.NET)

Demonstrates how you can publish NuGet packages to the Meniga GitHub Package
registry. This workflow is not compatible with .NET Framework projects.

## Publish NuGet Packages (.NET Framework)

Demonstrates how you can publish NuGet packages to the Meniga GitHub Package
registry. Only meant for .NET Framework projects that rely on Windows for 
building.

## Terraform Plan

This workflow is meant to be run whenever a new pull request is created or when
said pull request is updated. It creates a Terraform plan according to the 
changes made to the project and comments the output of the plan in addition 
to some other useful information gathered by Terraform.

The workflow is split up into two jobs.

### terraform-plan

Creates the plan as previously mentioned and comments on the pull request.

### cleanup-comments

This job executes before the `terraform-plan` job and all it does is remove 
previous comments on the pull request since those plans have become stale.

## Terraform Apply

This workflow is meant to run when changes in a pull request have been merged 
with one of the main branches in the repository. It applies the Terraform plan
that was created in the pull request. Pushing changes directly to the branches 
defined in the trigger will also run `terraform apply` but you will not get a 
chance to review the plan, so we strongly encourage the use of the 
[Terraform Plan](./workflow-templates/terraform-plan.yml) workflow.