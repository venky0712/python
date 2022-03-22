from github import Github

# Creating this to mass update all of our repos settings.

g = Github("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") # Your personal token

def change_protected_branch_settings():
    # Loops through all the repos and changes the /settings/branch_protection_rules/
    # CAREFUL with this!
    for repo in g.get_user().get_repos():
        branch = repo.get_branch("main")
        branch.edit_protection(required_approving_review_count=2, enforce_admins=True)
        print("Edited the branch protection rules for: " + repo.name)

def change_protected_branch_settings_test():
    repo = g.get_repo("venky0712/python")
    branch = g.get_repo("venky0712/python").get_branch("master")
    branch.edit_protection(required_approving_review_count=2, enforce_admins=True)

# Uncomment out one of these lines. Test to test a single repo/branch.
change_protected_branch_settings()
change_protected_branch_settings_test()