## Description

Due to a change in how we want to license Eclipse Tractus-X, there are a couple of changes
to legal documentation in our repositories.

This issue is created for every active repository in our GitHub org, to remind everyone
about the required changes and also to track the completion of if.

If there are any reasons, why you think this change should not be applied to this repository,
document them as comment on this issue, before closing it. Be aware, that there are most likely no
exceptions for our repositories.

If you have any questions, feel free to join the weekly [Community Office Hour](https://eclipse-tractusx.github.io/community/open-meetings#Office%20Hour)
and raise it there.

## What has to be done?

The following steps have to be completed, to fully implement the licensing change:

- [ ] Add a new file `LICENSE_non-code` in your repository root with the contents of the CC-BY-4.0 license
- [ ] Remove the `/LICENSES` directory in case you previously stored the CC-BY-4.0 license there. Make sure there is no other CC-BY-4.0 License left, other than on root as `LICENSE_non-code`
- [ ] Add the "Project Licenses" and "Terms of Use" sections to your `CONTRIBUTING.md` file. See eclipse-tractusx/sig-infra#476 for an example
- [ ] Adapt "Declared Project License" section in `NOTICE.md`. See eclipse-tractusx/sig-infra#476 for an example
- [ ] Please verify, your `CONTRIBUTION.md` does not have encoding issues. We found several occurences in repositories.

## Additional information

You can find detailed information in our [Release Guidelines](https://eclipse-tractusx.github.io/docs/release) section 7.
The changes have been introduces in eclipse-tractusx/eclipse-tractusx.github.io#856.

You can also see an example on how a repository was changed in eclipse-tractusx/sig-infra#476.

Overall progress tracked in eclipse-tractusx/sig-infra#477
