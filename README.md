# StackHPC OpenStack GitHub Workflows

Reusable GitHub workflows and actions for StackHPC OpenStack.

## Workflows

The following reusable workflows are provided in the `.github/workflows/`
directory.

### `multinode.yml`

The `multinode.yml` workflow can be used to create a multinode test cluster and
run tests and/or operations against it.

Features:

* Inject an SSH key to access the cluster
* Break (pause) the workflow on failure
* Upgrade from one OpenStack release to another

## Actions

The following actions are provided in the top-level directory.

### `sanitise-artifact-filenames`

Sanitise filenames for GitHub Actions artifacts.
