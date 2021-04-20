# Workflow templates

## Automerge

Emulates the `auto-merge` behavior many are used to in BitBucket.
You can include this in your project to always attempt to merge changes
made on one branch (`source`) with another branch (`target`). If the merge
fails then a pull request is created.

## Legacy CI

This workflow simply demonstrates how you can use a self-hosted Windows runner
to migrate a legacy build process that relies on `psake` as an example.

> This workflow should only be used as a temporary solution for build processes
that still rely on legacy build tools and cannot migrate to cloud runners 

## Publish NuGet Packages (.NET)

Demonstrates how you can publish NuGet packages to the Meniga GitHub Package
registry. This workflow is not compatible with .NET Framework projects.

## Publish NuGet Packages (.NET Framework)

Demonstrates how you can publish NuGet packages to the Meniga GitHub Package
registry. Only meant for .NET Framework projects.