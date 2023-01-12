#!/usr/bin/env bash

set -eu -o pipefail

USER_ID="$(stat --format='%u' /hop-docs)"
GROUP_ID="$(stat --format='%g' /hop-docs)"
groupadd -g "${GROUP_ID}" hop-docs
useradd -s /bin/bash -u "${USER_ID}" -g "${GROUP_ID}" -M -d /tmp hop-docs

exec chpst -u hop-docs:hop-docs -U hop-docs:hop-docs env HOME="/home/hop-docs" "$@"
