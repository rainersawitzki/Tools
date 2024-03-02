from github import Github

def list_organization_repositories(org_name, github_token):

    # Create a GitHub instance using your personal access token
    g = Github(github_token)
    with open("report.txt", "w") as file:
        try:
            # Get the organization
            org = g.get_organization(org_name)

            # Get all repositories for the organization
            repositories = org.get_repos()

            file.write(f"Repositories in organization '{org_name}':\n")
            for repo in repositories:
                file.write(f"\t{repo.full_name}\n")
                for branch in repo.get_branches():
                    file.write(f"\t\t{branch.name}\n")
                    print(branch.name)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with your organization name and personal access token
    organization_name = "Javacream"
    github_access_token = "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"

    list_organization_repositories(organization_name, github_access_token)
