from github import Github
from dateutil import parser
import datetime
def check_company_branch_name(branch_name):
    # Extract the potential date substring from the end of the input string
    splitted = branch_name.split("_")
    splitted_length = len(splitted)
    if splitted_length > 1:
        potential_date_str =splitted [splitted_length - 1]    
        # Try parsing the potential date
        try:
            parsed_date = parser.parse(potential_date_str)
            return (True, potential_date_str)
        except ValueError:
            # Parsing failed
            return (False, branch_name)
    else:
        return (False, branch_name)

def change_branch_name(repo, branch, protocol_file):

    change_name = check_company_branch_name(branch.name)
    try:
        if change_name[0]:
                new_branch_name = change_name[1]

                # Create a new branch based on the old branch
                repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=branch.commit.sha)

                # Delete the old branch
                repo.get_git_ref(f"heads/{branch.name}").delete()

                protocol_file.write(f"Branch name in repo {repo.name} changed from {branch.name} to {new_branch_name}.\n")
        else:
            protocol_file.write(f"Branch name  in repo {repo.name} unchanged: {branch.name}.\n")
    except Exception as e:
        protocol_file.write(f"**** ERROR in repo {repo.name} and {branch.name}: {e}.\n")
def list_organization_repositories(org_name, github_token):
    with open(f"protocol-{str(datetime.datetime.now().timestamp())}.txt", "w") as protocol_file:
            
        # Create a GitHub instance using your personal access token
        g = Github(github_token)
        try:
            # Get the organization
            org = g.get_organization(org_name)

            # Get all repositories for the organization
            repositories = org.get_repos()

            for repo in repositories:
                for branch in repo.get_branches():
                    change_branch_name(repo, branch, protocol_file)

        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    organization_name = "Javacream"
    github_access_token = "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"

    list_organization_repositories(organization_name, github_access_token)
