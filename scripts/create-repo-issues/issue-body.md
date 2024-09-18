## Description

The GitGuardian secret scanning tool licence is now expired, therefore in order to maintain the Security of the Tractus-X Repositories there will be inforced the [TRG-8.03](https://eclipse-tractusx.github.io/docs/release/trg-8/trg-8-03) for all Tractus-X repos.

## Incident Ticket

https://github.com/eclipse-tractusx/sig-security/issues/86

Your repository was found in one of our security scans, and it was listed along with other repositories for not contain any of this files:

```md
".github/workflows/trufflehog.yaml"
".github/workflows/trufflehog.yml"
".github/workflows/secrets-scan.yml"
```

Please read the [TRG-8.03](https://eclipse-tractusx.github.io/docs/release/trg-8/trg-8-03) and create the workflow file as soon as posible!

## What needs to be done?

- [ ] Add the Trufflehog workflow like described in [TRG-8.03](https://eclipse-tractusx.github.io/docs/release/trg-8/trg-8-03) to the `/.github/workflows` folder
- [ ] Remove all references to GitGuardian from documentation
- [ ] Create a PR and Merge it to `main`
- [ ] As committer: revise if any secrets were found in the scan (in the security tab)
- [ ] Close this ticket

Thank you very much for doing the update! 🚀

If there is any question, please let us know,  
Your Tractus-X Project Leads 💯