# Sanitise Artifact Filenames

This action sanitises directory and file names for GitHub Actions artifacts.
Example error from the upload-artifact action if you have an invalid path:

> Error: The path for one of the files in artifact is not valid:
> /tempest-artifacts.2024-08-29T18:18+00:00/docker.log. Contains the following
> character:  Colon :
>
> Invalid characters include:  Double quote ", Colon :, Less than <, Greater than
> >, Vertical bar |, Asterisk *, Question mark ?, Carriage return \r, Line feed
> \n
>
> The following characters are not allowed in files that are uploaded due to
> limitations with certain file systems such as NTFS. To maintain file system
> agnostic behavior, these characters are intentionally not allowed to prevent
> potential problems with downloads on different file systems.

## Usage

```yaml
- name: Sanitise filenames for artifacts
  uses: stackhpc/stackhpc-openstack-gh-workflows/sanitise-artifact-filenames@main
  with:
    path: path/to/artifact/
```
