# restricted-codespace-test

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/uw-escience-cloudbank/restricted-codespace-test?quickstart=1)

Click the button above to open a [CodeSpace](https://github.com/features/codespaces) (Azure Virtual Machine) paid for by a [CloudBank](https://github.com/features/codespaces) Azure Subscription that is connected to UW eScience [SSEC LLMoxie](https://github.com/uw-ssec/llmoxie) gateway with provisioned access to Anthropic Models via AWS Bedrock running on a CloudBank Account.

Currently only two models are available:
- `cloudbank-claude-haiku-4-5` (Claude Haiku 4.5)
- `cloudbank-claude-sonnet-4-6` (Claude Sonnet 4.6)

Phew. That's a mouthful. But the point is that you can run VSCode in your browser and have access to Anthropic Claude models without having to install anything on your local machine.

VSCode in the browser will open very quickly. However, it will take a minute or two to install various extensions and features.

**Important** if you 'Stop' the codespace, the state of your VM is preserved so that you can come back to it later. However, if you 'Delete' the codespace, it will be gone forever and you will have to start over.

**Important** The GitHub Copilot extension also allows you to connect to Anthropic models, and enforces a monthly quota linked to your GitHub user account. Only `claude` in a terminal or the `claude-code` extension in VSCode will use the CloudBank subscription and not your personal GitHub account.

