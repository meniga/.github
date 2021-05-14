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

This workflow demonstrates how to build a docker container using docker buildx 
and caching image layers to GitHub cache to for faster builds. Additionally it 
lints the Dockerfile, scans for vulnerabilities and pushes the container if 
built of specific branches or a tag was pushed.

## Debug GitHub Actions

Logs various objects in the GitHub context, i.e. github, job, steps, runner, 
strategy and matrix. Useful for troubleshooting workflows that are not running
as expected.

## psake CI

This workflow demonstrates how you can use a self-hosted Windows runner
to migrate a legacy build process that relies on internal tooling and `psake`.

> This workflow should only be used as a temporary solution for build processes
that still rely on legacy build tools and cannot migrate to cloud runners 

## psake TryCI

Same as psake CI, except for running `psake tryci`

## Publish NuGet Packages (.NET)

Demonstrates how you can publish NuGet packages to the Meniga GitHub Package
registry. This workflow is not compatible with .NET Framework projects.

## Publish NuGet Packages (.NET Framework)

Demonstrates how you can publish NuGet packages to the Meniga GitHub Package
registry. Only meant for .NET Framework projects that rely on Windows for 
building.