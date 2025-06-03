# How to publish a new version for the `latest` tag in ReadTheDocs

Commit your changes, or merge them from other branch(es), to the `dev`
git branch. And then push that branch to Github.

# How to publish a new version for the `stable` tag in ReadTheDocs

Commit your changes, or merge them from other branch(es), to the
`main` git branch. Then add a git tag to the most recent commit in
that branch (e.g., using the HOP CLI version that matches the
documentation changes). And then push that branch to Github, **and**
the git tag you created in the previous step.

It's pushing the git tag what actually triggers the build in
ReadTheDocs.

